import requests
import random
import string

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from srca.configs import addCommand, Client


BASE_URL = "https://api.mail.tm"

# =========================================
# GUARDAR EMAILS TEMPORALES
# =========================================

temp_mails = {}


# =========================================
# COMANDO MAIL
# =========================================

@addCommand("mail")
def mail(_, m):

    try:

        # =====================================
        # USERNAME RANDOM
        # =====================================

        username = ''.join(
            random.choice(string.ascii_lowercase)
            for _ in range(10)
        )

        password = "Password123"

        # =====================================
        # OBTENER DOMINIOS
        # =====================================

        domains_response = requests.get(
            f"{BASE_URL}/domains"
        )

        if domains_response.status_code != 200:

            return m.reply(
                f"❌ Error API\n<code>{domains_response.text}</code>"
            )

        data = domains_response.json()

        if "hydra:member" not in data:

            return m.reply(
                "❌ Error obteniendo dominios."
            )

        domains = data["hydra:member"]

        if len(domains) == 0:

            return m.reply(
                "❌ No hay dominios disponibles."
            )

        # =====================================
        # DOMINIO
        # =====================================

        domain = domains[0]["domain"]

        # =====================================
        # CREAR EMAIL
        # =====================================

        email = f"{username}@{domain}"

        account_data = {
            "address": email,
            "password": password
        }

        # =====================================
        # CREAR CUENTA
        # =====================================

        create_response = requests.post(
            f"{BASE_URL}/accounts",
            json=account_data
        )

        if create_response.status_code not in [200, 201]:

            return m.reply(
                f"❌ Error creando cuenta\n<code>{create_response.text}</code>"
            )

        # =====================================
        # LOGIN
        # =====================================

        token_response = requests.post(
            f"{BASE_URL}/token",
            json=account_data
        )

        if token_response.status_code != 200:

            return m.reply(
                f"❌ Error login\n<code>{token_response.text}</code>"
            )

        token_data = token_response.json()

        if "token" not in token_data:

            return m.reply(
                "❌ No se recibió token."
            )

        token = token_data["token"]

        headers = {
            "Authorization": f"Bearer {token}"
        }

        # =====================================
        # GUARDAR SESION
        # =====================================

        temp_mails[m.from_user.id] = {
            "headers": headers,
            "email": email
        }

        # =====================================
        # BOTON
        # =====================================

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📩 Revisar Emails",
                        callback_data=f"mailcheck_{m.from_user.id}"
                    )
                ]
            ]
        )

        # =====================================
        # RESPUESTA
        # =====================================

        text = f"""<b>

📧 EMAIL TEMPORAL GENERADO

━━━━━━━━━━━━━━━

• EMAIL:
<code>{email}</code>

━━━━━━━━━━━━━━━

📥 Presiona el botón para revisar correos.

</b>"""

        m.reply(
            text,
            reply_markup=keyboard
        )

    except Exception as e:

        m.reply(
            f"❌ ERROR\n<code>{e}</code>"
        )


# =========================================
# CALLBACKS
# =========================================

@Client.on_callback_query()
def clod(_, call):

    try:

        # =====================================
        # VALIDAR CALLBACK
        # =====================================

        if "_" not in call.data:
            return

        data = call.data.split("_")

        # =====================================
        # VALIDAR TAMAÑO
        # =====================================

        if len(data) < 2:
            return

        # =====================================
        # SOLO mailcheck
        # =====================================

        if data[0] != "mailcheck":
            return

        # =====================================
        # USER ID
        # =====================================

        user_id = int(data[1])

        # =====================================
        # BLOQUEAR BOTONES
        # =====================================

        if call.from_user.id != user_id:

            return call.answer(
                "Botones bloqueados."
            )

        # =====================================
        # VERIFICAR SESION
        # =====================================

        if user_id not in temp_mails:

            return call.answer(
                "❌ No tienes email."
            )

        headers = temp_mails[user_id]["headers"]

        # =====================================
        # OBTENER MENSAJES
        # =====================================

        response = requests.get(
            f"{BASE_URL}/messages",
            headers=headers
        )

        if response.status_code != 200:

            return call.message.reply(
                f"❌ Error obteniendo mensajes\n<code>{response.text}</code>"
            )

        data_json = response.json()

        if "hydra:member" not in data_json:

            return call.message.reply(
                "❌ Error leyendo correos."
            )

        messages = data_json["hydra:member"]

        # =====================================
        # NO HAY EMAILS
        # =====================================

        if len(messages) == 0:

            return call.answer(
                "📭 No hay correos."
            )

        # =====================================
        # MOSTRAR EMAILS
        # =====================================

        for msg in messages:

            message_id = msg["id"]

            full_response = requests.get(
                f"{BASE_URL}/messages/{message_id}",
                headers=headers
            )

            if full_response.status_code != 200:
                continue

            full_message = full_response.json()

            texto = f"""<b>

📩 EMAIL RECIBIDO

━━━━━━━━━━━━━━━

• DE:
<code>{msg['from']['address']}</code>

• ASUNTO:
<code>{msg['subject']}</code>

━━━━━━━━━━━━━━━

📨 MENSAJE:

<code>{full_message.get('text', 'Sin contenido')}</code>

</b>"""

            call.message.reply(texto)

    except Exception as e:

        print(e)

        call.message.reply(
            f"❌ ERROR\n<code>{e}</code>"
        )
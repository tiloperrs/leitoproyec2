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
# COMANDO /mail
# =========================================

@addCommand("mail")
def mail(_, m):

    try:

        # =========================
        # GENERAR USERNAME
        # =========================

        username = ''.join(
            random.choice(string.ascii_lowercase)
            for _ in range(10)
        )

        password = "Password123"

        # =========================
        # OBTENER DOMINIOS
        # =========================

        domains_response = requests.get(
            f"{BASE_URL}/domains"
        )

        # Verificar status
        if domains_response.status_code != 200:

            return m.reply(
                f"❌ Error API:\n<code>{domains_response.text}</code>"
            )

        data = domains_response.json()

        # Verificar respuesta
        if "hydra:member" not in data:

            return m.reply(
                "❌ Error obteniendo dominios."
            )

        domains = data["hydra:member"]

        # Verificar lista vacía
        if len(domains) == 0:

            return m.reply(
                "❌ No hay dominios disponibles."
            )

        # Obtener dominio
        domain = domains[0]["domain"]

        # Crear email
        email = f"{username}@{domain}"

        # =========================
        # CREAR CUENTA
        # =========================

        account_data = {
            "address": email,
            "password": password
        }

        create_response = requests.post(
            f"{BASE_URL}/accounts",
            json=account_data
        )

        # Verificar creación
        if create_response.status_code not in [200, 201]:

            return m.reply(
                f"❌ Error creando cuenta:\n<code>{create_response.text}</code>"
            )

        # =========================
        # LOGIN
        # =========================

        token_response = requests.post(
            f"{BASE_URL}/token",
            json=account_data
        )

        if token_response.status_code != 200:

            return m.reply(
                f"❌ Error login:\n<code>{token_response.text}</code>"
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

        # =========================
        # GUARDAR SESION
        # =========================

        temp_mails[m.from_user.id] = {
            "email": email,
            "headers": headers
        }

        # =========================
        # BOTONES
        # =========================

        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📩 Revisar Emails",
                        callback_data="check_mail"
                    )
                ]
            ]
        )

        # =========================
        # RESPUESTA
        # =========================

        text = f"""<b>

📧 EMAIL TEMPORAL GENERADO

━━━━━━━━━━━━━━━

• EMAIL:
<code>{email}</code>

━━━━━━━━━━━━━━━

📥 Usa el botón para revisar correos.

</b>"""

        m.reply(
            text,
            reply_markup=buttons
        )

    except Exception as e:

        m.reply(
            f"❌ ERROR:\n<code>{e}</code>"
        )


# =========================================
# CALLBACKS
# =========================================

@Client.on_callback_query()
def callbacks(_, query):

    try:

        if query.data == "check_mail":

            user_id = query.from_user.id

            # =========================
            # VERIFICAR EMAIL
            # =========================

            if user_id not in temp_mails:

                return query.message.reply(
                    "❌ No tienes email temporal."
                )

            headers = temp_mails[user_id]["headers"]

            # =========================
            # OBTENER MENSAJES
            # =========================

            response = requests.get(
                f"{BASE_URL}/messages",
                headers=headers
            )

            if response.status_code != 200:

                return query.message.reply(
                    f"❌ Error obteniendo mensajes:\n<code>{response.text}</code>"
                )

            data = response.json()

            if "hydra:member" not in data:

                return query.message.reply(
                    "❌ Error leyendo correos."
                )

            messages = data["hydra:member"]

            # =========================
            # SIN MENSAJES
            # =========================

            if len(messages) == 0:

                return query.message.reply(
                    "📭 No hay correos."
                )

            # =========================
            # MOSTRAR EMAILS
            # =========================

            for msg in messages:

                message_id = msg["id"]

                full_message_response = requests.get(
                    f"{BASE_URL}/messages/{message_id}",
                    headers=headers
                )

                if full_message_response.status_code != 200:
                    continue

                full_message = full_message_response.json()

                texto = f"""<b>

📩 NUEVO EMAIL

━━━━━━━━━━━━━━━

• DE:
<code>{msg['from']['address']}</code>

• ASUNTO:
<code>{msg['subject']}</code>

━━━━━━━━━━━━━━━

📨 MENSAJE:

<code>{full_message.get('text', 'Sin contenido')}</code>

</b>"""

                query.message.reply(texto)

    except Exception as e:

        query.message.reply(
            f"❌ ERROR:\n<code>{e}</code>"
        )
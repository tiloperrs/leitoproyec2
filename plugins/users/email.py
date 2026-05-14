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
        # GENERAR EMAIL
        # =========================

        username = ''.join(
            random.choice(string.ascii_lowercase)
            for _ in range(10)
        )

        password = "Password123"

        # =========================
        # DOMINIOS
        # =========================

        domains_response = requests.get(
            f"{BASE_URL}/domains"
        )

        domains = domains_response.json()["hydra:member"]

        domain = domains[0]["domain"]

        email = f"{username}@{domain}"

        # =========================
        # CREAR CUENTA
        # =========================

        account_data = {
            "address": email,
            "password": password
        }

        requests.post(
            f"{BASE_URL}/accounts",
            json=account_data
        )

        # =========================
        # LOGIN
        # =========================

        token_response = requests.post(
            f"{BASE_URL}/token",
            json=account_data
        )

        token = token_response.json()["token"]

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
        # BOTON
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

        text = f"""<b>

📧 EMAIL TEMPORAL

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
            f"<b>❌ ERROR:</b>\n<code>{e}</code>"
        )


# =========================================
# CALLBACK BOTON
# =========================================

@Client.on_callback_query()
def callbacks(_, query):

    try:

        if query.data == "check_mail":

            user_id = query.from_user.id

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

            messages = response.json()["hydra:member"]

            if not messages:

                return query.message.reply(
                    "📭 No hay correos."
                )

            # =========================
            # MOSTRAR EMAILS
            # =========================

            for msg in messages:

                message_id = msg["id"]

                full_message = requests.get(
                    f"{BASE_URL}/messages/{message_id}",
                    headers=headers
                ).json()

                texto = f"""<b>

📩 NUEVO EMAIL

━━━━━━━━━━━━━━━

• DE:
<code>{msg['from']['address']}</code>

• ASUNTO:
<code>{msg['subject']}</code>

━━━━━━━━━━━━━━━

📨 MENSAJE:

<code>{full_message['text']}</code>

</b>"""

                query.message.reply(texto)

    except Exception as e:

        query.message.reply(
            f"❌ ERROR:\n<code>{e}</code>"
        )
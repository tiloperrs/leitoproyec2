from pyrogram import filters, Client
import requests
import random
import string

from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from srca.configs import addCommand
from db.mongo_client import MongoDB


BASE_URL = "https://api.mail.tm"

temp_mails = {}


@addCommand('mail')
def start(_, message):

    querY = MongoDB().query_user(
        int(message.from_user.id)
    )

    if querY == None:
        return message.reply(
            'Usar el comando $register para el registro.'
        )

    if querY['role'] == 'baneado':
        return message.reply('User baneado')

    try:

        username = ''.join(
            random.choice(string.ascii_lowercase)
            for _ in range(10)
        )

        password = "Password123"

        # =====================================
        # DOMINIOS
        # =====================================

        domains_response = requests.get(
            f"{BASE_URL}/domains"
        )

        domains = domains_response.json()["hydra:member"]

        domain = domains[0]["domain"]

        # =====================================
        # EMAIL
        # =====================================

        email = f"{username}@{domain}"

        account_data = {
            "address": email,
            "password": password
        }

        # =====================================
        # CREAR CUENTA
        # =====================================

        requests.post(
            f"{BASE_URL}/accounts",
            json=account_data
        )

        # =====================================
        # LOGIN
        # =====================================

        token_response = requests.post(
            f"{BASE_URL}/token",
            json=account_data
        )

        token = token_response.json()["token"]

        headers = {
            "Authorization": f"Bearer {token}"
        }

        # =====================================
        # GUARDAR
        # =====================================

        temp_mails[message.from_user.id] = headers

        # =====================================
        # BOTON
        # =====================================

        re_gen = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "📩 Revisar Emails",
                    callback_data=f"mail:{message.from_user.id}"
                )
            ]
        ])

        texto = f'''<b>

📧 EMAIL TEMPORAL

━━━━━━━━━━━━━━━━━━

• EMAIL:
<code>{email}</code>

━━━━━━━━━━━━━━━━━━

by: @{message.from_user.username}

</b>'''

        message.reply(
            texto,
            reply_markup=re_gen
        )

    except Exception as e:

        message.reply(
            f'<b>❌ ERROR\n<code>{e}</code></b>'
        )
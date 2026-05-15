from pyrogram import filters, Client
import requests
import re

from plugins.tools.email import (
    temp_mails,
    BASE_URL
)


@Client.on_callback_query(filters.regex("^mail"))
def exit(client, message):

    try:

        # =====================================
        # VALIDAR BOTON
        # =====================================

        if ":" in message.data:

            user_id = int(
                message.data.split(":")[1]
            )

            if message.from_user.id != user_id:

                return message.answer(
                    "❌ No es tu botón",
                    show_alert=True
                )

        # =====================================
        # EMAIL GUARDADO
        # =====================================

        if user_id not in temp_mails:

            return message.answer(
                "❌ No tienes email.",
                show_alert=True
            )

        headers = temp_mails[user_id]

        # =====================================
        # MENSAJES
        # =====================================

        response = requests.get(
            f"{BASE_URL}/messages",
            headers=headers
        )

        messages = response.json()["hydra:member"]

        # =====================================
        # NO HAY EMAILS
        # =====================================

        if len(messages) == 0:

            return message.answer(
                "📭 No hay correos.",
                show_alert=True
            )

        # =====================================
        # MOSTRAR EMAILS
        # =====================================

        for msg in messages:

            message_id = msg["id"]

            full_message = requests.get(
                f"{BASE_URL}/messages/{message_id}",
                headers=headers
            ).json()

            # =====================================
            # CONTENIDO
            # =====================================

            contenido = full_message.get(
                'text',
                'Sin contenido'
            )

            # =====================================
            # LIMPIAR LINKS
            # =====================================

            contenido = re.sub(
                r'https?://\S+',
                '',
                contenido
            )

            # =====================================
            # LIMPIAR TRACKING
            # =====================================

            contenido = re.sub(
                r'\[.*?\]',
                '',
                contenido
            )

            # =====================================
            # LIMPIAR ESPACIOS
            # =====================================

            contenido = re.sub(
                r'\n{3,}',
                '\n\n',
                contenido
            )

            contenido = contenido.strip()

            # =====================================
            # EXTRAER OTP
            # =====================================

            otp = re.findall(
                r'\b\d{4,8}\b',
                contenido
            )

            otp_code = (
                otp[0]
                if otp else "No encontrado"
            )

            # =====================================
            # TEXTO BONITO
            # =====================================

            texto = f'''<b>

📩 EMAIL RECIBIDO

━━━━━━━━━━━━━━━━━━

• DE:
<code>{msg['from']['address']}</code>

• ASUNTO:
<code>{msg['subject']}</code>

━━━━━━━━━━━━━━━━━━

🔑 OTP:
<code>{otp_code}</code>

━━━━━━━━━━━━━━━━━━

📨 MENSAJE:

<code>{contenido[:700]}</code>

</b>'''

            message.message.reply(
                texto
            )

    except Exception as e:

        message.message.reply(
            f'<b>❌ ERROR\n<code>{e}</code></b>'
        )
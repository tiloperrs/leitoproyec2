from pyrogram import filters, Client
import requests

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

            texto = f'''<b>

📩 EMAIL RECIBIDO

━━━━━━━━━━━━━━━━━━

• DE:
<code>{msg['from']['address']}</code>

• ASUNTO:
<code>{msg['subject']}</code>

━━━━━━━━━━━━━━━━━━

📨 MENSAJE:

<code>{full_message.get('text', 'Sin contenido')}</code>

</b>'''

            message.message.reply(
                texto
            )

    except Exception as e:

        message.message.reply(
            f'<b>❌ ERROR\n<code>{e}</code></b>'
        )
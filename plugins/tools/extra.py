from pyrogram import Client, filters
from db.mongo_client import MongoDB
import random
import requests
import time

@Client.on_message(filters.command("extra", prefixes=["/", ".", "$", "!", "%", "#"], case_sensitive=False) & filters.text)
def extra(_, message):

    inicio = time.perf_counter()

    # Verificar grupo
    if MongoDB().query_group(message.chat.id) == None:
        return message.reply("Chat not Authorized.")

    # Verificar usuario
    user = MongoDB().query_user(int(message.from_user.id))

    if user == None:
        return message.reply("Usar el comando $register para el registro.")

    if user['role'] == "baneado":
        return message.reply("User baneado")


    try:
        args = message.text.split(None, 1)

        if len(args) != 2:
            return message.reply(
                "<b>⚠️ Uso correcto:\n/extra <code>BIN</code></b>"
            )


        BIN = args[1][:6]

        if len(BIN) < 6:
            return message.reply(
                "<b>BIN invalido, ingresa 6 digitos.</b>"
            )


        req = requests.get(
            f"https://bins.antipublic.cc/bins/{BIN}"
        )


        if req.status_code != 200:
            return message.reply("<b>BIN no encontrado.</b>")


        data = req.json()


        brand = data.get("brand","N/A")
        country = data.get("country_name","N/A")
        flag = data.get("country_flag","")
        bank = data.get("bank","N/A")
        level = data.get("level","N/A")
        type_card = data.get("type","N/A")


        extras = []

        for i in range(28):

            numbers = "".join(
                random.choice("0123456789")
                for _ in range(6)
            )

            month = random.randint(1,12)
            year = random.randint(2026,2030)

            extras.append(
                f"<code>{BIN}{numbers}xxxx|{month:02d}|{year}</code>"
            )


        lista = "\n".join(
            [
                f"<b>✯</b> {x}"
                for x in extras
            ]
        )


        tiempo = time.perf_counter() - inicio


        texto = f"""
<b>EXTRA GENERATOR

{lista}

━━━━━━━━━━━━━━━━━━
BIN INFO:

Pais: {country} {flag}
Banco: {bank}
Data: {brand} - {level} - {type_card}

━━━━━━━━━━━━━━━━━━
TIME: {tiempo:.2f}s
USER: @{message.from_user.username}
</b>
"""


        message.reply(
            texto,
            disable_web_page_preview=True
        )


    except Exception as e:
        print(e)
        message.reply(
            "<b>Entrada invalida.</b>"
        )
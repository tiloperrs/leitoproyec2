from pyrogram import Client, filters
from pymongo import MongoClient

mongo = MongoClient("TU_MONGO_URI")
db = mongo["TU_DATABASE"]
users = db["users"]


@Client.on_message(filters.command("global", prefixes="."))
async def global_message(client, message):

    partes = message.text.split(" ", 1)
    texto = partes[1] if len(partes) > 1 else ""

    if not texto and not message.reply_to_message:
        await message.reply("❌ Escribe un mensaje o responde a una foto.")
        return

    enviados = 0
    errores = 0

    for usuario in users.find({}):

        user_id = usuario["user_id"]

        try:

            # GLOBAL CON FOTO
            if message.reply_to_message and message.reply_to_message.photo:

                await client.send_photo(
                    chat_id=user_id,
                    photo=message.reply_to_message.photo.file_id,
                    caption=texto
                )

            # GLOBAL SOLO TEXTO
            else:

                await client.send_message(
                    chat_id=user_id,
                    text=texto
                )

            enviados += 1

        except Exception as e:
            print(f"Error {user_id}: {e}")
            errores += 1

    await message.reply(
        f"✅ GLOBAL TERMINADO\n\n"
        f"📨 Enviados: {enviados}\n"
        f"❌ Errores: {errores}"
    )
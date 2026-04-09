from pyrogram import Client, filters
from paquetes.plantillas import atrasgt
from paquetes.plantillas import tipogt
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from db.mongo_client import MongoDB

@Client.on_callback_query(filters.regex("auth"))
def gates_coman(client, message):
    try:
        querY = MongoDB().query_user(int(message.from_user.id))
        
        message.edit_message_text(
            "AUTH FUNCIONANDO",
            reply_markup=atrasgt(message.from_user.id)
        )
    except Exception as e:
        print("ERROR AUTH:", e)
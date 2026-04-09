from pyrogram import Client, filters
from paquetes.plantillas import atrasgt
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from db.mongo_client import MongoDB

@Client.on_callback_query(filters.regex("charged"))
def gates_coman(client, message):
    querY = MongoDB().query_user(int(message.from_user.id))
    message.edit_message_text('''
<b>𝐆𝐚𝐭𝐞𝐫𝐰𝐚𝐲𝐬 𝐜𝐡𝐚𝐫𝐠𝐞𝐝 🍫

</b>''',reply_markup=atrasgt(message.from_user.id))
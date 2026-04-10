from pyrogram import Client, filters
from paquetes.plantillas import atrasgt
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from db.mongo_client import MongoDB



@Client.on_callback_query(filters.regex("masst"))
def gates_coman(client, m):
    print("CLICK MASS")
    # querY = MongoDB().query_user(int(message.from_user.id))
    m.edit_message_text('''<b> 
payflow avs Charged /mass 
Type   Payflow avs
Format  $flw cc|mm|yy|cvc
status   on 

payflow Charged  /mass2 
Type   Payflow Charged
Format  $flw cc|mm|yy|cvc
status   on 
</b>''',reply_markup=atrasgt(m.from_user.id))
from pyrogram import Client, filters
from paquetes.plantillas import atrasgt
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from db.mongo_client import MongoDB



@Client.on_callback_query(filters.regex("masst"))
def gates_coman(client, m):
    querY = MongoDB().query_user(int(m.from_user.id))
    m.edit_message_text('''
<b> 🍒
━━━━━━━━━━━━━━━━
ºpayflow avs Charged ( /mass )
ºType  - Payflow avs
ºFormat - $flw cc|mm|yy|cvc
ºstatus - (✅ on )
━━━━━━━━━━━━━━━━
ºpayflow Charged ( /mass2 )
ºType  - Payflow Charged
ºFormat - $flw cc|mm|yy|cvc
ºstatus - (✅ on )
━━━━━━━━━━━━━━━━</b>''',reply_markup=atrasgt(m.from_user.id))
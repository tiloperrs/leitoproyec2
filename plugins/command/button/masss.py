from pyrogram import Client, filters
from paquetes.plantillas import atrasgt
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from db.mongo_client import MongoDB

@Client.on_callback_query(filters.regex("gtmass"))
def gates_coman(client, m):
    print("CLICK CHARGED")
    # querY = MongoDB().query_user(int(message.from_user.id))
    m.edit_message_text('''
<b>𝐆𝐚𝐭𝐞𝐫𝐰𝐚𝐲𝐬 mass 🍫
━━━━━━━━━━━━━━━━
Payflow avs Charged ( /mass) 
♅ºType   Payflow avs
♅ºFormat  $mass cc|mm|yy|cvc
♅ºstatus   (on ✅)
━━━━━━━━━━━━━━━━
Stripe auth ( /stmas)
♅ºType   Stripe auth
♅ºFormat  $stmas cc|mm|yy|cvc
♅ºstatus   (on ✅)
━━━━━━━━━━━━━━━━
Braintree auth ( /btmas)
♅ºType   Braintree auth
♅ºFormat  $btmas cc|mm|yy|cvc
♅ºstatus   (on ✅)
━━━━━━━━━━━━━━━━
</b>''',reply_markup=atrasgt(m.from_user.id))
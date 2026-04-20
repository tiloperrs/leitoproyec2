from pyrogram import Client, filters
from paquetes.plantillas import atrasgt
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from db.mongo_client import MongoDB

@Client.on_callback_query(filters.regex("charged"))
def gates_coman(client, m):
    print("CLICK CHARGED")
    # querY = MongoDB().query_user(int(message.from_user.id))
    m.edit_message_text('''
<b>𝐆𝐚𝐭𝐞𝐫𝐰𝐚𝐲𝐬 𝐜𝐡𝐚𝐫𝐠𝐞𝐝 🍫
━━━━━━━━━━━━━━━━
Payflow Charged ( /pfw) 
♅ºType   Payflow charged
♅ºFormat  $pfw cc|mm|yy|cvc
♅ºstatus   (on ✅)
━━━━━━━━━━━━━━━━
Braintree 5.79 ( /btc) 
♅ºType   Braintree 5.79
♅ºFormat  $pfw cc|mm|yy|cvc
♅ºstatus   (on ✅)
━━━━━━━━━━━━━━━━
paypal 0.7 ( /pp) 
♅ºType   paypal 0.7
♅ºFormat  $pp cc|mm|yy|cvc
♅ºstatus   (on ✅)
━━━━━━━━━━━━━━━━
</b>''',reply_markup=atrasgt(m.from_user.id))
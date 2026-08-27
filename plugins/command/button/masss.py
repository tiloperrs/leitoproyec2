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
Stripe Charged 15$( /stmas15) 
♅ºType   Stripe Charged
♅ºFormat  $mass15 cc|mm|yy|cvc
♅ºstatus   (on ✅)
━━━━━━━━━━━━━━━━
Stripe auth ( /stmas)
♅ºType   Stripe auth
♅ºFormat  $stmas cc|mm|yy|cvc
♅ºstatus   (on ✅)
━━━━━━━━━━━━━━━━
Payflow Charged 10.58( /mass2) 
♅ºType   Payflow 
♅ºFormat  $mass2 cc|mm|yy|cvc
♅ºstatus   (on ✅)
━━━━━━━━━━━━━━━━
Stripe auth ( /stmas1)
♅ºType   Stripe auth
♅ºFormat  $stmas1 cc|mm|yy|cvc
♅ºstatus   (on ✅)
━━━━━━━━━━━━━━━━
</b>''',reply_markup=atrasgt(m.from_user.id))
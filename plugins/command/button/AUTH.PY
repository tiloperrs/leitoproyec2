from pyrogram import Client, filters
from paquetes.plantillas import atrasgt
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup




@Client.on_callback_query(filters.regex("auth"))
def gates_coman(client, message):
    message.edit_message_text('''
<b>𝐆𝐚𝐭𝐞𝐫𝐰𝐚𝐲𝐬 𝐚𝐮𝐭𝐡 🍀
━━━━━━━━━━━━━━━━
♅ºStripe Auth ( /au )
♅ºType  - Stripe Auth
♅ºFormat  - $flw cc|mm|yy|cvc
♅ºstatus - (✅ on )
━━━━━━━━━━━━━━━━
♅ºStripe Auth ( /ar )
♅ºType  - Stripe Auth
♅ºFormat - $flw cc|mm|yy|cvc
♅ºstatus - (✅ on )
━━━━━━━━━━━━━━━━
♅ºStripe Auth ( /sb )
♅º Type  - Stripe Auth
♅ºFormat - $flw cc|mm|yy|cvc
♅ºstatus - (✅ on )
━━━━━━━━━━━━━━━━
''',reply_markup=atrasgt(message.from_user.id))
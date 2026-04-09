from pyrogram import Client, filters
from paquetes.plantillas import atrasgt
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup




@Client.on_callback_query(filters.regex("masst"))
def gates_coman(client, message):
    message.edit_message_text('''
<b>𝐆𝐚𝐭𝐞𝐫𝐰𝐚𝐲𝐬 𝐌𝐚𝐬𝐬 🍒
━━━━━━━━━━━━━━━━
♅ºpayflow avs Charged ( /mass )
♅ºType  - Payflow avs
♅ºFormat - $flw cc|mm|yy|cvc
♅ºstatus - (✅ on )
━━━━━━━━━━━━━━━━
♅ºpayflow Charged ( /mass2 )
♅ºType  - Payflow Charged
♅ºFormat - $flw cc|mm|yy|cvc
♅ºstatus - (✅ on )
━━━━━━━━━━━━━━━━
''',reply_markup=atrasgt(message.from_user.id))
from pyrogram import Client, filters
from paquetes.plantillas import atrasgt

@Client.on_callback_query(filters.regex(r"^auth"))
def gates_coman(client, message):
    print("CLICK AUTH")

    try:
        message.edit_message_text(
            '''<b>𝐆𝐚𝐭𝐞𝐫𝐰𝐚𝐲𝐬 𝐚𝐮𝐭𝐡 

♅ºStripe Auth ( /au )
♅ºType  - Stripe Auth
♅ºFormat  - $flw cc|mm|yy|cvc
♅ºstatus - ( on )

♅ºStripe Auth ( /ar )
♅ºType  - Stripe Auth
♅ºFormat - $flw cc|mm|yy|cvc
♅ºstatus - ( on )

♅ºStripe Auth ( /sb )
♅º Type  - Stripe Auth
♅ºFormat - $flw cc|mm|yy|cvc
♅ºstatus - ( on )
</b>''',
            reply_markup=atrasgt(message.from_user.id)
        )
    except Exception as e:
        print("ERROR AUTH:", e)
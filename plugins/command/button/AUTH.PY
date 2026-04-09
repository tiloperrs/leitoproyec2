from pyrogram import Client, filters
from paquetes.plantillas import atrasgt

@Client.on_callback_query()
def gates_coman(client, m):
    
    # 🔥 Detectar cualquier botón que contenga "auth" o "mass"
    data = str(m.data).lower()

    if "auth" in data or "mass" in data:
        m.edit_message_text(
            """<b>𝐆𝐚𝐭𝐞𝐫𝐰𝐚𝐲𝐬 𝐚𝐮𝐭𝐡 

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
</b>""",
            parse_mode="html",
            reply_markup=atrasgt(m.from_user.id)
        )
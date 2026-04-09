from pyrogram import Client, filters
from paquetes.plantillas import tipogt








@Client.on_callback_query(filters.regex("gates"))
def gates_coman(client, message):
    message.edit_message_text('''<b>
𝐁𝐢𝐞𝐧𝐯𝐞𝐧𝐢𝐝𝐨 𝐍𝐮𝐞𝐬𝐭𝐫𝐚 𝐙𝐨𝐧𝐚 𝐝𝐞 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬 ♛
━━━━━━━━━━━━━━━━
⨳ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬 𝐚𝐜𝐭𝐢𝐯𝐨𝐬 (5) ✅
⨳ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬 𝐝𝐞𝐜𝐥𝐢𝐧𝐞𝐝 (0) ❌
━━━━━━━━━━━━━━━━
''',reply_markup=tipogt(message.from_user.id))
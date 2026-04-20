from pyrogram import Client, filters
from paquetes.plantillas import tipogt
from db.mongo_client import MongoDB

@Client.on_callback_query(filters.regex("gates"))
def gates_coman(client, m):
    querY = MongoDB().query_user(int(m.from_user.id))
    m.edit_message_text('''<b>
𝐁𝐢𝐞𝐧𝐯𝐞𝐧𝐢𝐝𝐨 𝐍𝐮𝐞𝐬𝐭𝐫𝐚 𝐙𝐨𝐧𝐚 𝐝𝐞 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬 ♛
━━━━━━━━━━━━━━━━
⨳ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬 𝐚𝐜𝐭𝐢𝐯𝐨𝐬 (9) ✅
⨳ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬 𝐝𝐞𝐜𝐥𝐢𝐧𝐞𝐝 (0) ❌
━━━━━━━━━━━━━━━━
</b>''',reply_markup=tipogt(m.from_user.id))
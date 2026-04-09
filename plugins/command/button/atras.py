from pyrogram import Client, filters
from paquetes.plantillas import commd
from db.mongo_client import MongoDB

@Client.on_callback_query(filters.regex("atras"))
def atras(client, message):
    querY = MongoDB().query_user(int(message.from_user.id))
    message.edit_message_text(
f'''<b>𝐁𝐢𝐞𝐧𝐯𝐞𝐧𝐢𝐝𝐨 @{message.from_user.username} 𝐚 𝐊𝐢𝐲𝐨𝐭𝐚𝐤𝐚_𝐜𝐦𝐝𝐬 👑
━━━━━━━━━━━━━━━━
𝐄𝐬𝐩𝐞𝐫𝐨 𝐐𝐮𝐞 𝐄𝐧 𝐋𝐨𝐬 𝐒𝐢𝐠𝐮𝐢𝐞𝐧𝐭𝐞𝐬 𝐁𝐨𝐭𝐨𝐧𝐞𝐬 
𝐄𝐧𝐜𝐮𝐞𝐧𝐭𝐫𝐞𝐬 𝐥𝐨 𝐪𝐮𝐞 𝐞𝐬𝐭𝐚𝐬 𝐛𝐮𝐬𝐜𝐚𝐧𝐝𝐨 🎩
━━━━━━━━━━━━━━━━
𝐚𝐭𝐭:@Leito_nex 🎭</b>'''
,reply_markup=commd(message.from_user.id))
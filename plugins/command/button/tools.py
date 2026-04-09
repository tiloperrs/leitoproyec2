from pyrogram import Client, filters
from paquetes.plantillas import atras

@Client.on_callback_query(filters.regex("tools"))
def tool_com(client, m):
    m.edit_message_text('''
<b>𝐁𝐢𝐞𝐧𝐯𝐞𝐧𝐢𝐝𝐨 𝐚 𝐥𝐚𝐬 𝐓𝐨𝐥𝐥𝐬 ⚒
━━━━━━━━━━━━━━━━
𝐄𝐬𝐩𝐞𝐫𝐨 𝐪𝐮𝐞 𝐞𝐬𝐭𝐚𝐬 𝐭𝐨𝐨𝐥𝐬 𝐬𝐞𝐚𝐧 𝐝𝐞 𝐭𝐮 𝐚𝐠𝐫𝐚𝐝𝐨 🚀
━━━━━━━━━━━━━━━━                       
º𝐛𝐢𝐧: ( /𝐛𝐢𝐧 𝟏𝟐𝟑𝟒𝟓𝟔 )
º𝐒𝐭𝐚𝐭𝐮𝐬:𝐨𝐧𝐥𝐢𝐧𝐞! ✅
━━━━━━━━━━━━━━━━ 
º𝐆𝐞𝐧: ( /𝐠𝐞𝐧 𝟏𝟐𝟑𝟒𝟓𝟔 )
º𝐒𝐭𝐚𝐭𝐮𝐬:𝐨𝐧𝐥𝐢𝐧𝐞! ✅  
━━━━━━━━━━━━━━━━                             
º𝐑𝐚𝐧𝐝𝐨𝐦: ( /𝐫𝐧𝐝 𝐮𝐬) 
º𝐒𝐭𝐚𝐭𝐮𝐬:𝐨𝐧𝐥𝐢𝐧𝐞! ✅ 
━━━━━━━━━━━━━━━━                  
</b>''',reply_markup=atras(m.from_user.id))

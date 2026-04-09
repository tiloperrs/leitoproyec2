from srca.configs import addCommand,Client
from paquetes.plantillas import commd
from db.mongo_client import MongoDB

@addCommand('cmds')
def start(_,m):
    querY = MongoDB().query_user(int(m.from_user.id))
        
    if  querY == None: return m.reply('Usar el comando $register para el registro.')

    if  querY['role'] == 'baneado': return m.reply('User baneado')

    Client.send_photo(_,chat_id=m.chat.id,photo='https://i.pinimg.com/736x/78/25/cb/7825cb086c485705edfafceca9c875a5.jpg',
caption=f'''<b>𝐁𝐢𝐞𝐧𝐯𝐞𝐧𝐢𝐝𝐨 @{m.from_user.username} 𝐚 𝐊𝐢𝐲𝐨𝐭𝐚𝐤𝐚_𝐜𝐦𝐝𝐬 👑
━━━━━━━━━━━━━━━━
𝐄𝐬𝐩𝐞𝐫𝐨 𝐐𝐮𝐞 𝐄𝐧 𝐋𝐨𝐬 𝐒𝐢𝐠𝐮𝐢𝐞𝐧𝐭𝐞𝐬 𝐁𝐨𝐭𝐨𝐧𝐞𝐬 
𝐄𝐧𝐜𝐮𝐞𝐧𝐭𝐫𝐞𝐬 𝐥𝐨 𝐪𝐮𝐞 𝐞𝐬𝐭𝐚𝐬 𝐛𝐮𝐬𝐜𝐚𝐧𝐝𝐨 🎩
━━━━━━━━━━━━━━━━
𝐚𝐭𝐭:@Leito_nex 🎭</b>'''
,reply_markup = commd(m.from_user.id))
    
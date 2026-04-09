
from srca.configs import find_cards,antispam
from gates.stripe3 import stripe3
import time 
from db.mongo_client import MongoDB
from srca.configs import addCommand

from func_bin import get_bin_info

@addCommand('ar')
def mc(client, m):
    if MongoDB().query_group(m.chat.id) == None: return m.reply('Chat not Authorized.')
    querY = MongoDB().query_user(int(m.from_user.id))
    if  querY == None: return m.reply('Usar el comando $register para el registro.')
    if  querY['role'] == 'baneado': return m.reply('User baneado')
    if  querY['plan'] == 'free': return m.reply('User Fre , adquiera el plan https://t.me/Leito1324')
    inicio = time.time()
    if antispam(querY['antispam'],m):return
    
    
    if m.reply_to_message:ccs = find_cards(m.reply_to_message.text)
    else: ccs = find_cards(m.text)
    if not m.reply_to_message and len(m.text.split()) == 1:
        return m.reply("""
𝐬𝐭𝐫𝐢𝐩𝐞 𝐚𝐮𝐭𝐡 ⚔
━━━━━━━━━━━━━━━━ 
➢º𝐠𝐚𝐭𝐞𝐰𝐚𝐲𝐬:𝐚𝐜𝐭𝐢𝐯𝐨 ✅
➢º𝐔𝐬𝐨 𝐜𝐨𝐫𝐫𝐞𝐜𝐭𝐨:/𝐚𝐮 𝐜𝐜|𝐦𝐦|𝐲𝐲|𝐜𝐯𝐯
━━━━━━━━━━━━━━━━ 
𝐮𝐬𝐞𝐫:𝐩𝐫𝐞𝐦𝐢𝐮𝐦 👀
""")

    cc_com = '{}|{}|{}|{}'.format(ccs[0], ccs[1], ccs[2], ccs[3])
    
    x = get_bin_info(cc_com[:6])

    new = m.reply(f'''
⚜ 𝐒𝐭𝐫𝐢𝐩𝐞 𝐀𝐮𝐭𝐡 ⚜  
━━━━━━━━━━━━━━━━           
♅º𝐂𝐚𝐫𝐝: {𝐜𝐜_𝐜𝐨𝐦} 🚀
♅º𝐒𝐭𝐚𝐭𝐮𝐬: 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠... ❄️ 
♅º𝐔𝐬𝐞𝐫: {𝐦.𝐟𝐫𝐨𝐦_𝐮𝐬𝐞𝐫.𝐟𝐢𝐫𝐬𝐭_𝐧𝐚𝐦𝐞}
━━━━━━━━━━━━━━━━
♅º𝐃𝐮𝐞ñ𝐨: @𝐥𝐞𝐢𝐭𝐨𝟏𝟑𝟐𝟒''')
    
    chk = stripe3(cc_com).main()

    fin = time.time()
    texto = f'''
𝐒𝐭𝐫𝐢𝐩𝐞 𝐀𝐮𝐭𝐡
━━━━━━━━━━━━━━━━  
↬º𝐂𝐜: <code>{cc_com}</code>
↬º𝐒𝐭𝐚𝐭𝐮𝐬: {chk[0]}
↬º𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{chk[1]}</code>
━━━━━━━━━━━━━━━━  
↬º𝐁𝐈𝐍 = <code>{x.get("type")}</code> | <code>{x.get("level")}</code> | <code>{x.get("vendor")}</code>
↬º𝐂𝐎𝐔𝐍𝐓𝐘 = <code>{x.get("country")} {x.get("flag")}</code>
↬º𝐁𝐀𝐍𝐊 = <code>{x.get("bank_name")}</code>
━━━━━━━━━━━━━━━━  
↬º𝐏𝐱𝐬: 𝐋𝐢𝐯𝐞 ✅
↬º𝐓𝐢𝐦𝐞: <code>{fin-inicio:0.4f}'s</code>
↬º𝐅𝐫𝐨𝐦: {m.from_user.first_name}'''
    new.edit_text(texto)
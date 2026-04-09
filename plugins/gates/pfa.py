from srca.configs import find_cards,antispam
from gates.avspfw import avspfw1
import time 
from db.mongo_client import MongoDB
from srca.configs import addCommand

from func_bin import get_bin_info

@addCommand('pfa')
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
    cc_com = '{}|{}|{}|{}'.format(ccs[0], ccs[1], ccs[2], ccs[3])
    
    x = get_bin_info(cc_com[:6])

    new = m.reply(f'''<b>あ Stripe Auth

• Cc: <code>{cc_com}</code>      
• Status: Processing... [ ☃️ ]
• From: {m.from_user.first_name}</b>''')
    
    chk = avspfw1(cc_com).main()

    fin = time.time()
    texto = f'''<b>あPayflow avs 

• Cc: <code>{cc_com}</code>
• Status: {chk[0]}
• Response: <code>{chk[1]}</code>

BIN = <code>{x.get("type")}</code> | <code>{x.get("level")}</code> | <code>{x.get("vendor")}</code>
COUNTY = <code>{x.get("country")} {x.get("flag")}</code>
BANK = <code>{x.get("bank_name")}</code>

• Pxs: Live ✅
• Time: <code>{fin-inicio:0.4f}'s</code>
• From: {m.from_user.first_name}</b>'''
    new.edit_text(texto)
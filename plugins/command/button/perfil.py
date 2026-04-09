from pyrogram import Client, filters
from paquetes.plantillas import atras
from db.mongo_client import MongoDB
import datetime

@Client.on_callback_query(filters.regex("perfi"))
def perfil_cmon(client, m):
    try:
        perfil_text = '''
𝐏𝐞𝐫𝐟𝐢𝐥 𝐮𝐬𝐞𝐫 🎭
━━━━━━━━♜━━━━━━━━
☫|𝐢𝐝: {}
☫|𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: @{}
☫|𝐍𝐚𝐦𝐞: {}
☫|𝐂𝐫𝐞𝐝𝐢𝐭𝐨𝐬: {}
☫|𝐑𝐚𝐧𝐠𝐨: {}
☫|𝐏𝐥𝐚𝐧: {}
☫|𝐀𝐧𝐭𝐢𝐬𝐩𝐚𝐦: {}
━━━━━━━━♜━━━━━━━━


'''
        querY = MongoDB().query_user(int(m.from_user.id))
        m.edit_message_text(perfil_text.format(m.from_user.id,m.from_user.username,m.from_user.first_name,querY['credits'],querY['role'],querY['plan'],querY['antispam']),reply_markup=atras(m.from_user.id))
    
    except:pass
from srca.configs import addCommand,Client
from paquetes.plantillas import commd
from db.mongo_client import MongoDB

@addCommand('start')
def start(_,m):
    querY = MongoDB().query_user(int(m.from_user.id))

    if  querY == None: 
        return m.reply('Usar el comando $register para el registro.')
        
    if  querY == None: return m.reply('Usar el comando $register para el registro.')
    Client.send_photo(_,chat_id=m.chat.id,photo='https://i.pinimg.com/736x/78/25/cb/7825cb086c485705edfafceca9c875a5.jpg',caption='<i><b>Bienvenidos a Kiyotaka_chk</b>.</i>',reply_markup = commd(m.from_user.id))
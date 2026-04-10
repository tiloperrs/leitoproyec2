   
from pyrogram import Client
from pyrogram.types import CallbackQuery
import logging , os 
import plugins.command.button.auth
import plugins.command.button.mass

class Kiyotaka_chk():
    def __init__(self):
        self.app = Client(
            "Kiyotakac_bot",
            api_id    =  33276466,#API ID de Telegram App
            api_hash  = '6045dd5caa167e3e60a0c9a52ca9a0a2',#API Hash de Telegram app
            bot_token = '8684644836:AAEhLqpG4eUjaDoQkswKfX0iAvKhJcZ0wrY',#Token bot Telegram
            plugins   =  dict(root="plugins"))

        @self.app.on_callback_query()
        def clod(client, call: CallbackQuery):
            data = call.data.split(":")

            if call.from_user.id != int(data[1]):return call.answer("Botones bloqueados.")
            else: call.continue_propagation()

    def runn(self):
        os.system("cls")
        logging.basicConfig(level=logging.INFO)
        self.app.run()

Kiyotaka_chk().runn()


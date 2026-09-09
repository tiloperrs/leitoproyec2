import time
from pymongo import MongoClient
from pyrogram.errors import UserIsBlocked, PeerIdInvalid, InputUserDeactivated
from srca.configs import addCommand


class MongoDB:
    def __init__(self):
        self.db = MongoClient(
            "mongodb://mongo:YwXhiAfhbViTETrnPgzuQllDfDuvNhBY@maglev.proxy.rlwy.net:34166"
        )["bot"]
        self.users = self.db["user"]
        self.sent = self.db["sent_messages"]

    def is_owner(self, uid):
        u = self.users.find_one({"id": uid})
        return u and u.get("role") == "owner"

    def user_ids(self):
        return [u["id"] for u in self.users.find({}, {"id": 1})]


def extract_payload(msg):
    text = msg.text or msg.caption
    if not text:
        return None
    parts = text.split(maxsplit=1)
    return parts[1] if len(parts) > 1 else None


@addCommand("all")
def broadcast(bot, msg):
    mongo = MongoDB()

    if not mongo.is_owner(msg.from_user.id):
        return msg.reply("🚫 No autorizado")

    payload = extract_payload(msg)
    reply = msg.reply_to_message

    if not reply and not (payload or msg.photo or msg.video or msg.audio):
        return msg.reply("⚠️ Responde a un mensaje o escribe algo después del comando")

    ok = err = 0

    for uid in mongo.user_ids():
        try:
            if reply:
                sent = bot.copy_message(uid, msg.chat.id, reply.id)
            elif msg.photo:
                sent = bot.send_photo(uid, msg.photo.file_id, caption=payload)
            elif msg.video:
                sent = bot.send_video(uid, msg.video.file_id, caption=payload)
            elif msg.audio:
                sent = bot.send_audio(uid, msg.audio.file_id, caption=payload)
            else:
                sent = bot.send_message(uid, payload)

            mongo.sent.insert_one({"chat_id": uid, "message_id": sent.id})
            ok += 1
            time.sleep(0.7)

        except (UserIsBlocked, PeerIdInvalid, InputUserDeactivated):
            mongo.users.delete_one({"id": uid})
            err += 1

        except Exception as e:
            err += 1
            print(f"{uid}: {e}")
            time.sleep(1)

    msg.reply(f"✅ Enviado: {ok}\n❌ Errores: {err}")


@addCommand("rall")
def remove_broadcast(bot, msg):
    mongo = MongoDB()

    if not mongo.is_owner(msg.from_user.id):
        return msg.reply("🚫 No autorizado")

    ok = err = 0

    for m in mongo.sent.find():
        try:
            bot.delete_messages(m["chat_id"], m["message_id"])
            ok += 1
            time.sleep(0.4)
        except Exception:
            err += 1

    mongo.sent.delete_many({})
    msg.reply(f"🗑 Eliminados: {ok}\n❌ Errores: {err}")

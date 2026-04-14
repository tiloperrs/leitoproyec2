from srca.configs import find_cards, antispam, addCommand
from gates.b3auth import brainrrrt
from db.mongo_client import MongoDB
import time, requests

@addCommand("btmas")
def mass_cmd(client, m):

    if MongoDB().query_group(m.chat.id) is None:
        return m.reply("Chat not Authorized.")

    user = MongoDB().query_user(int(m.from_user.id))
    if not user:
        return m.reply("Usar el comando $register.")
    if user["role"] == "baneado":
        return m.reply("User baneado.")
    if user["credits"] < 1:
        return m.reply("Créditos insuficientes.")
    if user["plan"] == "free":
        return m.reply("User Free.")
    if antispam(user["antispam"], m):
        return

    texto = m.text.replace("/mass", "").strip()
    if m.reply_to_message:
        texto += "\n" + m.reply_to_message.text

    tarjetas = []
    for l in texto.splitlines():
        ccs = find_cards(l)
        if ccs and len(ccs) == 4:
            tarjetas.append(ccs)
        if len(tarjetas) == 10:
            break

    if not tarjetas:
        return m.reply("<b>braintree auth mass\nFormat: /mass x10</b>")

    inicio = time.time()
    gate = "braintree auth mass"
    msg = m.reply(f"<b>{gate}</b>\nProcesando {len(tarjetas)} tarjetas...")

    resultados, total_deduct = [], 0
    bin_cache = {}

    for i, ccs in enumerate(tarjetas, start=1):
        cc = "|".join(ccs)

        msg.edit_text(f"""<b>{gate}</b>

• Card: <code>{cc}</code>
• Status: Checking [{i}/{len(tarjetas)}]
• From: {m.from_user.first_name}
""")

        bin6 = ccs[0][:6]
        if bin6 not in bin_cache:
            try:
                bin_cache[bin6] = requests.get(
                    f"https://bins.antipublic.cc/bins/{bin6}", timeout=4
                ).json()
            except:
                bin_cache[bin6] = {}

        bin_data = bin_cache[bin6]
        country = f"{bin_data.get('country_name','')} {bin_data.get('country_flag','')}"

        chk = brainrrrt().main(cc)
        cr = 4 if "approved" in chk[0].lower() else 2

        if user["credits"] < total_deduct + cr:
            break

        total_deduct += cr
        resultados.append(
            f"<b>Card:</b> <code>{cc}</code>\n"
            f"<b>Status:</b> {chk[0]}\n"
            f"<b>Msg:</b> <code>{chk[1]}</code>\n"
            f"<b>Country:</b> {country}"
        )

    if total_deduct:
        MongoDB().user.update_one(
            {"id": user["id"]}, {"$inc": {"credits": -total_deduct}}
        )

    msg.edit_text(f"""<b>{gate} Finalizado</b>

{"\n\n".join(resultados)}

━━━━━━━━━━━━━━━━━━
• Créditos: {total_deduct}
• Tiempo: {time.time() - inicio:.2f}s
• By: {m.from_user.first_name}
""")
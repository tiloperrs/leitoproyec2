import requests
import time
from concurrent.futures import ThreadPoolExecutor
from srca.configs import addCommand, Client
from db.mongo_client import MongoDB


TEST_IP = "https://api.ipify.org"
TEST_HEADERS = "https://httpbin.org/headers"
TEST_HTTPS = "https://httpbin.org/ip"


def check_proxy(proxy):

    proxy_dict = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }

    try:

        start = time.time()

        r1 = requests.get(TEST_IP, proxies=proxy_dict, timeout=10)
        if r1.status_code != 200:
            return None

        r2 = requests.get(TEST_HEADERS, proxies=proxy_dict, timeout=10)
        if r2.status_code != 200:
            return None

        headers = r2.text.lower()

        if "x-forwarded-for" in headers:
            return None

        if "via" in headers:
            return None

        r3 = requests.get(TEST_HTTPS, proxies=proxy_dict, timeout=10)
        if r3.status_code != 200:
            return None

        speed = round(time.time() - start, 2)

        if speed > 3:
            return None

        return proxy

    except:
        return None


def get_proxies():

    sources = [

        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http",

        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",

        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",

        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",

        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",

        "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",

        "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt"
    ]

    proxies = []

    for url in sources:

        try:
            r = requests.get(url, timeout=10)
            proxies += r.text.splitlines()

        except:
            pass

    # eliminar duplicados
    proxies = list(set(proxies))

    return proxies


@addCommand("prox")
def prox(_, m):

    db = MongoDB()

    user = db.query_user(int(m.from_user.id))

    if user is None:
        return m.reply("Usa $register primero")

    msg = m.reply("🔎 Buscando proxies...")

    proxies = get_proxies()

    msg.edit(f"⚡ {len(proxies)} proxies encontradas\nProbando...")

    working = []

    with ThreadPoolExecutor(max_workers=300) as executor:

        results = executor.map(check_proxy, proxies)

    for r in results:

        if r:
            working.append(r)

    # eliminar duplicados otra vez por seguridad
    working = list(set(working))

    filename = "elite_proxies.txt"

    with open(filename, "w") as f:

        for p in working:
            f.write(p + "\n")

    db.db.proxies.insert_one({

        "type": "elite",
        "count": len(working),
        "created": int(time.time()),
        "proxies": working

    })

    Client.send_document(
        _,
        m.chat.id,
        filename,
        caption=f"🟢 {len(working)} proxies elite"
    )

    msg.delete()
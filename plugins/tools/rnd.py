import random
import datetime
from srca.configs import addCommand
from db.mongo_client import MongoDB


# ================== PAÍSES VALIDOS ==================
COUNTRIES = {
    # ---- NORTH AMERICA ----
    "us": {"name": "United States", "region": "na", "phone": "+1",
           "zip": lambda: f"{random.randint(10000,99999)}",
           "cities": ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]},

    "ca": {"name": "Canada", "region": "na", "phone": "+1",
           "zip": lambda: f"{random.choice('ABCEGHJKLMNPRSTV')}{random.randint(1,9)}"
                          f"{random.choice('ABCEGHJKLMNPRSTV')} "
                          f"{random.randint(1,9)}{random.choice('ABCEGHJKLMNPRSTV')}{random.randint(1,9)}",
           "cities": ["Toronto", "Vancouver", "Montreal", "Calgary"]},

    # ---- LATAM ----
    "mx": {"name": "Mexico", "region": "latam", "phone": "+52",
           "zip": lambda: f"{random.randint(10000,99999)}",
           "cities": ["Mexico City", "Guadalajara", "Monterrey"]},

    "br": {"name": "Brazil", "region": "latam", "phone": "+55",
           "zip": lambda: f"{random.randint(10000,99999)}-{random.randint(100,999)}",
           "cities": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]},

    "ar": {"name": "Argentina", "region": "latam", "phone": "+54",
           "zip": lambda: f"{random.choice('ABCDEFGH')}{random.randint(1000,9999)}",
           "cities": ["Buenos Aires", "Córdoba", "Rosario"]},

    "cl": {"name": "Chile", "region": "latam", "phone": "+56",
           "zip": lambda: f"{random.randint(1000000,9999999)}",
           "cities": ["Santiago", "Valparaíso", "Concepción"]},

    "co": {"name": "Colombia", "region": "latam", "phone": "+57",
           "zip": lambda: f"{random.randint(100000,999999)}",
           "cities": ["Bogotá", "Medellín", "Cali"]},

    "pe": {"name": "Peru", "region": "latam", "phone": "+51",
           "zip": lambda: f"{random.randint(10000,99999)}",
           "cities": ["Lima", "Arequipa", "Cusco"]},

    # ---- EUROPE ----
    "es": {"name": "Spain", "region": "eu", "phone": "+34",
           "zip": lambda: f"{random.randint(10000,52999)}",
           "cities": ["Madrid", "Barcelona", "Valencia", "Sevilla"]},

    "fr": {"name": "France", "region": "eu", "phone": "+33",
           "zip": lambda: f"{random.randint(10000,95999)}",
           "cities": ["Paris", "Lyon", "Marseille", "Toulouse"]},

    "de": {"name": "Germany", "region": "eu", "phone": "+49",
           "zip": lambda: f"{random.randint(10000,99999)}",
           "cities": ["Berlin", "Munich", "Hamburg", "Frankfurt"]},

    "it": {"name": "Italy", "region": "eu", "phone": "+39",
           "zip": lambda: f"{random.randint(10000,99999)}",
           "cities": ["Rome", "Milan", "Naples", "Turin"]},

    "pt": {"name": "Portugal", "region": "eu", "phone": "+351",
           "zip": lambda: f"{random.randint(1000,9999)}-{random.randint(100,999)}",
           "cities": ["Lisbon", "Porto", "Braga"]},

    "gb": {"name": "United Kingdom", "region": "eu", "phone": "+44",
           "zip": lambda: f"{random.choice(['SW','NW','SE','NE','EC'])}{random.randint(1,9)} "
                          f"{random.randint(1,9)}{random.choice('ABCD')}{random.choice('ABCD')}",
           "cities": ["London", "Manchester", "Birmingham"]},

    "nl": {"name": "Netherlands", "region": "eu", "phone": "+31",
           "zip": lambda: f"{random.randint(1000,9999)} {random.choice('ABCD')}{random.choice('ABCD')}",
           "cities": ["Amsterdam", "Rotterdam", "Utrecht"]},

    "ch": {"name": "Switzerland", "region": "eu", "phone": "+41",
           "zip": lambda: f"{random.randint(1000,9999)}",
           "cities": ["Zurich", "Geneva", "Bern"]},

    # ---- ASIA ----
    "jp": {"name": "Japan", "region": "asia", "phone": "+81",
           "zip": lambda: f"{random.randint(100,999)}-{random.randint(1000,9999)}",
           "cities": ["Tokyo", "Osaka", "Yokohama"]},

    "kr": {"name": "South Korea", "region": "asia", "phone": "+82",
           "zip": lambda: f"{random.randint(10000,99999)}",
           "cities": ["Seoul", "Busan", "Incheon"]},

    "cn": {"name": "China", "region": "asia", "phone": "+86",
           "zip": lambda: f"{random.randint(100000,999999)}",
           "cities": ["Beijing", "Shanghai", "Shenzhen"]},

    "in": {"name": "India", "region": "asia", "phone": "+91",
           "zip": lambda: f"{random.randint(100000,999999)}",
           "cities": ["Mumbai", "Delhi", "Bangalore"]},

    # ---- AFRICA ----
    "za": {"name": "South Africa", "region": "afr", "phone": "+27",
           "zip": lambda: f"{random.randint(1000,9999)}",
           "cities": ["Johannesburg", "Cape Town", "Durban"]},

    "ng": {"name": "Nigeria", "region": "afr", "phone": "+234",
           "zip": lambda: f"{random.randint(100000,999999)}",
           "cities": ["Lagos", "Abuja", "Ibadan"]},

    "eg": {"name": "Egypt", "region": "afr", "phone": "+20",
           "zip": lambda: f"{random.randint(10000,99999)}",
           "cities": ["Cairo", "Giza", "Alexandria"]},

    # ---- MIDDLE EAST ----
    "ae": {"name": "United Arab Emirates", "region": "me", "phone": "+971",
           "zip": lambda: "00000",
           "cities": ["Dubai", "Abu Dhabi", "Sharjah"]},

    "sa": {"name": "Saudi Arabia", "region": "me", "phone": "+966",
           "zip": lambda: f"{random.randint(10000,99999)}",
           "cities": ["Riyadh", "Jeddah", "Mecca"]},
}

# ================== DATOS POR REGIÓN ==================
FIRST_NAMES = {
    "na": ["James", "Michael", "David", "Emily", "Sarah"],
    "latam": ["Juan", "Carlos", "Sofia", "Maria"],
    "eu": ["Luca", "Pierre", "Anna", "Laura"],
    "asia": ["Kenji", "Hiroshi", "Aiko", "Yuki"],
    "afr": ["Kwame", "Amadou", "Amina", "Zara"],
    "me": ["Ahmed", "Omar", "Layla", "Noor"],
}

LAST_NAMES = {
    "na": ["Smith", "Johnson", "Brown"],
    "latam": ["Gomez", "Martinez", "Lopez"],
    "eu": ["Rossi", "Dubois", "Muller"],
    "asia": ["Sato", "Tanaka", "Wang"],
    "afr": ["Diallo", "Mensah", "Okoye"],
    "me": ["Haddad", "Khalil", "Aziz"],
}

STREETS = {
    "na": ["Main St", "Oak Avenue", "Maple Street"],
    "latam": ["Avenida Central", "Calle Principal"],
    "eu": ["High Street", "King Street", "Victoria Road"],
    "asia": ["Chuo Dori", "Sakura Street"],
    "afr": ["Independence Road", "Market Street"],
    "me": ["Al Noor Street", "Sheikh Zayed Road"],
}

EMAIL_DOMAINS = ["gmail.com", "outlook.com", "yahoo.com"]


# ================== COMANDO ==================
@addCommand('rnd')
def rnd(_, m):
    if MongoDB().query_group(m.chat.id) is None:
        return m.reply("Chat not Authorized.")

    user = MongoDB().query_user(int(m.from_user.id))
    if not user:
        return m.reply("Usar el comando $register.")
    if user["role"] == "baneado":
        return m.reply("User baneado.")

    args = m.text.split()
    if len(args) < 2:
        return m.reply("Ej: $rnd us | es | br | jp | ae")

    code = args[1].lower()
    cfg = COUNTRIES.get(code)

    if not cfg:
        return m.reply("País no soportado.")

    region = cfg["region"]

    first = random.choice(FIRST_NAMES[region])
    last = random.choice(LAST_NAMES[region])
    city = random.choice(cfg["cities"])
    street = f"{random.randint(1,9999)} {random.choice(STREETS[region])}"
    zip_code = cfg["zip"]()

    age = random.randint(18, 65)
    year = datetime.date.today().year - age
    dob = f"{year}-{random.randint(1,12):02}-{random.randint(1,28):02}"

    email = f"{first.lower()}{last.lower()}{random.randint(10,99)}@{random.choice(EMAIL_DOMAINS)}"
    phone = f"{cfg['phone']} {random.randint(600000000,999999999)}"

    text = f"""<b>[🌎] INFORMACIÓN VALIDADA
━━━━━━━━━━━━━━━━
 • Name : <code>{first} {last}</code>
 • Age : <code>{age}</code>
 • DOB : <code>{dob}</code>
 • Email : <code>{email}</code>
 • Phone : <code>{phone}</code>

 • Street : <code>{street}</code>
 • City : <code>{city}</code>
 • Zip : <code>{zip_code}</code>
 • Country : <code>{cfg['name']}</code>
━━━━━━━━━━━━━━━━</b>"""

    m.reply(text)
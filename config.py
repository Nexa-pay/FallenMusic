from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("34569477"))
API_HASH = getenv("3967519b70936b859949e093f873141a")

BOT_TOKEN = getenv("BOT_TOKEN", 8276604094:AAHJwN7-6jw4_ZaL25PKMD6nMQhUEt0cnMs)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("8264803525"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tunemusic_dot")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PolicyPixels")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

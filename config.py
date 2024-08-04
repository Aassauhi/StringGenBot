from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("12557431"))
API_HASH = getenv("dbf930927f239982765d29cf6cb9a579")

BOT_TOKEN = getenv("7029065576:AAHReOT0L-nZDYdB2nlrqbRHkmfKVwZwYek")
MONGO_DB_URI = getenv("mongodb+srv://jaypck:ey8ZyUVRcKiiiO3A@cluster0.q7zla97.mongodb.net/?retryWrites=true&w=majority", None)

OWNER_ID = int(getenv("OWNER_ID", 6724898708)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/gujhadi")

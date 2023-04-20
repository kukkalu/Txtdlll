import os

API_ID = API_ID = 26435700

API_HASH = os.environ.get("API_HASH", "527cf5174e120a9093611bc69d7b7709")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5898578245:AAEmaAGMRrfmu5qR1jHWMKPA9AeB3mtF_SA")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5908818236)

LOG = -1001902213617

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5908818236").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)

import os

API_ID = API_ID = 952608

API_HASH = os.environ.get("API_HASH", "8d8d0ad8e3d4bcd54420190f57da78ad")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5626113427:AAE1eEJpYOqNAIGm96ucXYWYFK0Gu49YFjA")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 818269274)

LOG = -818269274

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "818269274").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)



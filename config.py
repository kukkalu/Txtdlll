import os

API_ID = API_ID = 10577960

API_HASH = os.environ.get("API_HASH", "80fd047285f4e94ca80311928b6bb5da")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6286056110:AAHvTTaBxAMikfamkeFs8TlBjNNxnK8AoEg")

PASS_DB = int(os.environ.get("PASS_DB", "100"))

OWNER = int(os.environ.get("OWNER", 5593532344))

LOG = -1001981770797

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5593532344").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)

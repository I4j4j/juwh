import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6753870288:AAFX77cjvUlMG1Jon2V4FNtxajclkMbM67A")

    APP_ID = int(os.environ.get("APP_ID","25217515")

    API_HASH = os.environ.get("API_HASH", "1bb27e5be73593e33fc735c1fbe0d855")

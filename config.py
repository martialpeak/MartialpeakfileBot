import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5554849329:AAFP-IUeWzPRwszUFIEhFz35DAYiXnRwAVI")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "14017215"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "edeeac7a9320471c96ec38a897d68684")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001546256298"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "492438607"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://fbzgsyhrwbxiuj:7e6c715cb5e0b093784602a9f53be71cc53aa1368df1ee85a2f9cc8819e4ee83@ec2-3-215-164-137.compute-1.amazonaws.com:5432/d8qb9pilu2a2g4")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001687042819"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\n🆔@MartialPeak_Ch 🆔@IrManhwa")
try:
    ADMINS=[492438607 5361266585]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>join Channel\n\nPlease join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

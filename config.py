import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "ImTharuk")
ALIVE_NAME = getenv("ALIVE_NAME", "SL Bots")
BOT_USERNAME = getenv("BOT_USERNAME", "videostreamslbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SLBotsofficialHelp")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "trtechguide")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SLBotsOfficial")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/88ae1aa43400b2c6a855d.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TharukRenuja/VStream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/b534c2f75460135b3d1bd.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/c31fa74425577233bc4e0.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/15065fb564b783d9ccfc8.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/f05fe24920a7cdc3d5b34.jpg")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "Client0")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))

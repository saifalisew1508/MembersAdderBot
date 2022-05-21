import re
import sys
from os import getenv

from dotenv import load_dotenv


load_dotenv()


# Get it from my.telegram.org
APP_ID = int(getenv("APP_ID", ""))
API_HASH = getenv("API_HASH")

# Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

#MIT License

#Copyright (c) 2024 ᴋᴜɴᴀʟ [AFK]

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import logging
from telethon import TelegramClient
from os import getenv
from STORM.data import DEV

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

API_ID = 25574934
API_HASH = "029944bda8b241aacbb38b7eaa58d851"
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", default=None)
BOT_TOKEN2 = getenv("BOT_TOKEN2", default=None)
BOT_TOKEN3 = getenv("BOT_TOKEN3", default=None)
BOT_TOKEN4 = getenv("BOT_TOKEN4", default=None)
BOT_TOKEN5 = getenv("BOT_TOKEN5", default=None)
BOT_TOKEN6 = getenv("BOT_TOKEN6", default=None)
BOT_TOKEN7 = getenv("BOT_TOKEN7", default=None)
BOT_TOKEN8 = getenv("BOT_TOKEN8", default=None)
BOT_TOKEN9 = getenv("BOT_TOKEN9", default=None)
BOT_TOKEN10 = getenv("BOT_TOKEN10", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="7714883515").split()))
for x in DEV:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="7710642242"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('ᴀ ɴ ɪ ᴍ ᴀ ʟ 1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('ᴀ ɴ ɪ ᴍ ᴀ ʟ 2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('ᴀ ɴ ɪ ᴍ ᴀ ʟ 3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('ᴀ ɴ ɪ ᴍ ᴀ ʟ 4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('ᴀ ɴ ɪ ᴍ ᴀ ʟ 5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('ᴀ ɴ ɪ ᴍ ᴀ ʟ 6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('ᴀ ɴ ɪ ᴍ ᴀ ʟ 7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('ᴀ ɴ ɪ ᴍ ᴀ ʟ 8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('ᴀ ɴ ɪ ᴍ ᴀ ʟ 9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('ᴀ ɴ ɪ ᴍ ᴀ ʟ 10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

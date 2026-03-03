import os
import asyncio
import random
from telethon import TelegramClient, events
from telethon.errors import FloodWaitError

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

source_channel = "mavanisunny"
earnkaro_bot = "EarnKaroBot"  # apna actual bot username

client = TelegramClient("session.session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    await asyncio.sleep(random.randint(5,15))
    try:
        await event.forward_to(earnkaro_bot)
        print("Forwarded")
    except FloodWaitError as e:
        await asyncio.sleep(e.seconds)
        await event.forward_to(earnkaro_bot)

print("Bot started successfully")
client.start()
client.run_until_disconnected()

from telethon import TelegramClient, events
import asyncio
import os
import random

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

source_channel = "mavanisunny"
earnkaro_bot = "ekconverter9bot"

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    await asyncio.sleep(random.randint(5,15))
    try:
        await event.forward_to(earnkaro_bot)
    except Exception as e:
        print(e)

client.start()
client.run_until_disconnected()

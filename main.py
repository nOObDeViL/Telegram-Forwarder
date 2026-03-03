from telethon import TelegramClient, events
import os
import asyncio

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

client = TelegramClient("session", api_id, api_hash)

SOURCE = "mavanisunny"
DESTINATION = "ekconverter9bot"

@client.on(events.NewMessage(chats=SOURCE))
async def handler(event):
    await client.send_message(DESTINATION, event.message)

async def main():
    await client.start()
    print("Bot started successfully")

    # This keeps the container alive forever
    await client.run_until_disconnected()

asyncio.run(main())

from telethon import TelegramClient, events
import os
import asyncio

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

client = TelegramClient("session", api_id, api_hash)

SOURCE = "your_source_channel"
DESTINATION = "your_destination_channel"

@client.on(events.NewMessage(chats=SOURCE))
async def handler(event):
    await client.send_message(DESTINATION, event.message)

async def main():
    await client.start()  # session file already exists, safe
    print("Bot started successfully")

    # Keep program alive forever
    await asyncio.Event().wait()

asyncio.run(main())

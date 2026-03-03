from telethon import TelegramClient, events
import os
import asyncio

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

client = TelegramClient("session", api_id, api_hash)

SOURCE = "source_channel_username"
DESTINATION = "destination_channel_username"

@client.on(events.NewMessage(chats=SOURCE))
async def handler(event):
    await client.send_message(DESTINATION, event.message)

async def main():
    await client.connect()

    if not await client.is_user_authorized():
        print("Session invalid")
        return

    print("Bot started successfully")
    await client.run_until_disconnected()

asyncio.run(main())

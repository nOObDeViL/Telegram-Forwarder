from telethon import TelegramClient
import os
import asyncio

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

client = TelegramClient("session", api_id, api_hash)

async def main():
    await client.connect()

    if not await client.is_user_authorized():
        print("Session invalid. Generate new session locally.")
        return

    print("Bot started successfully")
    await client.run_until_disconnected()

asyncio.run(main())

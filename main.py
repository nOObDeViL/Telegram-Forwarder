from telethon import TelegramClient, events
import os
import asyncio

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

client = TelegramClient("session", api_id, api_hash)

SOURCE = "mavanisunny"

async def main():
    await client.start()
    print("Bot started successfully")

    # Properly resolve bot entity once
    bot_entity = await client.get_entity("ekconverter9bot")

    @client.on(events.NewMessage(chats=SOURCE))
    async def handler(event):
        try:
            await client.forward_messages(bot_entity, event.message)
            print("Forwarded to bot")
        except Exception as e:
            print("Forward error:", e)

    await client.run_until_disconnected()

asyncio.run(main())

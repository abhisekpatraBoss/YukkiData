from pyrogram import Client, filters
from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

app = Client("rawdatabot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.all)
async def raw_handler(client, message):
    await message.reply(
        f"<b>Raw Data:</b>\n<pre>{message}</pre>",
        quote=True,
        parse_mode="html"
    )

app.run()

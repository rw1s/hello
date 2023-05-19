import pyrogram
from pyrogram import Client
import os
api_id = os.environ.get("api_id")
api_hash = os.environ.get("api_hash")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
session = os.environ.get("pyrogram")
token = os.environ.get("TOKEN")
bh = Client("", api_id=api_id, api_hash=api_hash,session_string=session)
bh.run()
bot = Client("bot", api_id=APP_ID, api_hash=APP_HASH,bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.run()

from pyrogram import filters, Client
from pyrogram.types import Message
from pytgcalls.__version__ import __version__ as pytgver
from pymongo import __version__ as mongo_version
from pyrogram import __version__ as pyrogram_version

from config import OWNER_ID
from FallenMusic import app
from FallenMusic.Helpers.database.chatsdb import get_served_chats
from FallenMusic.Helpers.database.usersdb import get_served_users

# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["stats"]) & filters.user(OWNER_ID))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""**Bot İstatistikleri Ve Bilgileri**{(await cli.get_me()).mention} :
        
**📍 MongoDB Versiyonu:** `{mongo_version}`
**📍 Pyrogram Versiyonu:** `{pyrogram_version}`
**📍 Py-TgCalls Versiyonu:** `{pytgver}`

**👤 Kullanıcı Sayısı:** `{users}`
**👥 Grup Sayısı:** `{chats}` """
    )
    

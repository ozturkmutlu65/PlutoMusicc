import asyncio
from config import OWNER_ID
from FallenMusic import app
from pyrogram import filters
from FallenMusic.Helpers.database.chatsdb import get_served_chats

from pyrogram.errors import FloodWait 
from pyrogram.types import Message



@app.on_message(filters.command(["duyuru"]) & filters.user(OWNER_ID))
async def broadcast(_, message):
    if message.reply_to_message:
        x = message.reply_to_message.id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                "**Kullanım**:\n/duyuru [MESAJ] yada [Mesaj yanıtla]"
            )
        query = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            await app.forward_messages(
                i, y, x
            ) if message.reply_to_message else await app.send_message(
                i, text=query
            )
            sent += 1
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
    try:
        await message.reply_text(
            f"**{sent} Gruba gönderildi.**"
        )
    except:
        pass

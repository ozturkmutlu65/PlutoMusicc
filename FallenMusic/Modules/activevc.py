from pyrogram import filters
from pyrogram.types import Message

from config import OWNER_ID
from FallenMusic import app
from FallenMusic.Helpers.active import get_active_chats
from FallenMusic.Helpers.inline import close_key


@app.on_message(filters.command(["aktifses"]) & filters.user(OWNER_ID))
async def activevc(_, message: Message):
    mystic = await message.reply_text("» ᴀᴋᴛɪғ sᴇsʟɪ sᴏʜʙᴇᴛ ʟɪsᴛᴇsɪ ᴀʟıɴıʏᴏʀ...")
    chats = await get_active_chats()
    text = ""
    j = 0
    for chat in chats:
        try:
            title = (await app.get_chat(chat)).title
        except Exception:
            title = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        if (await app.get_chat(chat)).username:
            user = (await app.get_chat(chat)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{chat}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("ᴀᴋᴛɪғ sᴇsʟɪ sᴏʜʙᴇᴛ ʏᴏᴋ...")
    else:
        await mystic.edit_text(
            f"**ᴀᴋᴛɪғ ᴏʟᴀɴ sᴇsʟɪ sᴏʜʙᴇᴛ ʟɪsᴛᴇsɪ :**\n\n{text}",
            reply_markup=close_key,
            disable_web_page_preview=True,
        )

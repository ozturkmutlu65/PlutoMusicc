from pyrogram import filters
from pyrogram.types import Message

from FallenMusic import app, pytgcalls
from FallenMusic.Helpers import admin_check, close_key, is_streaming, stream_on


@app.on_message(filters.command(["devam", "resume"]) & filters.group)
@admin_check
async def res_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass

    if await is_streaming(message.chat.id):
        return await message.reply_text("ʏᴀʏıɴı ᴅᴜʀᴀᴋʟᴀᴛᴛıɢ̆ıɴı ʜᴀᴛıʀʟıʏᴏʀ ᴍᴜsᴜɴ?")
    await stream_on(message.chat.id)
    await pytgcalls.resume_stream(message.chat.id)
    return await message.reply_text(
        text=f"➻ ʏᴀʏıɴı sᴜ̈ʀᴅᴜ̈ʀᴅᴜ̈ 💫\n│ \n👉: {message.from_user.mention} 🥀",
        reply_markup=close_key,
    )

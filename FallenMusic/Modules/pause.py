from pyrogram import filters
from pyrogram.types import Message

from FallenMusic import app, pytgcalls
from FallenMusic.Helpers import admin_check, close_key, is_streaming, stream_off


@app.on_message(filters.command(["durdur", "pause"]) & filters.group)
@admin_check
async def pause_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass

    if not await is_streaming(message.chat.id):
        return await message.reply_text(
            "Akışa devam etmeyeyim mi?"
        )

    await pytgcalls.pause_stream(message.chat.id)
    await stream_off(message.chat.id)
    return await message.reply_text(
        text=f"➻ ʏᴀʏıɴı ᴅᴜʀᴀᴋʟᴀᴛᴛı 🥺\n│ \n👉 : {message.from_user.mention} 🥀", reply_markup=close_key)

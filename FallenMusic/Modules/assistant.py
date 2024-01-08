from pyrogram import filters
from pyrogram.types import Message

from config import OWNER_ID
from FallenMusic import ASS_MENTION, LOGGER, app, app2



@app.on_message(filters.command(["asspfp", "setpfp"]) & filters.user(OWNER_ID))
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo:
        fuk = await message.reply_text("» ᴀsɪsᴛᴀɴıɴ ᴘʀᴏғɪʟ ʀᴇsᴍɪ ᴅᴇɢ̆ɪşɪʏᴏʀ...")
        img = await message.reply_to_message.download()
        try:
            await app2.set_profile_photo(photo=img)
            return await fuk.edit_text(
                f"» {ASS_MENTION} ᴘʀᴏғɪʟ ʀᴇsᴍɪ ʙᴀşᴀʀıʏʟᴀ ᴅᴇɢ̆ɪşᴛɪʀɪʟᴅɪ."
            )
        except:
            return await fuk.edit_text("» ʜᴀᴛᴀ.. ᴘʀᴏғɪʟ ʀᴇsᴍɪ ᴅᴇɢ̆ɪşᴛɪʀɪʟᴇᴍᴇᴅɪ.")
    else:
        await message.reply_text(
            "» ᴘʀᴏғɪʟɪɴ ʀᴇsᴍɪɴɪ ᴅᴇɢ̆ɪşᴛɪʀᴍᴇᴋ ɪᴄ̧ɪɴ ʙɪʀ ғᴏᴛᴏɢ̆ʀᴀғᴀ ʏᴀɴıᴛ ᴠᴇʀɪɴ."
        )

@app.on_message(filters.command(["delpfp", "delasspfp"]) & filters.user(OWNER_ID))
async def set_pfp(_, message: Message):
    try:
        pfp = [p async for p in app2.get_chat_photos("me")]
        await app2.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text(
            "» ᴘʀᴏғɪʟ ʀᴇsᴍɪ ʙᴀşᴀʀıʏʟᴀ sɪʟɪɴᴅɪ."
        )
    except Exception as ex:
        LOGGER.error(ex)
        await message.reply_text("» ʜᴀᴛᴀ.. ᴘʀᴏғɪʟ ʀᴇsᴍɪ ᴅᴇɢ̆ɪşᴛɪʀɪʟᴇᴍᴇᴅɪ.")


@app.on_message(filters.command(["assbio", "setbio"]) & filters.user(OWNER_ID))
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            await app2.update_profile(bio=newbio)
            return await message.reply_text(
                f"» {ASS_MENTION} ʙɪᴏ ʙᴀşᴀʀıʏʟᴀ ᴅᴇɢ̆ɪşᴛɪʀɪʟᴅɪ."
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        await app2.update_profile(bio=newbio)
        return await message.reply_text(f"» {ASS_MENTION} ʙɪᴏ ʙᴀşᴀʀıʏʟᴀ ᴅᴇɢ̆ɪşᴛɪʀɪʟᴅɪ.")
    else:
        return await message.reply_text(
            "» ʙɪʀ ᴍᴇsᴀᴊᴀ ʏᴀɴıᴛ ᴠᴇʀɪɴ ʏᴀ ᴅᴀ ʙɪʀ ᴍᴇᴛɪɴ ʏᴀᴢıɴ."
        )

@app.on_message(filters.command(["assname", "setname"]) & filters.user(OWNER_ID))
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            await app2.update_profile(first_name=name)
            return await message.reply_text(
                f"» {ASS_MENTION} ɪsɪᴍ ʙᴀsᴀʀıʏʟᴀ ᴅᴇɢ̆ɪşᴛɪʀɪʟᴅɪ."
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        await app2.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"» {ASS_MENTION} ɪsɪᴍ ʙᴀsᴀʀıʏʟᴀ ᴅᴇɢ̆ɪşᴛɪʀɪʟᴅɪ.")
    else:
        return await message.reply_text(
            "» ʙɪʀ ᴍᴇsᴀᴊᴀ ʏᴀɴıᴛ ᴠᴇʀɪɴ ʏᴀ ᴅᴀ ʙɪʀ ᴍᴇᴛɪɴ ʏᴀᴢıɴ."
        )

from typing import Callable

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import CallbackQuery, Message

from FallenMusic import app

from .active import is_active_chat


def admin_check(func: Callable) -> Callable:
    async def non_admin(_, message: Message):
        if not await is_active_chat(message.chat.id):
            return await message.reply_text("ʙᴏᴛ şᴜᴀɴ ʏᴀʏıɴ ʏᴀᴘᴍıʏᴏʀ.")


        check = await app.get_chat_member(message.chat.id, message.from_user.id)
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply_text(
                "» ʏᴏ̈ɴᴇᴛɪᴄɪ ᴅᴇɢ̆ɪʟsɪɴ ʙᴇʙᴇɢ̆ɪᴍ, ʟᴜ̈ᴛғᴇɴ ᴢᴏʀʟᴀᴍᴀ."
            )

        admin = (
            await app.get_chat_member(message.chat.id, message.from_user.id)
        ).privileges
        if admin.can_manage_video_chats:
            return await func(_, message)
        else:
            return await message.reply_text(
                "» ʙᴜ ɪşʟᴇᴍɪ ʏᴀᴘᴍᴀᴋ ɪᴄ̧ɪɴ ʏᴇᴛᴋɪɴ ʏᴏᴋ."
            )

    return non_admin


def admin_check_cb(func: Callable) -> Callable:
    async def cb_non_admin(_, query: CallbackQuery):
        if not await is_active_chat(query.message.chat.id):
            return await query.answer(
                "ʙᴏᴛ şᴜᴀɴ ʏᴀʏıɴ ʏᴀᴘᴍıʏᴏʀ.", show_alert=True
            )


        try:
            check = await app.get_chat_member(query.message.chat.id, query.from_user.id)
        except:
            return
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await query.answer(
                "» ʏᴏ̈ɴᴇᴛɪᴄɪ ᴅᴇɢ̆ɪʟsɪɴ ʙᴇʙᴇɢ̆ɪᴍ, ʟᴜ̈ᴛғᴇɴ ᴢᴏʀʟᴀᴍᴀ.",
                show_alert=True,
            )

        admin = (
            await app.get_chat_member(query.message.chat.id, query.from_user.id)
        ).privileges
        if admin.can_manage_video_chats:
            return await func(_, query)
        else:
            return await query.answer(
                "» ʙᴜ ɪşʟᴇᴍɪ ʏᴀᴘᴍᴀᴋ ɪᴄ̧ɪɴ ʏᴇᴛᴋɪɴ ʏᴏᴋ.",
                show_alert=True,
            )

    return cb_non_admin

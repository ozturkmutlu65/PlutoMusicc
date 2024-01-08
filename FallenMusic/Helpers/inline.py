from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✯ ᴋᴀᴘᴀᴛ ✯", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="ʙᴇɴɪ ɢʀᴜʙᴜɴᴀ ᴇᴋʟᴇ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="ʏᴀʀᴅıᴍ & ᴋᴏᴍᴜᴛʟᴀʀ", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="❄ ᴄʜᴀɴɴᴇʟ ❄", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="✨ ᴅᴇsᴛᴇᴋ ✨", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="☁️ ᴋᴀʏɴᴀᴋ ᴋᴏᴅ ☁️", url="https://github.com/PlutoOwner/PlutoMuzik"
        ),
        InlineKeyboardButton(text="👤 sᴀʜɪ̇ᴘ", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(text="✨ ᴅᴇsᴛᴇᴋ ✨", url=config.SUPPORT_CHAT)
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="ɢᴇɴᴇʟ ᴋᴏᴍᴜᴛʟᴀʀ",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="ᴀᴢəʀʙᴀʏᴄᴀɴ", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="sᴀʜɪᴘ", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="ɢᴇʀɪ", callback_data="fallen_home"),
        InlineKeyboardButton(text="ᴋᴀᴘᴀᴛ", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="✨ ᴅᴇsᴛᴇᴋ ✨", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="ɢᴇʀɪ", callback_data="fallen_help"),
        InlineKeyboardButton(text="ᴋᴀᴘᴀᴛ", callback_data="close"),
    ],
]

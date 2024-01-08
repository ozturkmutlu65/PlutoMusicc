from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
from youtubesearchpython.__future__ import VideosSearch

from FallenMusic import BOT_NAME, app


@app.on_inline_query()
async def inline_query_handler(_, query):
    text = query.query.strip().lower()
    answers = []
    if text.strip() == "":
        try:
            await app.answer_inline_query(
                query.id,
                results=answers,
                switch_pm_text="ʏᴏᴜᴛᴜʙᴇ'ᴅᴇ ᴀʀᴀʏᴀʙɪʟᴇᴄᴇɢ̆ɪɴɪᴢ ʙɪʀ şᴇʏ ʏᴀᴢıɴ...",
                cache_time=10,
            )
        except:
            return
    else:
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")
        for x in range(15):
            title = (result[x]["başlık"]).title()
            duration = result[x]["süre"]
            views = result[x]["viewCount"]["short"]
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[0]
            channellink = result[x]["channel"]["link"]
            channel = result[x]["channel"]["name"]
            link = result[x]["link"]
            published = result[x]["publishedTime"]
            description = f"{views} | {duration} Mins | {channel}  | {published}"
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="• ʏᴏᴜᴛᴜʙᴇ •",
                            url=link,
                        )
                    ],
                ]
            )
            searched_text = f"""
✨ **ʙᴀşʟıᴋ :** [{title}]({link})

⏳ **sᴜ̈ʀᴇ :** `{duration}`ᴍɪɴᴜᴛᴇs
👀 **ɢᴏ̈ʀᴜ̈ɴᴛᴜ̈ʟᴇᴍᴇ :** `{views}`
⏰ **ʏᴀʏıɴʟᴀɴᴅı :** {published}
🎥 **ᴋᴀɴᴀʟ :** [{channel}]({channellink})

<u>💖 **ᴀʀᴀᴍᴀʏı ɢᴜ̈ᴄ̧ʟᴇɴᴅɪʀᴇɴ {BOT_NAME}**</u>"""
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    thumb_url=thumbnail,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )
        try:
            return await app.answer_inline_query(query.id, results=answers)
        except:
            return

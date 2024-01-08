import os

import requests
import yt_dlp
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch

import config
from FallenMusic import BOT_MENTION, BOT_USERNAME, LOGGER, app


@app.on_message(filters.command(["song", "bul", "indir", "music"]))
async def song(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    m = await message.reply_text("🔎")

    query = "".join(" " + str(i) for i in message.command[1:])
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=5).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as ex:
        LOGGER.error(ex)
        return await m.edit_text(
            f"YT-DL'den parça alınamadı.\n\nNedeni:** `{ex}`"
        )

    await m.edit_text("» Şarkı indiriliyor,\n\nLütfen bekleyin....")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"☁️ **Başlık :** [{title[:23]}]({link})\n⏱️ **Süre :** `{duration}`\n🗳 **Yükleyen :** {BOT_MENTION}"
        res = f"👤 İstiyen [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n☁️ **Başlık :** [{title[:23]}]({link})\n⏱️ **Süre :** `{duration}`\n🗳 **Yükleyen :** @{BOT_USERNAME}"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        try:
            visit_butt = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎧 𝐌𝐮̈𝐳𝐢𝐤 𝐊𝐚𝐧𝐚𝐥ı", url=config.PLAYLIST
                        )
                    ]
                ]
            )
            await app.send_audio(
                chat_id=message.from_user.id,
                audio=audio_file,
                caption=rep,
                thumb=thumb_name,
                title=title,
                duration=dur,
                reply_markup=visit_butt,
            )
            await app.send_audio(
                chat_id=config.PLAYLIST_ID,
                audio=audio_file,
                caption=res,
                thumb=thumb_name,
                title=title,
                duration=dur,
            )
            if message.chat.type != ChatType.PRIVATE:
                await message.reply_text(
                    "Lütfen özel mesajlarınızı kontrol edin, istediğiniz şarkıyı oraya gönderdim."
                )
        except:
            start_butt = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🙋🏻 Buradan",
                            url=f"https://t.me/{BOT_USERNAME}?start",
                        )
                    ]
                ]
            )
            return await m.edit_text(
                text="YouTube'dan Müziği yalnızca özel sohbette indirebilirsiniz. Lütfen beni özel sohbette başlat.",
                reply_markup=start_butt,
            )
        await m.delete()
    except:
        return await m.edit_text("Telegram sunucularına ses yüklemesi başarısız oldu.")

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as ex:
        LOGGER.error(ex)

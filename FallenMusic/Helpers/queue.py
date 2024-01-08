from FallenMusic import fallendb


async def put(
    chat_id,
    title,
    duration,
    videoid,
    file_path,
    ruser,
    user_id,
):
    put_f = {
        "title": title,
        "duration": duration,
        "file_path": file_path,
        "videoid": videoid,
        "req": ruser,
        "user_id": user_id,
    }
    get = fallendb.get(chat_id)
    if get:
        fallendb[chat_id].append(put_f)
    else:
        fallendb[chat_id] = []
        fallendb[chat_id].append(put_f)

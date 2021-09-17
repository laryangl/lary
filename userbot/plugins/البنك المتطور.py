
import os
from datetime import datetime

from userbot import catub

from . import hmention, reply_id

"""
try:
    from . import PING_PIC, PING_TEXT
except:
    pass
"""
plugin_category = "tools"

PING_PIC = os.environ.get("PING_PIC") or (
    "https://telegra.ph/file/1700c83603e7d29b82ffc.png"
)

JM_TXT = os.environ.get("PING_TEXT") or ""I wish to meet you in Tokyo in the city of love and love and tears and laughs and sing together" your looks embarrass me and forget where I am" and laugh and exchange looks ."


@catub.cat_cmd(
    pattern="بنك$",
    command=("بنك", plugin_category),
    info={
        "header": "امر تجربه البوت اذا يشتغل ارسل  .بنك فقط",
        "option": "امر بنك المتطور كتابة  @",
        "usage": [
            "{tr}بنك",
        ],
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    start = datetime.now()
    cat = await edit_or_reply(
        event, "<b><i>  ❤️⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃟✨ البــــنك... 🍀⃝⃝⃟🍂 </b></i>", "html"
    )
    end = datetime.now()
    await cat.delete()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        caption = f"<b><i>{JM_TXT}<i><b>\n<code>┏━━━━━━━┓\n┃ ✦ {ms}\n┃ ✦ <b>{hmention}</b>\n┗━━━━━━━┛"
        await event.client.send_file(
            event.chat_id,
            PING_PIC,
            caption=caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
    else:
        await event.edit_or_reply(
            event, "<code>يجـب اضـافة متـغير `PING_PIC`  اولا  f<code>", "html"
        )


# ======================================================================================================================================

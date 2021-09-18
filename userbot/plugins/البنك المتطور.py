import os
from datetime import datetime

from userbot import catub

from . import reply_id

"""
try:
    from . import PING_PIC, PING_TEXT
except:
    pass
"""
plugin_category = "tools"

PING_PIC = os.environ.get("PING_PIC") or (
    "https://telegra.ph/file/a4fc6361f56d9937b4b4a.jpg"
)

JM_TXT = os.environ.get("PING_TEXT") or "˛ ٰ𝖳𝖺𝗄𝖾 𝗆𝖾 𝗍ِ𝗈 𝗒𝗈ِ𝗎  𝗒𝗈𝗎 𝗋 𝖺𝗅𝗅 𝗂 𝗐ِ𝖺𝗇𝗍 🎀ٰ ."


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
        event, "<b><i> .•♫•♬•𝙋𝙞𝙉𝙜•♬•♫•. </b></i>", "html"
    )
    end = datetime.now()
    await cat.delete()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        caption = f"<b><i>{JM_TXT}<i><b>\n<code>ⵧⵧⵧⵧⵧⵧ.•♫•♬•𝙡𝙖𝙧𝙮•♬•♫•.ⵧⵧⵧⵧⵧⵧ\n︙ ❆ {ms}\n︙ ❆ <b>@CXRCX</b>\nⵧⵧⵧⵧⵧⵧ.•♫•♬•𝙡𝙖𝙧𝙮•♬•♫•.ⵧⵧⵧⵧⵧⵧ"
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

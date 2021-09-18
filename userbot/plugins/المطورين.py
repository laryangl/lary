import random
import re
import time
from platform import python_version

from telethon import version, Button
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from userbot import StartTime, catub, JMVERSION

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"

@catub.cat_cmd(
    pattern="المطور$",
    command=("المطور", plugin_category),
    info={
        "header": "لأظهار مطورين السورس",
        "usage": [
            "{tr}المطور",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  - "
    CUSTOM_ALIVE_TEXT = gvarstatus("ALIVE_TEXT")
    CAT_IMG = gvarstatus("ALIVE_PIC") or " https://telegra.ph/file/e92f1373596365f34b2f8.jpg "
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        cat_caption = f".•♫•♬•𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧 𝙎𝙤𝙐𝙧𝙘𝙀•♬•♫•.\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧʏᴏʟᴀɴᴅⵧⵧⵧⵧⵧⵧⵧⵧ𓍻
\n"
        cat_caption += f"- .•♫•♬•𝙈𝙊𝙃𝘼𝙈𝙀𝘿 •♬•♫•.   :  @EEEEE1K\n"
        cat_caption += f"- 𝙈𝙪𝙍𝙩𝘼𝙯𝙖  :  @𝘽𝘽𝘽𝙑𝙑𝘽𝙑\n"
        cat_caption += f"- 𝙏𝙤𝙁𝙮  :   @𝙈𝙈𝙇𝙈𝙈𝙈\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧʏᴏʟᴀɴᴅⵧⵧⵧⵧⵧⵧⵧⵧ𓍻
\n"
        await event.client.send_file(
            event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id
        )

@catub.cat.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await catalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)

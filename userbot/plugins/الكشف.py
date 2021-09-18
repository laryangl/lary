import html
import os

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

from userbot import catub
from userbot.core.logger import logging

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch

plugin_category = "utils"
LOGS = logging.getLogger(__name__)


async def fetch_info(replied_user, event):
    """Get details from the User object."""
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(
            user_id=replied_user.user.id, offset=42, max_id=0, limit=80
        )
    )
    replied_user_profile_photos_count = "❆︙ محاط صوره لازم يحط"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception:
        pass
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about
    replied_user.user.bot
    replied_user.user.restricted
    replied_user.user.verified
    photo = await event.client.download_profile_photo(
        user_id,
        Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",
        download_big=True,
    )
    first_name = (
        first_name.replace("\u2060", "") if first_name else ("❆︙ اسمه الاول ماكو ")
    )
    last_name = last_name.replace("\u2060", "") if last_name else (" ")
    username = "@{}".format(username) if username else ("❆︙ ضلعي هذا ماعنده معرف  ")
    user_bio = "❆︙ ما مخلي نبذا خلي يحط وتدلل" if not user_bio else user_bio
    caption = "ⵧⵧⵧⵧⵧⵧ.•♫•♬•𝙡𝙖𝙧𝙮•♬•♫•.ⵧⵧⵧⵧⵧⵧ\n\n"
    caption += f"<b>- اسمه ›</b> {first_name} {last_name}\n"
    caption += f"<b>- معرفه ›</b> {username}\n"
    caption += f"<b>- الايدي   ›</b> <code>{user_id}</code>\n"
    caption += f"<b>-  الصور شكد ›</b> {replied_user_profile_photos_count}\n"
    caption += f"<b>-️ النبذا  ›</b> \n<code>{user_bio}</code>\n\n"
    caption += f"<b>-  الكروبات الي بينك وبينه ›</b> {common_chat}\n"
    caption += f"<b>- رابط حسـابه ›</b> "
    caption += f'<a href="tg://user?id={user_id}">{first_name}</a>\n'
    caption += f"ⵧⵧⵧⵧⵧⵧ.•♫•♬•𝙡𝙖𝙧𝙮•♬•♫•.ⵧⵧⵧⵧⵧⵧ"
    return photo, caption


@catub.cat_cmd(
    pattern="كشف(?:\s|$)([\s\S]*)",
    command=("كشف", plugin_category),
    info={
        "header": "Gets information of an user such as restrictions ban by spamwatch or cas.",
        "description": "That is like whether he banned is spamwatch or cas and small info like groups in common, dc ..etc.",
        "usage": "{tr}userinfo <username/userid/reply>",
    },
)
async def _(event):
    "Gets information of an user such as restrictions ban by spamwatch or cas"
    replied_user, error_i_a = await get_user_from_event(event)
    if not replied_user:
        return
    catevent = await edit_or_reply(
        event, "❆︙ جار إحضار معلومات المستخدم اننظر قليلا ⚒️"
    )
    replied_user = await event.client(GetFullUserRequest(replied_user.id))
    user_id = replied_user.user.id
    # some people have weird HTML in their names
    first_name = html.escape(replied_user.user.first_name)
    # https://stackoverflow.com/a/5072031/4723940
    # some Deleted Accounts do not have first_name
    if first_name is not None:
        # some weird people (like me) have more than 4096 characters in their
        # names
        first_name = first_name.replace("\u2060", "")
    # inspired by https://telegram.dog/afsaI181
    common_chats = replied_user.common_chats_count
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception:
        dc_id = "Couldn't fetch DC ID!"
    if spamwatch:
        ban = spamwatch.get_ban(user_id)
        if ban:
            sw = f"**Spamwatch Banned :** `True` \n       **-**🤷‍♂️**Reason : **`{ban.reason}`"
        else:
            sw = f"**Spamwatch Banned :** `False`"
    else:
        sw = "**Spamwatch Banned :**`Not Connected`"
    try:
        casurl = "https://api.cas.chat/check?user_id={}".format(user_id)
        data = get(casurl).json()
    except Exception as e:
        LOGS.info(e)
        data = None
    if data:
        if data["ok"]:
            cas = "**Antispam(CAS) Banned :** `True`"
        else:
            cas = "**Antispam(CAS) Banned :** `False`"
    else:
        cas = "**Antispam(CAS) Banned :** `Couldn't Fetch`"
    caption = """**معلومات المسـتخدم[{}](tg://user?id={}):
   ❆︙⚕️ الايدي: **`{}`
   ❆︙👥**المجموعات المشتركه : **`{}`
   ❆︙🌏**رقم قاعده البيانات : **`{}`
   ❆︙🔏**هل هو حساب موثق  : **`{}`
""".format(
        first_name,
        user_id,
        user_id,
        common_chats,
        dc_id,
        replied_user.user.restricted,
        sw,
        cas,
    )
    await edit_or_reply(catevent, caption)


@catub.cat_cmd(
    pattern="ايدي(?:\s|$)([\s\S]*)",
    command=("ايدي", plugin_category),
    info={
        "header": "Gets info of an user.",
        "description": "User compelete details.",
        "usage": "{tr}whois <username/userid/reply>",
    },
)
async def who(event):
    "Gets info of an user"
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user, reason = await get_user_from_event(event)
    if not replied_user:
        return
    cat = await edit_or_reply(event, "**❆︙ جاي ابحوش بل حسابات صبر شوي   **")
    replied_user = await event.client(GetFullUserRequest(replied_user.id))
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return await edit_or_reply(cat, "**❆︙ ماكو هيج حساب  **")
    message_id_to_reply = await reply_id(event)
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await cat.delete()
    except TypeError:
        await cat.edit(caption, parse_mode="html")


# كـتابة  @RRRD7
# تعديل وترتيب  @SBB_B
@catub.cat_cmd(
    pattern="رابط الحساب(?:\s|$)([\s\S]*)",
    command=("رابط الحساب", plugin_category),
    info={
        "header": "Generates a link to the user's PM .",
        "usage": "{tr}link <username/userid/reply>",
    },
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"❆︙[{tag}](tg://user?id={user.id})")

# Copyright (C) 2021 catub TEAM
# FILES WRITTEN BY  @BBBVVBV *#* @EEEEE1K
import html

from telethon.tl import functions
from telethon.tl.functions.users import GetFullUserRequest

from ..Config import Config
from . import (
    ALIVE_NAME,
    AUTONAME,
    BOTLOG,
    BOTLOG_CHATID,
    DEFAULT_BIO,
    catub,
    edit_delete,
    get_user_from_event,
)

plugin_category = "utils"
DEFAULTUSER = str(AUTONAME) if AUTONAME else str(ALIVE_NAME)
DEFAULTUSERBIO = str(DEFAULT_BIO) if DEFAULT_BIO else "𝖳𝖺𝗄𝖾 𝗆𝖾 𝗍ِ𝗈 𝗒𝗈ِ𝗎  𝗒𝗈𝗎 𝗋 𝖺𝗅𝗅 𝗂 𝗐ِ𝖺𝗇𝗍 🎀 @TTTYT_M"


@catub.cat_cmd(
    pattern="بوكه(?:\s|$)([\s\S]*)",
    command=("بوكه", plugin_category),
    info={
        "header": "To clone account of mentiond user or replied user",
        "usage": "{tr}clone <username/userid/reply>",
    },
)
async def _(event):
    "To clone account of mentiond user or replied user"
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user is None:
        return
    user_id = replied_user.id
    profile_pic = await event.client.download_profile_photo(user_id, Config.TEMP_DIR)
    first_name = html.escape(replied_user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    replied_user = await event.client(GetFullUserRequest(replied_user.id))
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = replied_user.about
    await event.client(functions.account.UpdateProfileRequest(first_name=first_name))
    await event.client(functions.account.UpdateProfileRequest(last_name=last_name))
    await event.client(functions.account.UpdateProfileRequest(about=user_bio))
    pfile = await event.client.upload_file(profile_pic)
    await event.client(functions.photos.UploadProfilePhotoRequest(pfile))
    await edit_delete(event, "❆︙تم بوك الحساب بنجاح عزيزي اني بكتك ✅")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#CLONED\nsuccessfully cloned [{first_name}](tg://user?id={user_id })",
        )


@catub.cat_cmd(
    pattern="رجعه$",
    command=("رجعه", plugin_category),
    info={
        "header": "To revert back to your original name , bio and profile pic",
        "note": "For proper Functioning of this command you need to set AUTONAME and DEFAULT_BIO with your profile name and bio respectively.",
        "usage": "{tr}revert",
    },
)
async def _(event):
    "To reset your original details"
    name = f"{DEFAULTUSER}"
    blank = ""
    bio = f"{DEFAULTUSERBIO}"
    await event.client(
        functions.photos.DeletePhotosRequest(
            await event.client.get_profile_photos("me", limit=1)
        )
    )
    await event.client(functions.account.UpdateProfileRequest(about=bio))
    await event.client(functions.account.UpdateProfileRequest(first_name=name))
    await event.client(functions.account.UpdateProfileRequest(last_name=blank))
    await edit_delete(event, "❆︙ تدلل رجعتله حسابه ولا يهمك ✅")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, f"❆︙تدلل رجعتله حسابه ولا يهمك ✅"
        )

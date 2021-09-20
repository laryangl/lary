import asyncio

from telethon.tl.functions.users import GetFullUserRequest

from userbot import catub

from ..core.managers import edit_or_reply
from ..helpers.utils import _format
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, get_user_from_event

plugin_category = "admin"




@catub.cat_cmd(
    pattern="كتم(?:\s|$)([\s\S]*)",
    command=("كتم", plugin_category),
)
async def startgmute(event):
    "To mute a person in all groups where you are admin."
    if event.is_private:
        await event.edit("**.•♫•♬•𝙨𝙤𝙢𝙚 𝙥𝙧𝙤𝙗𝙡𝙚𝙢𝙨 𝙤𝙧 𝙚𝙧𝙧𝙤𝙧𝙨 𝙢𝙖𝙮 𝙤𝙘𝙘𝙪𝙧•♬•♫•.**")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == catub.uid:
            return await edit_or_reply(
                event, "**𖡛... . لمـاذا تࢪيـد كتم نفسـك؟  ...𖡛**"
            )
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(
            event, "**𖡛... غيـر قـادر عـلى جـلب مـعلومات الـشخص ...𖡛**"
        )
    if is_muted(userid, "gmute"):
        return await edit_or_reply(
            event,
            f"**𖡛... هـذا الشـخص مكـتوم بـنجاح ...𖡛**",
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**خـطأ**\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"**.•♫•♬•.User muted successfully  . مكتوم•♬•♫•.**",
            )
        else:
            await edit_or_reply(
                event,
                f"**.•♫•♬•.User muted successfully  . مكتوم•♬•♫•.**",
            )
    if BOTLOG:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                " الـكتم\n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**السبب :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                " الـكتم\n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)


# =================== الغـــــــــــــاء الكـــــــــــــــتم  ===================  #


@catub.cat_cmd(
    pattern="الغاء كتم(?:\s|$)([\s\S]*)",
    command=("الغاء كتم", plugin_category),
    info={
        "header": "To unmute the person in all groups where you were admin.",
        "description": "This will work only if you mute that person by your gmute command.",
        "usage": "{tr}ungmute <username/reply>",
    },
)
async def endgmute(event):
    "To remove gmute on that person."
    if event.is_private:
        await event.edit("**.•♫•♬•𝙨𝙤𝙢𝙚 𝙥𝙧𝙤𝙗𝙡𝙚𝙢𝙨 𝙤𝙧 𝙚𝙧𝙧𝙤𝙧𝙨 𝙢𝙖𝙮 𝙤𝙘𝙘𝙪𝙧•♬•♫•.**")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == catub.uid:
            return await edit_or_reply(event, "**𖡛... لمـاذا تࢪيـد كتم نفسـك؟ ...𖡛**")
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(
            event, "**𖡛... غيـࢪ قـادࢪ عـلى جـلب مـعلومات الـشخص ...𖡛**"
        )
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(
            event, f"**𖡛... هـذا الشـخص غيـࢪ مكـتوم اصلا  ...𖡛**"
        )
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**خطـأ**\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"**.•♫•♬•𝙈𝙪𝙏𝙚 𝙐𝙣 الكتم ملغي•♬•♫•. **",
            )
        else:
            await edit_or_reply(
                event,
                f"** .•♫•♬•𝙈𝙪𝙏𝙚 𝙐𝙣 الكتم ملغي•♬•♫•.**",
            )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "، الغـاء الـكتم\n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**السبب :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                " الغـاء الـكتم \n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )


# ===================================== #


@catub.cat_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


# =====================================  #

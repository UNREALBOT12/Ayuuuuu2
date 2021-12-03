import asyncio
from config import BOT_USERNAME, SUDO_USERS
from driver.decorators import authorized_users_only, sudo_users_only, errors
from driver.filters import command, other_filters
from driver.veez import user as USER
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant


@Client.on_message(
    command(["userbotjoin", f"userbotjoin@{BOT_USERNAME}"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
@errors
async def join_group(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except BaseException:
        await message.reply_text(
            "• **i'm not have permission:**\n\n» ❌ __Add Users__",
        )
        return

    try:
        user = await USER.get_me()
    except BaseException:
        user.first_name = "music assistant"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"🛑 𝗙𝗹𝗼𝗼𝗱 𝗪𝗮𝗶𝘁 𝗘𝗿𝗿𝗼𝗿 🛑 \n\n**ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ ᴏᴘ ᴜꜱᴇʀʙᴏᴛ ᴄᴀɴ'ᴛ ᴊᴏɪɴ ᴜʀ ɢʀᴏᴜᴘ ᴅᴜᴇ ᴛᴏ ʜᴇᴀᴠʏ ᴊᴏɪɴ ʀᴇQᴜᴇꜱᴛ.**"
            "\n\n**ᴀᴅᴅ ᴀꜱꜱɪꜱᴛᴀɴᴛ ᴍᴀɴᴜᴀʟʟʏ ɪɴ ᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ.**\n\n**ᴀꜱꜱɪꜱᴛᴀɴᴛ :  @FallenAssistant**\n\n**ᴍꜱɢ ᴀᴛ :**\n\n**@CreatorPavanSupport**\n\n**ᴏʀ ᴄᴏɴᴛᴀᴄᴛ ᴍᴀꜱᴛᴇʀ 𝙾𝚙 𝙰𝚊𝚢𝚞𝚜𝚑.**",
        )
        return
    await message.reply_text(
        f"✅ **ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ ᴏᴘ ᴜꜱʀᴇʙᴏᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴊᴏɪɴᴇᴅ ᴛʜɪꜱ ᴄʜᴀᴛ.**",
    )


@Client.on_message(command(["userbotleave",
                            f"leave@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def leave_one(client, message):
    try:
        await USER.send_message(message.chat.id, "ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ ᴏᴘ ᴜꜱʀᴇʙᴏᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʟᴇꜰᴛ ᴛʜɪꜱ ᴄʜᴀᴛ.")
        await USER.leave_chat(message.chat.id)
    except BaseException:
        await message.reply_text(
            "❌ **userbot couldn't leave your group, may be floodwaits.**\n\n**» or manually kick userbot from your group**"
        )

        return


@Client.on_message(command(["leaveall", f"leaveall@{BOT_USERNAME}"]))
@sudo_users_only
async def leave_all(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **userbot** leaving all chats !")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"Userbot leaving all group...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        except BaseException:
            failed += 1
            await lol.edit(
                f"Userbot leaving...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        await asyncio.sleep(0.7)
    await client.send_message(
        message.chat.id, f"✅ Left from: {left} chats.\n❌ Failed in: {failed} chats."
    )

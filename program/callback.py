# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""𝗧𝗵𝗶𝘀 𝗶𝘀 𝘁𝗵𝗲 𝗙𝗮𝗹𝗹𝗲𝗻 𝗠𝘂𝘀𝗶𝗰...!**
┏━━━━━━━━━━━━━━━━━┓
┣» ᴏᴘ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ. 
┣» ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴍᴜꜱɪᴄ.
┣» ᴠɪᴅᴇᴏ ᴘʟᴀʏ ꜱᴜᴘᴘᴏʀᴛᴇᴅ.
┣» ᴀᴅᴠᴀɴᴄᴇᴅ ꜰᴇᴀᴛᴜʀᴇꜱ.
┣» ꜱᴜᴘᴇʀꜰᴀꜱᴛ ꜱᴘᴇᴇᴅ.
┗━━━━━━━━━━━━━━━━━┛
ᴅᴇꜱɪɢɴᴇᴅ ʙʏ :** [𝗢𝗣 𝗔𝗔𝗬𝗨𝗦𝗛](https://t.me/Op_Aayush)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅ ʟɪꜱᴛ", callback_data="cbcmds"),
                ],[
                    InlineKeyboardButton(
                        "ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/creatorpavansupport"
                    ),
                    InlineKeyboardButton(
                        "ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/theCreatorPavan"
                    ),
                ],[
                    InlineKeyboardButton(
                        "🙂 ᴀᴅᴅ ꜰᴀʟʟᴇɴ ʙᴀʙʏ 🙂",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

💡 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ꜰᴀʟʟᴇɴ ʙᴀᴄᴋ", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""💞 **ʜᴇʟʟᴏᴡ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» ꜰᴏʀ ᴋɴᴏᴡɪɴɢ ᴀ ᴄᴏᴍᴍᴀɴᴅ ʟɪꜱᴛ ᴏꜰ ꜰᴀʟʟᴇɴ ᴊᴜꜱᴛ ᴘʀᴇꜱꜱ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴀɴᴅ ʀᴇᴀᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ᴇxᴘʟᴀɴᴀᴛɪᴏɴ.

**ᴛʜɪꜱ ᴏᴘ ʙᴏᴛ ɪꜱ ꜱᴘᴇᴄɪᴀʟʟʏ ᴅᴇꜱɪɢɴᴇᴅ ʙʏ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ ɴᴇᴛᴡᴏʀᴋ.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴀᴅᴍɪɴ ᴄᴍᴅ", callback_data="cbadmin"),
                    InlineKeyboardButton("ꜱᴜᴅᴏ ᴄᴍᴅ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("ʙᴀꜱɪᴄ ᴄᴍᴅ", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 ꜰᴀʟʟᴇɴ ʙᴀᴄᴋ", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ꜰᴀʟʟᴇɴ ʙᴀꜱɪᴄ ᴄᴏᴍᴍᴀɴᴅꜱ :

» /play [ꜱᴏɴɢ ɴᴀᴍᴇ/ʟɪɴᴋ] - ᴘʟᴀʏ ᴍᴜꜱɪᴄ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ 
» /stream [Qᴜᴇʀʏ/ʟɪɴᴋ] - ꜱᴛʀᴇᴀᴍ ᴛʜᴇ ʏᴛ ʟɪᴠᴇ/ʀᴀᴅɪᴏ ʟɪᴠᴇ ᴍᴜꜱɪᴄ 
» /vplay [ᴠɪᴅᴇᴏ ɴᴀᴍᴇ/ʟɪɴᴋ] - ᴘʟᴀʏ ᴠɪᴅᴇᴏ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ 
» /vstream - ᴘʟᴀʏ ʟɪᴠᴇ ᴠɪᴅᴇᴏ ꜰʀᴏᴍ ʏᴛ ʟɪᴠᴇ/ᴍ3ᴜ8 
» /playlist - ꜱʜᴏᴡ ʏᴏᴜ ᴛʜᴇ ᴘʟᴀʏʟɪꜱᴛ 
» /video [Qᴜᴇʀʏ] - ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ 
» /song [Qᴜᴇʀʏ] - ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴏɴɢ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ 
» /lyrics [Qᴜᴇʀʏ] - ꜱᴄʀᴀᴘ ᴛʜᴇ ꜱᴏɴɢ ʟʏʀɪᴄ 
» /search [Qᴜᴇʀʏ] - ꜱᴇᴀʀᴄʜ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ  
» /ping - ꜱʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴘɪɴɢ ꜱᴛᴀᴛᴜꜱ 
» /uptime - ꜱʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ ꜱᴛᴀᴛᴜꜱ 
» /alive - ꜱʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴀʟɪᴠᴇ ɪɴꜰᴏ [ɪɴ ɢʀᴏᴜᴘ]

**ᴛʜɪꜱ ᴏᴘ ʙᴏᴛ ɪꜱ ꜱᴘᴇᴄɪᴀʟʟʏ ᴅᴇꜱɪɢɴᴇᴅ ʙʏ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ ɴᴇᴛᴡᴏʀᴋ.**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ꜰᴀʟʟᴇɴ ʙᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ꜰᴀʟʟᴇɴ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ :

» /pause - ᴘᴀᴜꜱᴇ ᴛʜᴇ ꜱᴛʀᴇᴀᴍ 
» /resume - ʀᴇꜱᴜᴍᴇ ᴛʜᴇ ꜱᴛʀᴇᴀᴍ 
» /skip - ꜱᴡɪᴛᴄʜ ᴛᴏ ɴᴇxᴛ ꜱᴛʀᴇᴀᴍ 
» /stop - ꜱᴛᴏᴘ ᴛʜᴇ ꜱᴛʀᴇᴀᴍɪɴɢ 
» /vmute - ᴍᴜᴛᴇ ᴛʜᴇ ᴜꜱᴇʀʙᴏᴛ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ 
» /vunmute - ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴜꜱᴇʀʙᴏᴛ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ 
» /volume 1-200 - ᴀᴅᴊᴜꜱᴛ ᴛʜᴇ ᴠᴏʟᴜᴍᴇ ᴏꜰ ᴍᴜꜱɪᴄ (ᴜꜱᴇʀʙᴏᴛ ᴍᴜꜱᴛ ʙᴇ ᴀᴅᴍɪɴ) 
» /reload - ʀᴇʟᴏᴀᴅ ʙᴏᴛ ᴀɴᴅ ʀᴇꜰʀᴇꜱʜ ᴛʜᴇ ᴀᴅᴍɪɴ ᴅᴀᴛᴀ 
» /userbotjoin - ɪɴᴠɪᴛᴇ ᴛʜᴇ ᴜꜱᴇʀʙᴏᴛ ᴛᴏ ᴊᴏɪɴ ɢʀᴏᴜᴘ 
» /userbotleave - ᴏʀᴅᴇʀ ᴜꜱᴇʀʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ɢʀᴏᴜᴘ

**ᴛʜɪꜱ ᴏᴘ ʙᴏᴛ ɪꜱ ꜱᴘᴇᴄɪᴀʟʟʏ ᴅᴇꜱɪɢɴᴇᴅ ʙʏ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ ɴᴇᴛᴡᴏʀᴋ.**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ꜰᴀʟʟᴇɴ ʙᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ꜰᴀʟʟᴇɴ ꜱᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅꜱ :

» /rmw - ᴄʟᴇᴀɴ ᴀʟʟ ʀᴀᴡ ꜰɪʟᴇꜱ 
» /rmd - ᴄʟᴇᴀɴ ᴀʟʟ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ꜰɪʟᴇꜱ 
» /sysinfo - ꜱʜᴏᴡ ᴛʜᴇ ꜱʏꜱᴛᴇᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ 
» /update - ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏ ʟᴀᴛᴇꜱᴛ ᴠᴇʀꜱɪᴏɴ 
» /restart - ʀᴇꜱᴛᴀʀᴛ ʏᴏᴜʀ ʙᴏᴛ 
» /leaveall - ᴏʀᴅᴇʀ ᴜꜱᴇʀʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀʟʟ ɢʀᴏᴜᴘ

**ᴛʜɪꜱ ᴏᴘ ʙᴏᴛ ɪꜱ ꜱᴘᴇᴄɪᴀʟʟʏ ᴅᴇꜱɪɢɴᴇᴅ ʙʏ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ ɴᴇᴛᴡᴏʀᴋ.**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ꜰᴀʟʟᴇɴ ʙᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **ꜰᴀʟʟᴇɴ ꜱᴇᴛᴛɪɴɢꜱ ꜰᴏʀ** {query.message.chat.title}\n\n⏸ : ꜰᴀʟʟᴇɴ ᴘᴀᴜꜱᴇ\n▶️ : ꜰᴀʟʟᴇɴ ʀᴇꜱᴜᴍᴇ\n🔇 : ꜰᴀʟʟᴇɴ ᴍᴜᴛᴇ\n🔊 : ꜰᴀʟʟᴇɴ ᴜɴᴍᴜᴛᴇ\n⏹ : ꜰᴀʟʟᴇɴ ꜱᴛʀᴇᴀᴍ ꜱᴛᴏᴘ\n\n© @CreatorPavanNetwork",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 ꜰᴀʟʟᴇɴ ᴄʟᴏꜱᴇ", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()

# (c) @Aadhi000
from bot.client import Client
from pyrogram import filters
from pyrogram import types
from bot.core.db.add import add_user_to_database


@Client.on_message(filters.command(["start", "ping"]) & filters.private)
async def ping_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sir :(")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text=f"""<b>𝗛𝗜 {message.from_user.first_name } 👋,</b>\n"""
        "<b>𝗜 𝗖𝗔𝗡 𝗥𝗘𝗡𝗔𝗠𝗘 𝗙𝗜𝗟𝗘𝗦 𝗪𝗜𝗧𝗛𝗢𝗨𝗧 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗𝗜𝗡𝗚 𝗜𝗧!</b></n>"
        "<b>𝗠𝗔𝗗𝗘 𝗕𝗬 :- @GUARDIANff</b></n>",
       await message.reply_photo(photo=START_PIC,
                                caption=text,
        reply_markup=types.InlineKeyboardMarkup([[
        types.InlineKeyboardButton("🛠️ 𝗗𝗘𝗩 🛠️", url='https://t.me/GUARDIANff')
        ],[
        types.InlineKeyboardButton('𝗨𝗣𝗗𝗔𝗧𝗘𝗦', url='https://t.me/AM_FILMS'),
        types.InlineKeyboardButton('𝗦𝗨𝗣𝗣𝗢𝗥𝗧', url='https://t.me/+sSWbe8vjU2s1ZTRl'),
        ],[
        types.InlineKeyboardButton("𝗕𝗢𝗧 𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦",
                                      callback_data="showSettings")]]))
    )

@Client.on_message(filters.command("help") & filters.private)
async def help_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="<b>𝙸 𝙲𝙰𝙽 𝚁𝙴𝙽𝙰𝙼𝙴 𝙼𝙴𝙳𝙸𝙰 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙸𝚃!</b>\n"
             "<b>𝚂𝙿𝙴𝙴𝙳 𝙳𝙴𝙿𝙴𝙽𝙳𝚂 𝙾𝙽 𝚈𝙾𝚄𝚁 𝙼𝙴𝙳𝙸𝙰 𝙳𝙲.</b>\n\n"
             "<b>𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝙼𝙴 𝙼𝙴𝙳𝙸𝙰 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝙸𝚃 𝚆𝙸𝚃𝙷 /rename 𝙲𝙾𝙼𝙼𝙰𝙽𝙳.</b>\n\n"
             "<b>𝚃𝙾 𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰𝙽𝚈 𝙸𝙼𝙰𝙶𝙴 𝚆𝙸𝚃𝙷 /set_thumbnail</b>\n\n"
             "<b>𝚃𝙾 𝚂𝙴𝙴 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝙿𝚁𝙴𝚂𝚂 /show_thumbnail</b>",
        reply_markup=types.InlineKeyboardMarkup([[
           types.InlineKeyboardButton("𝗕𝗢𝗧 𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦",
                                      callback_data="showSettings")]])
    )

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config


@app.on_message(
    command(["مطور", "مبرمج السورس", "نور"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/3955f6d7c023440c11156.jpg",
        caption="• Dev Bot ↦ المطور \n ━━━━━━━━━━━━ \n • Dev ↦  Cr SoUrce . \n • Bio ↦ ˛ ╭──── • ◈ • ────╮

么• My Official Channel 💚
么• I post here Source & New Updates 💖
么• My official account Dev¹ : @nor_o  🖤
么• My official account Dev² : @O_F_4 🤍

╰──── • ◈ • ────╯
.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙲𝚁 𝙽𝙾𝚄𝚁", url=f"https://t.me/nor_o"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Updates", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )

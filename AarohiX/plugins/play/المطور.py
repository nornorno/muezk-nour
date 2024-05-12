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
        caption="• Dev Bot ↦ المطور نور الحاكم \n ━━━━━━━━━━━━ \n • Dev ↦ { nor_o.t.me }{ o_f_4.t.me } Cr SoUrce . \n • Bio ↦𝗘𝗩𝗘 #𝗥𝗬𝗧𝗛𝗜𝗡𝗚 𝗧𝗛𝗜𝗦 #𝗔𝗖𝗖𝗢𝗨𝗡𝗧 { noordot.t.me } { @O_F_4 }{ sahnks.t.me }{ vza_o.t.me } { h_n_y_o.t.me }{ vzo_a.t.me }{ mssna_1bot.t.me }{ noonelhakem_123bot.t.me }{ cr_co_bot.t.me }",
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

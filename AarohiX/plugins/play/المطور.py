from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config


@app.on_message(
    command(["مطور", "مبرمج السورس", "زيكا"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/77bd924e46880da2b8d38.jpg",
        caption="• Dev Bot ↦ αℓτυяĸy \n ━━━━━━━━━━━━ \n • Dev ↦ Cr SoUrce: αℓτυяĸy . \n • Bio ↦- 𓏺 Whoever humbles #himself to god will be #exalted 𓏺",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "αℓτυяĸy", url=f"https://t.me/X_II_H"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Updates", url=f"https://t.me/xx6uxx"
                    ),
                ],
            ]
        ),
    )

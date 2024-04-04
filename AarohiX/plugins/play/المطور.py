from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config


@app.on_message(
    command(["مطور السورس", "مبرمج السورس", "المطور"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/3955f6d7c023440c11156.jpg",
        caption="• Dev Bot ↦ سهيله \n ━━━━━━━━━━━━ \n • Dev ↦  Ahmed Teto . \n • Bio ↦ أستغفر الله الذي لا إله إلا هو الحي القيوم، وأتوب إليه . @T_S_T4",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Ahmed Teto", url=f"tg://openmessage?user_id={config.OWNER_ID}"
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

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config


@app.on_message(filters.command(["مح"], ""))
async def maker(client: Client, message: Message):
    await message.reply_animation(
        animation="https://telegra.ph/file/83e7bdf0e2dad83402160.mp4",
        caption="القميل هذا  ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المقبول 🫧", url=f"tg://openmessage?user_id={message.from_user.mention}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "القـابل 🤭", url=f"t.me/t7_au"
                    ),
                ],
            ]
        ),
    )

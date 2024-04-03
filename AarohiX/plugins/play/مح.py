from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config


@app.on_message(
    command(["مح"])
)
async def maker(client: Client, message: Message):
    await message.reply_video(
        video="https://telegra.ph/file/83e7bdf0e2dad83402160.mp4",
        caption="-القميل هذا  ❲ {0} ❳ 🫧\n- بعتلك بوسه يا  ❲ {message.reply_to_message.from_user.mention} ❳ \n عيب كده اي المحن ده 🤭",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المقبول 🫧", url=f""
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "القـابل 🤭", url=""
                    ),
                ],
            ]
        ),
    )

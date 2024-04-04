from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config
from pyrogram.errors import FloodWait



@app.on_message(filters.command(["مح"], ""))
async def maker(client: Client, message: Message):
     await message.reply_video(
        video="https://telegra.ph/file/83e7bdf0e2dad83402160.mp4",
        caption="•القميل هذا ✨♥ \n※ بعتلك بوسه يا 😘♥ @ \nعيب كده اي المحن ده 😹",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton(
                        user.mention,
                        "المقبول 🫧", url=f"https://t.me/{user.mention}"
                    ),
                ],
                [
                     InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

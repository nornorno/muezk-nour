from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config
from pyrogram.errors import FloodWait




@app.on_message(filters.command(["بوت حذف","رابط الحذف","حذف حساب","عاوز احذف"], ""))
async def maker(client: Client, message: Message):
     await message.reply_video(
        video="https://telegra.ph/file/06b0d6f4227097d519aa8.mp4",
        caption="◍ مع السـلامه اراك لاحقـا 🥀 ❲ [اطغط هنا](https://t.me/LC6BOT) ❳",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

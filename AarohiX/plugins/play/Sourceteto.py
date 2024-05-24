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
        caption=f"""˛ ❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰▰
么 [𝚂𝙾𝚄𝚁𝙲𝙴:Dev¹:](https://t.me/nor_o)
么 [𝚂𝙾𝚄𝚁𝙲𝙴:Dev²:](https://t.me/N_7_K)
么 [𝚂𝙾𝚄𝚁𝙲𝙴:Dev³:](https://t.me/KeRo_7x)
么 [𝚂𝙾𝚄𝚁𝙲𝙴:Dev⁴:](https://t.me/A_c_o_i)
么 [𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝚌𝚑𝚊𝚗𝚗𝚎¹](https://t.me/vzo_a)
么 [Support group²](https://t.me/cr_nox)
▰▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مطور السورس", url=f"https://t.me/nor_o"), 
                 ],[
                   InlineKeyboardButton(
                        "𝚂𝙾𝚄𝚁𝙲𝙴:αℓτυяĸy", url=f"https://t.me/vzo_a"),
                ],[
                  InlineKeyboardButton(
                        "مطور السورس", url=f"https://t.me/nor_o"),
              ],
        ),

    )
    

import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from AarohiX import app
from random import  choice, randint

@app.on_message(filters.command(["مح"], ""))
async def maker(client: Client, message: Message):
    await message.reply_video(
        video="https://telegra.ph/file/83e7bdf0e2dad83402160.mp4",
        caption="-القميل هذا  @{message.from_user.mention} 🫧\n- بعتلك بوسه يا  ❲  ❳ \n عيب كده اي المحن ده 🤭",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المقبول 🫧", url=f"t.me/t7_au"
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

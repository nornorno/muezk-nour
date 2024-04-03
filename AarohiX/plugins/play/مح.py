import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from asyncio import gather
from pyrogram.errors import FloodWait



@app.on_message(filters.command(["مح"], ""))
async def maker(client: Client, message: Message):
    await message.reply_video(
        video="https://telegra.ph/file/83e7bdf0e2dad83402160.mp4",
        caption="القميل هذا tg://openmessage?user_id={message.from_user.mention} ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المقبول 🫧", url=f""
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
    

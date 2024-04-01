import asyncio
import os
import time
import requests
import aiohttp
from config import START_IMG_URL
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from asyncio import gather
from pyrogram.errors import FloodWait





@app.on_message(
    filters.command(["مميزات","مميزات تيتو"], "")
& filters.group
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**⦿ قايمه مميزات سورس تيتو :\n
╮⦿  المطور
│᚜⦿ سؤال
│᚜⦿ مين في الكول 
│᚜⦿ تفعيل الاذان
│᚜⦿ كت
│᚜⦿ احكام
│᚜⦿ افتح الكول
│᚜⦿ احرف
│᚜⦿ الرابط
│᚜⦿ البنك 
│᚜⦿ منع تصفيه تلقائي
│᚜⦿ رفع مشرف
│᚜⦿ شعر
│᚜⦿ نادي المطور
│᚜⦿ زخرفه
│᚜⦿ مميزات
│᚜⦿ همسه
│᚜⦿ يوت
│᚜⦿ تحميل
│᚜⦿ لو خيروك
│᚜⦿ معلومات الجروب
│᚜⦿ طرد كتم
│᚜⦿ تلكراف ميديا
│᚜⦿ اسكرين 
│᚜⦿ صراحه
│᚜⦿ صور
│᚜⦿ صور بنات 
│᚜⦿ صور شباب
│᚜⦿ السورس 
│᚜⦿ كتم
│᚜⦿ اقتباس
│᚜⦿ هيدرات
│᚜⦿ اذكار 
╯⦿  بث مباشر للقنوات 
[𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝘁𝗼](https://t.me/WX_PM) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴛᴇᴛσ", url=f"https://t.me/WZAERE"),                        
                 ],[
                InlineKeyboardButton(
                        "close", callback_data="close"),
               ],
          ]
        ),
    )


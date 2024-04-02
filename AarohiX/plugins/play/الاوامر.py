import asyncio
import os
from pyrogram.types import CallbackQuery
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    command("الاوامر")
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
      photo=f"https://telegra.ph/file/c9546322d3e3ad7abd8f1.jpg",
        caption=f"""• اهلا بك في قائمه الاوامر التابعه لـ [𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝘁𝗼](https://t.me/wx_pm)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامـر الكـروبات ❄️", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامـر القنـوات 🥀", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "المـميزات 🫧", callback_data="yyy"), 
                 ],[
                    InlineKeyboardButton(
                        "اوامـر الالعاب 🚦", callback_data="adm"), 
                InlineKeyboardButton(
                        "اوامـر اضافية", callback_data="hmd"), 
                 ],[       
                       
                    InlineKeyboardButton(
                        "𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝘁𝗼›", url=f"https://t.me/WX_PM"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("gr"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**╮⦿ اوامـر الكـروبات ❄️
│᚜⦿ كتم / طرد
│᚜⦿ قفل الملصات
│᚜⦿ الادمنيه
╯⦿  زخرفه**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ التالي ›", callback_data="ch"), 
                    
                ],[
                    InlineKeyboardButton(
                        "‹ الرئيسية ›", callback_data="الاوامر"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("ch"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**-  اوامر التفعيل اتبع مايلي
 — — — — — — — — — —

‹ طريقه تفعيل البوت في الكروبات والقنوات ⤈ ›

‹ Gr1 › 
 اضف البوت مع كامل الصلاحيات عدا البقاء متخفي 

‹ Gr2 › : 
افتح اتصال في المجموعة او القناة 

‹ Gr2 › :  
اكتب تشغيل + اسم الأغنية 

 - سيتم انضمام الحساب المساعد الى المحادثة الصوتية وتشغيل الاغنية التي اردتها .
- الحساب المساعد عبارة عن حساب وهمي وضيفته فقط تشغيل الموسيقى 

- لاتقم بطرده او حضره اثناء تشغيل الموسيقى يمكنك استخدام الامر

- __ايقاف__ لانهاء تشغيل المقطع الصوتي وخروج الحساب المساعد دون مشاكل**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ التالي ›", callback_data="adm"), 
                    InlineKeyboardButton(
                        "‹ رجوع ›", callback_data="gr"), 
                ],[
                    InlineKeyboardButton(
                        "‹ الرئيسية ›", callback_data="الاوامر"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("adm"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**- قائمة الالعاب هي : ↶
— — — — — — — — — — — — — —

- العكس ↫ لعبة عكس الكلمات 

- امثله ↫ لعبة امثله مسليه

- لو خيروك ↫ لعبة لو خيروك

- كلمات ↫ لعبة كلمات 

- صراحه ↫ لعبة صراحه

- نشط عقلك ↫ لعبة اسئلة عامة

— — — — — — — — — — — — —""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ التالي ›", callback_data="hmd"), 
                    InlineKeyboardButton(
                        "‹ رجوع ›", callback_data="ch"), 
                ],[
                    InlineKeyboardButton(
                        "‹ الرئيسية ›", callback_data="الاوامر"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("hmd"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**-  اوامر التسليه
 — — — — — — — — — — 
- ( غنيلي ) يرسل لك اغنية عشوائية

- ( فيلم ) فيلم كامل عشوائي

- ( متحركة ) متحركات عشوائيه مميزة

- ( اقتباسات ) اقتباس بالصورة جميل

- ( اسمي ) لعرض اسمك الكامل

- ( ا ) لعرض معلوماتك

- ( all ) لعمل تاك جماعي في المجموعه

— — — — — — — — — — — — — —**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ التالي ›", callback_data="gr"), 
                    InlineKeyboardButton(
                        "‹ رجوع ›", callback_data="adm"), 
                ],[
                    InlineKeyboardButton(
                        "‹ الرئيسية ›", callback_data="الاوامر"), 
                    
                ]
            ]
        )
    )
  

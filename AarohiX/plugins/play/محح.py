import asyncio


import random


from AarohiX import app


from pyrogram.types import (InlineKeyboardButton,


                            InlineKeyboardMarkup, Message)


from pyrogram import filters, Client





@app.on_message(
    filters.command(["مح"], "")
& filters.group
 )
async def mmmezat(client, message):
        await message.reply_video"""https://telegra.ph/file/83e7bdf0e2dad83402160.mp4""",
        caption="•القميل هذا ✨♥ https://t.me/{message.from_user.username} \n※ بعتلك بوسه يا 😘♥ @ \nعيب كده اي المحن ده 😹",
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


import asyncio
import datetime
from AarohiX import app
from pyrogram import Client
from AarohiX.utils.database import get_served_chats
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


MESSAGE = f"افضل بوت ميوزك قنوات و جروبات بدون تهنيج ❄.\n- ميزه تفعيل الاذان ، كت تويت ، اوامر حمايه\nارفع البوت ادمن فقناتك او جروبك واستمتع بجوده الصوت و السرعه الخياليه للبوت ❄\n معرف البوت  [ @UUIYBOT ] \n➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵𝘴 ♩🎸\n◍ 𝙱𝙾𝚃 ➤ @UUIYBOT\n◍ 𝙳𝙴𝚅 ➤ @WZAERE"

🏮 ʙᴏᴛ »|| @{app.username}||"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ضيـف البوت لمجموعتـك ✅", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)
                except Exception as e:
                    pass  
    except Exception as e:
        pass  

async def continuous_broadcast():
    while True:
        await send_message_to_chats()
        await asyncio.sleep(50000)  
        
asyncio.create_task(continuous_broadcast())

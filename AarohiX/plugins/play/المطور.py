from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config


@app.on_message(
    command(["مطور", "مبرمج السورس", "نور"])
)
async def maker(client: Client, message: Message):
    await message.reply_video(
        video="https://telegra.ph/file/06ea0dffac061d340b30a.mp4",
        caption="• 𝐃𝐞𝐯 𝐁𝐨𝐭: ↦ مــيوزك العـالم \n ━━━━━━━━━━━━ \n • 𝐃𝐞𝐯: ↦ Cr SoUrce:nour . \n • 𝐁𝐢𝐨 ↦- 𓏺 Whoever humbles #himself to god will be #exalted 𓏺",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✧❅مطـورالسـورس✧❅", url=f"https://t.me/nor_o"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Updates", url=f"https://t.me/vzo_a"
                    ),
                ],
            ]
        ),
    )

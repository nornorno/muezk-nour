import asyncio
from pyrogram.enums import ChatType, ChatMemberStatus
from AarohiX import app
from pyrogram import filters
from AarohiX.utils.admin_check import admin_filter


@app.on_message(filters.command(["مح"], ""))
async def maker(client: Client, message: Message):
    await message.reply_video(
        video="https://telegra.ph/file/83e7bdf0e2dad83402160.mp4",
        caption="القميل هذا [{m.user.first_name}](tg://user?id={m.user.id}) ",
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

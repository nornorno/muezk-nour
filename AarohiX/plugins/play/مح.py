from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config


@app.on_message(
    command(["مح"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/83e7bdf0e2dad83402160.mp4",
        caption="※ هذا القميل {message.from_user.mention} \n※ بعتلك بوسه يا 😘♥ [{user.first_name}](tg://user?id={user.id})\n عيب كده اي المحن ده 😹",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المقبول 🤭", url=f"[{user.first_name}](tg://user?id={user.id})"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "القابل", url=f"{message.from_user.mention}"
                    ),
                ],
            ]
        ),
    )

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Aarohix import app
from config import BOT_USERNAME
from Aarohix.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
اهلا بيك في قائمه البوتات المهمه بالتليجرام 🏮. 
**"""




@app.on_message(filters.command("بوتاتي"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ضيف البوت لمجموعتك ✅.", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("بوت تلكراف ميديا", url="https://t.me/Soeirusbot"),
          InlineKeyboardButton("بوت مانع الروابط", url="https://t.me/Bloc_klinkBot"),
          ],
               [
                InlineKeyboardButton("بوت تلاوت", url="https://t.me/tlawtbot"),

],
[
              InlineKeyboardButton("بوت تنزيل من تيكتوك", url=f"https://t.me/TikDownloadedBot"),
              InlineKeyboardButton("︎بوت ميوزك", url=f"https://t.me/UUIYBOT"),
              ],
              [
              InlineKeyboardButton("اختراق جلسات", url=f"https://t.me/uuou0bot"),
InlineKeyboardButton("استخراج جلسات", url=f"https://t.me/al11ibot"),
],
[
InlineKeyboardButton("بوت نقل اعضاء", url=f"https://t.me/sku0bot"),
InlineKeyboardButton("سورس تيتو", url=f"https://t.me/WX_PM"),
],
[
              InlineKeyboardButton("بوت تمويل", url=f"https://t.me/ZDD7bot"),
              InlineKeyboardButton("تحميل من يوتيوب", url=f"https://t.me/yt7_ybot"),
              ],
              [
              InlineKeyboardButton("صانع استيكرات", url=f"https://t.me/stickers7x_bot"),
InlineKeyboardButton("صانع بوتات", url=f"https://t.me/market_7bot"),
],
[
InlineKeyboardButton("بوت زخرفه", url=f"https://t.me/zhrafatbot"),
InlineKeyboardButton("بوت سمسمي", url=f"https://t.me/xxma_bot"),
],
[
InlineKeyboardButton("مـطور البوتات", url=f"https://t.me/G_7_Rr"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/cf3ae85a39109bfbf4109.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/DAXXTEAM/DAXXMUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/DAXXTEAM/DAXXMUSIC) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/HEROKUFREECC)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")



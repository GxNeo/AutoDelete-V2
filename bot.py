import asyncio
from datetime import datetime, date
import pytz
import time
from os import environ
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters, idle

NEEK = """
<i><b>Group‌ message will be automatically deleted after 15 minutes due to copyright issue.</b></i>

<i><b>⚜ Powered by @CinimaBranthen</b></i>
   
   """
#######
BOT_START_TIME = time.time()
########
API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
#SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))
GROUPS = []
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))

tz = pytz.timezone("Asia/Kolkata")   
now = datetime.now(tz)
#teek = time.time()
uptime = time.strftime("%W Week | %d Day | %H hour| %M Min | %S Sec", time.gmtime(time.time() - BOT_START_TIME))
tme = now.strftime("%H:%M:%S %p")
date = now.strftime("%d-%m-%-Y")
day = now.strftime("%A")


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "nekodate":
        await query.answer(f"""👋🏻 Hello {query.from_user.first_name}
        
📅 Date : {date}
⛅️ Day : {day}
🌇 UTC : +0530

© CinimaBranthen
""", show_alert=True)
    elif query.data == "nekotime":
        await query.answer(f"""👋 Hello {query.from_user.first_name}
        
⏰️ Time : {tme}
⚡️ Zone : Asia/Kolkata
⌛️ Uptime : {uptime}

© CinimaBranthen
        """, show_alert=True)
         
@Bot.on_message(filters.command('start') & filters.private & filters.user(ADMINS))
async def start(bot, message):
    await message.delete()
 
@Bot.on_message((filters.private | filters.group) & filters.command('neek'))
async def start(client, message):
    await message.reply_text(
        text=NEEK,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⏰️ ᴛɪᴍᴇ", callback_data="nekotime"),
                    InlineKeyboardButton("📆 ᴅᴀᴛᴇ", callback_data="nekodate")
                ]
                
            ]
        ),
        quote=True
        )

@Bot.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
#User.start()
#print("User Started!")
Bot.start()
print("Bot Started!")

idle()

#User.stop()
#print("User Stopped!")
Bot.stop()
print("Bot Stopped!")

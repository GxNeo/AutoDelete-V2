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
SESSION = environ.get("SESSION",'BQAJTNEuOQSe7ju0LqMlTcI-YILs1rE0Bd4IF8iorGwW6x0TJeMqb6oiiTy_8jmqSqDTUzSlodDAVqV_0Lu5guNsfYGeBeItDyMcqVCOrpOfECsh2zmbde5HErF4nf_GvlMRUSfC_Q8AMkbzI9mnjpzWvcKMbRogqQjQTU3Zoi6Mhcg47Tq_9H0yrmU21fzUr3IhbWF9DF8-inO0De6RYhd_J_KPKZHlFMmLEwl3gyOBNYfoysvcOC8cEoMzu3dVkNuVjqi8dsg2doDnhiYVZBiLEDPx_crtcOh6lwmeu-Yvn3IiA7f9_PsGdSMfBTwrwAVIJ2uYb5dHDU_G2OAzjapJccJeTwA')
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
#fcuk = datetime.month_name(locale = 'English')
#teek = time.time()
uptime = time.strftime("%W Week | %d Day | %H hour | %M Min | %S Sec", time.gmtime(time.time() - BOT_START_TIME))
tme = now.strftime("%H:%M:%S %p")
date = now.strftime(f"%d-{fcuk}-%-Y")
day = now.strftime("%A")


User = Client(session_name=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(session_name="auto-delete",
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

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")

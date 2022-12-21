import asyncio
from os import environ
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters, idle

NEEK = """<b>Group‌ message will be automatically deleted after 15 minutes due to copyright issue.</b>
    
<b>⚜ Powered by @CinimaBranthen</b>"""

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
    
    



Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


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
                    InlineKeyboardButton("How to Deploy?", url="https://youtu.be/hkmc3e7U7R4"),
                    InlineKeyboardButton("About Me", callback_data="about_data")
                ]
                
            ],
        ),
        reply_to_message_id=message.message_id
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

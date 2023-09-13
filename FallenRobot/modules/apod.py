import requests
from FallenRobot import pbot
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , CallbackQuery , Message

@pbot.on_message(filters.command("apod"), group=977)
async def genshin_character(_: Client, message: Message):
    m= await message.reply_text("Fetching Info....", parse_mode=ParseMode.MARKDOWN)
    response = requests.get(f"https://api.safone.me/astronomy")
    if response.status_code == 200:
        data = response.json()
        a= data["date"]
        link= data["link"]
       
        c = data ["imageUrl"]
        d = data ["title"]

        photo = f"{c}"
        
        genshin_char = f"""

<b>🔭Title:</b> {d}

<b>📅Date:</b> {a}

<b>📎Link:</b>  {link}      

            """

    await message.reply_photo (photo , caption= genshin_char, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("More Info", callback_data = "apod")]]))

@pbot.on_callback_query(group=298)
async def features(_: Client, query: CallbackQuery):
    data = query.data
    if data == "apod":
       response = requests.get(f"https://api.safone.me/astronomy")
       if response.status_code == 200:
         data = response.json()
         exp= data["explanation"]
         calltext = f''' {exp}'''
    await query.message.edit_text(
           text = f''' {calltext}''',
           disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Website", url = "https://apod.nasa.gov/apod/")
                    ]
                ]
            )
                                            )


__mod_name__ = "Apod"

__help__ = """

eg. /apod 

 """




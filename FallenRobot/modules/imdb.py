import asyncio
import requests
from Himawari import pgram as pbot
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , CallbackQuery , Message


@pbot.on_message(filters.command("imdb"), group=977)
async def genshin_character(_: Client, message: Message):
    text = "".join(message.text.split(" ")[1:])
    if len(text) == 0:
        return await message.reply_text(
            "Cannot reply to empty message.", parse_mode=ParseMode.MARKDOWN
        )

    m= await message.reply_text("Gathering Infromation....", parse_mode=ParseMode.MARKDOWN)
    response = requests.get(f"https://api.safone.dev/imdb?query={text}&limit=1" )
    if response.status_code == 200:
        data = response.json()
        data_ph = response.json()['results']
        data_r = response.json()['results'][0]['rating']
        data_da = response.json()['results'][0]['releaseDetailed']
        
        
        imx = data_ph[0]['poster']
        
        
        rating = data_r['star']
        plot = data_ph[0]['plot']
        genre = data_ph[0]['genre']
        actors = data_ph[0]['actors']
        directors = data_ph[0]['directors']
        run_time =  data_ph[0]['runtime']
        day =  data_da['day']
        month =  data_da['month']
        year = data_ph[0]['year']

        photo = imx
        genshin_char = f"""

**Duration:** {run_time}      
**Plot :**{plot}
**Genre:** {genre}
**Rating:** {rating}
**Actors:** {actors}
**Directors:** {directors}
**Relese Date:** {day}/{month}/{year}

            """
    await message.reply_photo (photo , caption= genshin_char, parse_mode=ParseMode.MARKDOWN )
    await m.delete()

__help__ = """
  
**Usage:**
    
- `/imdb movie name` *:* Get info about any movie 
    """
__mod_name__ = "Imdb"

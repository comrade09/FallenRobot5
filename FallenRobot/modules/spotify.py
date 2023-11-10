import asyncio
import requests
from FallenRobot import pbot
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , CallbackQuery , Message


@pbot.on_message(filters.command("spotify"), group=466)
async def genshin_character(_: Client, message: Message):
    text = "".join(message.text.split(" ")[1:])
    if len(text) == 0:
        return await message.reply_text(
            "Cannot reply to empty message.", parse_mode=ParseMode.MARKDOWN
        )

    m= await message.reply_text("Gathering Infromation....", parse_mode=ParseMode.MARKDOWN)
    response = requests.get(f"https://api.safone.dev/spotify?query={text}&limit=1" )
    if response.status_code == 200:
        data = response.json()
        data_ph = response.json()['results']
        
        
        
        
        imx = data_ph[0]['imageUrl']
        
        
        rating = data_ph[0]['popularity']
        date = data_ph[0]['releaseDate']
        link = data_ph[0]['songUrl']
        title = data_ph[0]['title']
        artist = data_ph[0]['artist']
        duration = data_ph[0]['duration']
        genre = data_ph[0]['genres']
       

        photo = imx
        genshin_char = f"""

**Song** {title}  
**Duration:** {duration}  
**Song Link:**[Click Here](f"{link}"),  
**Artist :**{artist}
**Genre:** {genre}
**Rating:** {rating}
**Realese:** {date}


            """
    await message.reply_photo (photo , caption= genshin_char, parse_mode=ParseMode.MARKDOWN )
    await m.delete()
__help__ = """
  
**Usage:**
    
- `/spotify song name` *:* Get info about any song
- `/lyrics song name` *:* Get lyrics of songs
    """
__mod_name__ = "Song"

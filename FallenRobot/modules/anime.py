import asyncio
import requests
from FallenRobot import  pbot
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , CallbackQuery , Message
  
def shorten(description):
    msg = ""
    if len(description) > 200:
        description = description[0:200] + "..."
        msg += f"{description}"
    else:
        msg += f"{description}"
    return msg
 
@pbot.on_message(filters.command("character"), group=977)
async def genshin_character(_: Client, message: Message):
    text = "".join(message.text.split(" ")[1:])
    if len(text) == 0:
        return await message.reply_text(
            "Cannot reply to empty message.", parse_mode=ParseMode.MARKDOWN
        )

    m= await message.reply_text("Gathering Infromation....", parse_mode=ParseMode.MARKDOWN)
    response = requests.get("https://api.safone.dev/anime/character?query=" + text)
    if response.status_code == 200:
        data = response.json()
        data_ph = response.json()['image']
        imx = data_ph ['medium']
        desc = data ['description']
        mxg = shorten(desc)
        gender = data ['gender']
        height = data ['height']
        age = data ['age']
        photo = imx
        genshin_char = f"""

**Age:** {age}      
**Description :**{mxg}
**Height:** {height} 
**Gender:** {gender} 

            """
    await message.reply_photo (photo , caption= genshin_char, parse_mode=ParseMode.MARKDOWN )


@bot.on_message(filters.command("manga"), group=977)
async def genshin_character(_: Client, message: Message):
    text = "".join(message.text.split(" ")[1:])
    if len(text) == 0:
        return await message.reply_text(
            "Cannot reply to empty message.", parse_mode=ParseMode.MARKDOWN
        )

    m= await message.reply_text("Gathering Infromation....", parse_mode=ParseMode.MARKDOWN)
    response = requests.get("https://api.safone.dev/anime/manga?query=" + text)
    if response.status_code == 200:
        data = response.json()
        data_end = response.json()['endDate']
        data_st = response.json()['startDate']
        data_t = response.json()['title']
        imx = data ['imageUrl']
        desc = data ['description']
        mxg = shorten(desc)
        avg = data ['averageScore']
        chp = data ['chapters']
        eday = data_end ['day']
        emonth = data_end ['month']  
        eyear = data_end ['year']
        sday = data_st ['day']
        smonth = data_st ['month']  
        syear = data_st ['year']
        status = data ['status']
        title =  data_t ['english']
        photo_manga = imx
        genres = data ['genres']
        gen_char = f"""

**Title:** {title}
**Total Chapters:** {chp}
**Start Date:** {eday}/{emonth}/{eyear}
**End Date:** {sday}/{smonth}/{syear}
**Status:** {status}
**Avg Score:** {avg}      
**Description :**{mxg}
**Genres:** {genres} 

"""

    await message.reply_photo(photo=photo_manga, caption= gen_char, parse_mode=ParseMode.MARKDOWN )

@bot.on_message(filters.command("anime"), group=977)
async def genshin_character(_: Client, message: Message):
    text = "".join(message.text.split(" ")[1:])
    if len(text) == 0:
        return await message.reply_text(
            "Cannot reply to empty message.", parse_mode=ParseMode.MARKDOWN
        )

    mk= await message.reply_text("Gathering Infromation....", parse_mode=ParseMode.MARKDOWN)
    response = requests.get("https://api.safone.dev/anime/search?query=" + text)
    if response.status_code == 200:
        data = response.json()
        data_end = response.json()['endDate']
        data_st = response.json()['startDate']
        data_t = response.json()['title']
        imx = data ['imageUrl']
        desc = data ['description']
        mxg = shorten(desc)
        avg = data ['averageScore']
        ep = data ['episodes']
        sea = data ['season']
        studios = data ['studios']
        eday = data_end ['day']
        emonth = data_end ['month']  
        eyear = data_end ['year']
        sday = data_st ['day']
        smonth = data_st ['month']  
        syear = data_st ['year']
        status = data ['status']
        title =  data_t ['english']
        photo_sr = imx
        genres = data ['genres']
        sr_char = f"""

**Title:** {title}
**Total Episodes:** {ep}
**Start Date:** {eday}/{emonth}/{eyear}
**End Date:** {sday}/{smonth}/{syear}
**Status:** {status}
**Title:** {sea}
**Title:** {studios}
**Avg Score:** {avg}      
**Description :**{mxg}
**Genres:** {genres} 

"""

    await message.reply_photo(photo=photo_sr, caption= sr_char, parse_mode=ParseMode.MARKDOWN )
    await mk.delete()
__mod_name__ = "Anime"

__help__ = """

Command '/gicharacter'
eg. /gicharacter Amber

 """



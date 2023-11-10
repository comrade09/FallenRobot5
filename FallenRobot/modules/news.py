import requests
import random
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums import ParseMode 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , CallbackQuery , Message
from FallenRobot import pbot

API_URL = "https://api.safone.dev/news{}"
ANIME_URL = "https://api.safone.dev/anime/news{}"

@pbot.on_message(filters.command("news"))
async def news(_, message: Message):
    keyword = (
        message.text.split(" ", 1)[1].strip() if len(message.text.split()) > 1 else ""
    )
    url = API_URL.format(keyword)

    try:
        response = requests.get(url)
        news_data = response.json()['results']

        if "error" in news_data:
            error_message = news_data["error"]
            await message.reply_text(f"Error: {error_message}")
        else:
            if len(news_data) > 0:
                news_item = random.choice(news_data)

                author = news_item["author"]
                time = news_item ["time"]
                title = news_item["title"]
                date = news_item["date"]
                description = news_item["description"]
                
                nurl = news_item["link"]
                image = news_item["imageUrl"]

                message_text = f"<b>📰TITLE</b>: {title}\n\n<b>📄AUTHOR</b>: {author}\n\n<b>📅DATE & TIME</b>: {date} {time}\n\n<b>📃DESCRIPTION</b>: `{description}`\n\n📂READ MORE : {nurl} "
                photo =f"{image}"

                await message.reply_photo(photo,caption = message_text)
            else:
                await message.reply_text("No news found.")

    except requests.exceptions.RequestException as e:
        await message.reply_text(f"Error: {str(e)}")

@pbot.on_message(filters.command("animenews"))
async def aninews(_, message: Message):
    anikeyword = (
        message.text.split(" ", 1)[1].strip() if len(message.text.split()) > 1 else ""
    )
    url = ANIME_URL.format(anikeyword)

    try:
        response = requests.get(url)
        aninews_data = response.json()['results']

        if "error" in aninews_data:
            error_message = aninews_data["error"]
            await message.reply_text(f"Error: {error_message}")
        else:
            if len(aninews_data) > 0:
                aninews_item = random.choice(aninews_data)
                title = aninews_item["title"]
                description = aninews_item["description"]
                nurl = aninews_item["link"]
                image = aninews_item["imageUrl"]

                animessage_text = f"<b>📰TITLE</b>: {title}\n\n<b>📃DESCRIPTION</b>: `{description}`\n\n📂READ MORE : {nurl} "
                aniphoto =f"{image}"

                await message.reply_photo(aniphoto,caption = animessage_text)
            else:
                await message.reply_text("No news found.")

    except requests.exceptions.RequestException as e:
        await message.reply_text(f"Error: {str(e)}")


__help__ = """
    
Get your news  by using this module
    
**Usage:**
    
- /news  Get today breaking news
- /animenews Get anime news
  

    
    """
__mod_name__ = "News"

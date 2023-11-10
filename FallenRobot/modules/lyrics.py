import requests
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums import ParseMode 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , CallbackQuery 
from ShinobuRobot import pbot


@pbot.on_message(filters.command("lyrics"), group=469)
async def chatbot(_: Client, message: Message):
    text = "".join(message.text.split(" ")[1:])
    if len(text) == 0:
        return await message.reply_text(
            "Cannot reply to empty message.", parse_mode=ParseMode.MARKDOWN
        )

    m= await message.reply_text("Please wait 1 min ....", parse_mode=ParseMode.MARKDOWN)
    response = requests.get(f"https://api.safone.dev/lyrics?query={text}")
    if response.status_code == 200:
        news_item= response.json()
        author = news_item["artist"]
        titl = news_item["title"]
        date = news_item["releaseDate"]
        description = news_item["lyrics"]
        nurl = news_item["link"]
        image = news_item["thumbnail"]

    message_text = f"<b>🎵SONG NAME</b>: {titl}\n\n<b>🎤ARTIST</b>: {author}\n\n<b>📅DATE & TIME</b>: {date} \n\n<b>📃LYRICS</b>: `{description}`\n\n📂More : {nurl} "
    photo =f"{image}"

    await message.reply_text(message_text)

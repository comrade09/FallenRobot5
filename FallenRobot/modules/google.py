import requests
from Himawari import pgram as pbot
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums import ParseMode


@pbot.on_message(filters.command("google"), group=434)
async def chatbot(_: Client, message: Message):
    text = "".join(message.text.split(" ")[1:])
    if len(text) == 0:
        return await message.reply_text(
            "Cannot reply to empty message.", parse_mode=ParseMode.MARKDOWN
        )

    m = await message.reply_text("Getting Request....", parse_mode=ParseMode.MARKDOWN)
    response = requests.get("https://sugoi-api.vercel.app/search?keyword=" + text)
    if response.status_code == 200:
        data = response.json()
        reply = ""
        for i in range(3):
            title = data[i]["title"]
            desc = data[i]["desc"]
            link = data[i]["link"]
            reply += f"""
<b>{title}</b>
URL: {link}
<i>{desc}</i>\n
            """
        return await m.edit_text(
            reply, parse_mode=ParseMode.HTML, disable_web_page_preview=True
        )

    elif response.status_code == 429:
        return await m.edit_text(
            "ChatBot Error: Too many requests. Please wait a few moments."
        )
    elif response.status_code >= 500:
        return await m.edit_text(
            "ChatBot Error: API server error. Contact us at @tyranteyeeee."
        )
    else:
        return await m.edit_text(
            "ChatBot Error: Unknown Error Occurred. Contact us at @tyranteyeeee."
        )

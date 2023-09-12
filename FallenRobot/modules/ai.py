import requests
from FallenRobot import pbot
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , CallbackQuery
import io


@pbot.on_message(filters.command("bard"), group =77 )
async def chatbot(_: Client, message: Message):
    text = "".join(message.text.split(" ")[1:])
    if len(text) == 0:
        return await message.reply_text("Cannot reply to empty message.", parse_mode=ParseMode.MARKDOWN)
        

    m = await message.reply_text("Getting Request....", parse_mode=ParseMode.MARKDOWN)
    response = requests.get(
        "https://sugoi-api.vercel.app/bard?msg="
        + text
        + "&user_id="
        + str(message.from_user.id)
    )
    if response.status_code == 200:
        data = response.json()
        if len(data) <= 1024:
            return await m.edit_text(data, parse_mode=ParseMode.MARKDOWN)
        else:
            file_data = io.BytesIO(data.encode())
            file_data.name = "response.txt"
            await message.reply_document(file_data)
            return await m.delete()
    elif response.status_code == 429:
        return await m.edit_text("ChatBot Error: Too many requests. Please wait a few moments.")
    elif response.status_code >= 500:
        return await m.edit_text("ChatBot Error: API server error. Contact us at @Zen_Network.")
    else:
        return await m.edit_text("ChatBot Error: Unknown Error Occurred. Contact us at @Zen_Network.")
    
@pbot.on_message(filters.command("asksaf"), group=987)
async def chatbot(_: Client, message: Message):
    text = "".join(message.text.split(" ")[1:])
    if len(text) == 0:
        return await message.reply_text(
            "Cannot reply to empty message.", parse_mode=ParseMode.MARKDOWN
        )

    m= await message.reply_text("Answering....", parse_mode=ParseMode.MARKDOWN)
    response = requests.get("https://api.safone.me/asq?query=" + text)
    if response.status_code == 200:
        data = response.json()
        ans = data['answer']
        answer = f"""
`{ans}`

            """
        
    await message.reply_text(answer, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("More Info", url = f"https://www.google.com/search?q={text}")]]))

   

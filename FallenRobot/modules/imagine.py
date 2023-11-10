from io import BytesIO
import base64
import requests
from PIL import Image
import requests
from FallenRobot import pbot
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , CallbackQuery , Message
import asyncio


def base64_to_image(base64_data):
    try:
        if isinstance(base64_data, list):
            base64_data = base64_data[0]

        base64_data += '=' * (4 - len(base64_data) % 4)
        image_data = base64.b64decode(base64_data)
        image = Image.open(BytesIO(image_data))
        return image
    except Exception as e:
        print(f"Error decoding base64 data: {e}")
        return None

@pbot.on_message(filters.command("imagine"), group=1)
async def carbon_func(_, message):
    if message.reply_to_message:
        if message.reply_to_message.text:
            txt = message.reply_to_message.text
        else:
            return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ.")
    else:
        try:
            txt = message.text.split(None, 1)[1]
        except IndexError:
            return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ.")
    m = await message.reply_text("Generating Image ")
    response = requests.get(f"https://api.safone.dev/imagine?text={txt}&limit=1" )
    if response.status_code == 200:  
        data = response.json()
        
        # Check if 'image' key exists in the response
        imx = data['image']


    # Replace 'YOUR_BASE64_IMAGE_DATA' with your actual base64-encoded image data
    base64_image_data = imx

    image = base64_to_image(base64_image_data)
    if image:
        # Convert image to BytesIO object
        image_buffer = BytesIO()
        image.save(image_buffer, format="PNG")
        image_buffer.seek(0)

        # Send image to the user who requested
        await message.reply_photo(image_buffer, caption="Here is your image!")
        await m.delete()
    else:
        await message.reply_text("Failed to decode base64 image data.")
__mod_name__ = "Image-Gen"

__help__ = """

Command '/imagine'
eg. /imagine Boy in space

 """

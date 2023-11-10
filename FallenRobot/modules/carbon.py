from pyrogram import filters
import asyncio
from FallenRobot import pbot
from FallenRobot.utils.errors import capture_err
from FallenRobot.utils.functions import make_carbon
from io import BytesIO
import base64
import requests
from PIL import Image


def base64_to_image(base64_data):
    try:
        base64_data += '=' * (4 - len(base64_data) % 4)
        image_data = base64.b64decode(base64_data)
        image = Image.open(BytesIO(image_data))
        return image
    except Exception as e:
        print(f"Error decoding base64 data: {e}")
        return None

@pbot.on_message(filters.command("carbon"), group=35)
async def carbon_func(_, message):
    if message.reply_to_message:
        if message.reply_to_message.text:
            txt = message.reply_to_message.text
        else:
            return await message.reply_text("Please Reply to a message")
    else:
        try:
            txt = message.text.split(None, 1)[1]
        except IndexError:
            return await message.reply_text("Please Reply to a message")
    m = await message.reply_text("Generating Carbon....")
    response = requests.get(f"https://api.safone.dev/carbon?code=" + txt )
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
        await message.reply_photo(image_buffer, caption=f"Here is your Carbon Image {message.from_user.mention} ")
        await m.delete()
    else:
        await message.reply_text("Failed process image ")

@pbot.on_message(filters.command("rayso"), group=646)
async def rayso_func(_, message):
    if message.reply_to_message:
        if message.reply_to_message.text:
            txt = message.reply_to_message.text
        else:
            return await message.reply_text("Please Reply to a message")
    else:
        try:
            txt = message.text.split(None, 1)[1]
        except IndexError:
            return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ.")
    m = await message.reply_text("ɢᴇɴᴇʀᴀᴛɪɴɢ ᴄᴀʀʙᴏɴ...")
    response = requests.get(f"https://api.safone.dev/rayso?code=" + txt )
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
        await message.reply_photo(image_buffer, caption=f"Here is your image! {message.from_user.mention} ")
        await m.delete()
    else:
        await message.reply_text("Failed to decode base64 image data.")




__mod_name__ = "Carbon"

__help__ = """
Makes a Carbon or Rayso of given text and sends it to you 

 /carbon *:* Makes carbon of replied text .
 /rayso  *:* makes rayso of the given text .

"""

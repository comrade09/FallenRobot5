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

def base64_to_image(base64_data):
    try:
        base64_data += '=' * (4 - len(base64_data) % 4)
        image_data = base64.b64decode(base64_data)
        image = Image.open(BytesIO(image_data))
        return image
    except Exception as e:
        print(f"Error decoding base64 data: {e}")
        return None

@pbot.on_message(filters.command("waifu"), group=986)
async def carbon_func(_, message):
    
    m = await message.reply_text("`pls waitoo...`")

    response = requests.get(f"https://api.safone.dev/anime/nsfw/neko" )
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
    else:
        await message.reply_text("Failed to decode base64 image data.")

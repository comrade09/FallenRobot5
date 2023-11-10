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

@pbot.on_message(filters.command(["awoo","bite","blush","bonk","bully","cringe","cry" ,"cuddle","dance","glomp","hanhold","highfive","hug","kill","kiss","lick","megumin","nekoo","nom","pat","poke","shinubo","smile","smug","swaifu","wave","wink","yeet",], prefixes="/"))
async def carbon_func(_, message):

    m = await message.reply_text("Ggetting Image>...")
    
    base_url = "https://api.safone.dev/anime/sfw/"
    
    # Check the command and modify the URL accordingly
    command = message.text.split()[0][1:]  # Extract the command without the "/"
    
    if command == "awoo":
        final_url = base_url + "awoo"
    elif command == "waifu":
        final_url = base_url + "waifu"
    elif command == "pat":
        final_url = base_url + "pat"
    elif command == "bite":
        final_url = base_url + "bite"
    elif command == "blush":
        final_url = base_url + "blush"
    elif command == "bonk":
        final_url = base_url + "bonk"
    elif command == "bully":
        final_url = base_url + "bully"
    elif command == "blush":
        final_url = base_url + "blush"
    elif command == "cringe":
        final_url = base_url + "cringe"
    elif command == "cry":
        final_url = base_url + "cry"
    elif command == "cuddle":
        final_url = base_url + "cuddle"
    elif command == "dance":
        final_url = base_url + "dance"
    elif command == "glomp":
        final_url = base_url + "glomp"
    elif command == "hanhold":
        final_url = base_url + "hanhold"
    elif command == "yeet":
        final_url = base_url + "yeet"
    elif command == "wink":
        final_url = base_url + "wink"
    elif command == "kill":
        final_url = base_url + "kill"
    elif command == "kiss":
        final_url = base_url + "kiss"
    elif command == "smug":
        final_url = base_url + "smug"
    elif command == "wave":
        final_url = base_url + "wave"
    elif command == "nom":
        final_url = base_url + "nom"
    elif command == "megumin":
        final_url = base_url + "megumin"
    elif command == "lick":
        final_url = base_url + "lick"
    elif command == "hug":
        final_url = base_url + "hug"
    elif command == "highfive":
        final_url = base_url + "highfive"
    else:
        final_url = base_url  
    
    response = requests.get(f"{final_url}" )

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
__help__ = """
    
Get fsw images using this module
    
**Usage:**
    /awoo": "awoo",
    /waifu": "waifu",
    /pat": "pat",
    /bite": "bite",
    /blush": "blush",
    /bonk": "bonk",
    /bully": "bully",
    /cringe": "cringe",
    /cry": "cry",
    /cuddle": "cuddle",
    /dance": "dance",
    /glomp": "glomp",
    /hanhold": "hanhold",
    /happy": "happy",
    /highfive": "highfive",
    /hug": "hug",
    /kick": "kick",
    /kill": "kill",
    /kiss": "kiss",
    /lick": "lick",
    /megumin": "megumin",
    /neko": "neko",
    /nom": "nom",
    /poke": "poke",
    /shinubo": "shinubo",
    /slap": "slap",
    /smile": "smile",
    /smug": "smug",
    /wave": "wave",
    /wink": "wink",
    /yeet": "yeet"
    
    """
__mod_name__ = "Sfw"

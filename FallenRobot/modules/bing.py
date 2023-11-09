import json

import requests
from telegram import InputMediaPhoto, Update
from telegram.ext import CallbackContext, CommandHandler

#REPO => Your Bots File Name
from FallenRobot import (
    dispatcher,
)  # Assuming the dispatcher object is imported from the REPO file


# Command handler for the '/bingimg' command
def bingimg_search(update: Update, context: CallbackContext):
    message = update.effective_message

    try:
        text = message.text.split(None, 1)[
            1
        ]  # Extract the query from command arguments
    except IndexError:
        return message.reply_text(
            "Provide me a query to search!"
        )  # Return error if no query is provided

    search_message = message.reply_text(
        "Searching image using Bing search 🔎"
    )  # Display searching message

    # Send request to Bing image search API
    url = "https://sugoi-api.vercel.app/bingimg?keyword=" + text
    resp = requests.get(url)
    images = json.loads(resp.text)  # Parse the response JSON into a list of image URLs

    media = []
    count = 0
    for img in images:
        if count == 7:
            break

        # Create InputMediaPhoto object for each image URL
        media.append(InputMediaPhoto(media=img))
        count += 1

    # Send the media group as a reply to the user
    message.reply_media_group(media=media)

    # Delete the searching message and the original command message
    search_message.delete()
    message.delete()


# Command handler for the '/googleimg' command
def googleimg_search(update: Update, context: CallbackContext):
    message = update.effective_message

    try:
        text = message.text.split(None, 1)[
            1
        ]  # Extract the query from command arguments
    except IndexError:
        return message.reply_text(
            "Provide me a query to search!"
        )  # Return error if no query is provided

    search_message = message.reply_text(
        "Searching image using Google search 🔎"
    )  # Display searching message

    # Send request to Google image search API
    url = "https://sugoi-api.vercel.app/googleimg?keyword=" + text
    resp = requests.get(url)
    images = json.loads(resp.text)  # Parse the response JSON into a list of image URLs

    media = []
    count = 0
    for img in images:
        if count == 7:
            break

        # Create InputMediaPhoto object for each image URL
        media.append(InputMediaPhoto(media=img))
        count += 1

    # Send the media group as a reply to the user
    message.reply_media_group(media=media)

    # Delete the searching message and the original command message
    search_message.delete()
    message.delete()
    
__help__ = """
/bingimg Get images from bing
/googleimg get images from google
"""

__mod_name__ = "Bing"


# Add the command handlers to the dispatcher
dispatcher.add_handler(CommandHandler("bingimg", bingimg_search))
dispatcher.add_handler(CommandHandler("googleimg", googleimg_search))

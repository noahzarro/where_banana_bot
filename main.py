from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import json
import requests
import time
import math
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, File
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters


# create Bot
with open("token.json","r") as read_file:
    TOKEN = json.load(read_file)[0]
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

myFont = ImageFont.truetype("Ubuntu-B.ttf", 20)

img = Image.open('template.jpg')
I1 = ImageDraw.Draw(img)
what = "agityp"
to_draw = "where "+what
#to_draw = "a"
I1.text((580-len(to_draw)*4, 45), to_draw, fill=(20, 20, 20), font=myFont)

img.save("temp.png")

def start(bot, update):
    bot.send_message(update.message.from_user.id, text="Aaaagi! Use /where <word> to generate an image")

def start(bot, update):
    bot.send_message(update.message.from_user.id, text="Aaaagi! Use /where <word> to generate an image")


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('where', review))
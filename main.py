#!/usr/bin/env python3

"""A telegram bot which creates memes in the style of "where banana"
"""

import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

FONT = ImageFont.truetype("Ubuntu-Bold.ttf", 20)


def create_image(what: str):
    """
    Creates an image with the given text and saves it as temp.png.
    :param what: the text to display on the image
    """
    img = Image.open("template.jpg")
    drawer = ImageDraw.Draw(img)
    to_draw = f"where {what}"
    drawer.text((580 - len(to_draw) * 4, 45), to_draw, fill=(20, 20, 20), font=FONT)
    img.save("temp.png")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Sends a welcome message to the user.
    :param update: the Telegram update object
    :param context: the Telegram context object
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Aaaagi! Use /where <word> to generate an image",
    )


async def where(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Generates and sends an image with the specified text to the user.
    :param update: the Telegram update object
    :param context: the Telegram context object
    """
    if len(context.args) > 0:
        what = " ".join(context.args)
        create_image(what)
        with open("temp.png", "rb") as img_to_send:
            await context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=img_to_send
            )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Aaaagi! Use /where <word> to generate an image",
        )


def main():
    """
    Runs the bot with the specified Telegram API token.
    """
    token = os.environ.get("TOKEN")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("where", where))

    app.run_polling()


if __name__ == "__main__":
    main()

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os

TOKEN = os.environ.get("TOKEN")

app = ApplicationBuilder().token(TOKEN).build()
myFont = ImageFont.truetype("Ubuntu-Bold.ttf", 20)


def create_image(what: str):
    img = Image.open("template.jpg")
    drawer = ImageDraw.Draw(img)
    to_draw = f"where {what}"
    drawer.text((580 - len(to_draw) * 4, 45), to_draw, fill=(20, 20, 20), font=myFont)

    img.save("temp.png")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Aaaagi! Use /where <word> to generate an image",
    )


async def where(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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


app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("where", where))

app.run_polling()

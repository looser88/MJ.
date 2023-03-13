import os
import aiohttp
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from pyrogram.handlers import MessageHandler
from pyshorteners import Shortener

FIRE_API = os.environ.get("FIRE_API", "4b4ee8f8717d775262ef74432e202b8be8597b62")

reply_markup = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("𝘊𝘭𝘰𝘴𝘦", callback_data='close_data')
        ]]
    )

@Client.on_message(filters.command(["short"]) & filters.regex(r'https?://[^\s]+'))
async def reply_shortens(bot, update):
    message = await update.reply_text(
        text="`Analysing your link...`",
        disable_web_page_preview=True,
        quote=True
    )
    link = update.matches[0].group(0)
    shorten_urls = await short(link)
    await message.edit_text(
        text=shorten_urls,
        disable_web_page_preview=True
    )

@Client.on_inline_query(filters.regex(r'https?://[^\s]+'))
async def inline_short(bot, update):
    link = update.matches[0].group(0),
    shorten_urls = await short(link)
    answers = [
        InlineQueryResultArticle(
            title="Short Links",
            description=update.query,
            input_message_content=InputTextMessageContent(
                message_text=shorten_urls,
                disable_web_page_preview=True
            ),
            reply_to_message_id=message.id
        )
    ]
    await bot.answer_inline_query(
        inline_query_id=update.id,
        results=answers
    )

async def short(link):
    shorten_urls = "**--Shorted URLs--**\n"
    
    # Bit.ly shorten
    if FIRE_API:
        try:
            s = Shortener(api_key=FIRE_API)
            url = s.Fire-links.in(link)
            shorten_urls += f"\n**Fire-links.in :-** {url}"
        except Exception as error:
            print(f"Bit.ly error :- {error}")

    
    # Send the text
    try:
        shorten_urls += ""
        return shorten_urls
    except Exception as error:
        return error

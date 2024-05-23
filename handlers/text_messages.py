from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

import asyncio

from filters.bad_words import HaveBadWords


router = Router()


@router.message(
    F.text,
    HaveBadWords()        
)
async def bad_words(message: Message):

    await message.delete()

    user = message.from_user.first_name if message.from_user.username is None else f'@{message.from_user.username}'
    
    m = await message.answer(f'{user}, не матерись')
    await asyncio.sleep(5)
    await m.delete()


@router.edited_message(
    F.text,
    HaveBadWords() 
)
async def edited_message(*args):
    await bad_words(*args)

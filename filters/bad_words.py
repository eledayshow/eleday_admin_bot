from aiogram.filters import BaseFilter
from aiogram.types import Message

import string
from transliterate import translit

import filters.words as words


class HaveBadWords(BaseFilter):

    async def __call__(self, message: Message):

        text = message.text.lower()

        # неплохие слова
        for w in words.not_bad_words:
            text = text.replace(w, '')

        # пунктуация
        for p in string.punctuation + ' ':
            text = text.replace(p, '')

        or_text = text
        
        # транслирование (slovo -> слово)
        text = translit(text, 'ru')
        
        for word in words.bad_words:
            if word in text:
                return True

        # похожие буквы
        for k, w in words.en_ru_map.items():
            text = text.replace(k, w)
        
        for word in words.bad_words:
            if word in text:
                return True

        text = or_text

        # похожие буквы
        for k, w in words.en_ru_map.items():
            text = text.replace(k, w)
        
        for word in words.bad_words:
            if word in text:
                return True
            
        return False

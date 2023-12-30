import asyncio

from aiogram import Bot
from aiogram.enums import *
from aiogram.types import *
from aiogram.utils.formatting import *


class Responder:
    message: Message

    def __init__(self, entity: Bot | Message):
        if isinstance(entity, Message):
            self.message = entity
            self.bot = entity.bot
        else:
            self.bot = entity

    def get_content(self, content):
        if isinstance(content, Text):
            return [content.as_html(), ParseMode.HTML]

        return [content, None]

    async def message_manipulate(self, content, method='answer', reply_markup=None,
                                 autodelete_seconds: int | None = None, **args):
        msg_text, parse_method = self.get_content(content)

        if method and hasattr(self.message, method) and callable(func := getattr(self.message, method)):
            message = await func(msg_text, reply_markup=reply_markup, can_be_edited=True, parse_mode=parse_method,
                                 **args)

        if autodelete_seconds:
            await self.delete_msg(message, autodelete_seconds)

        return message

    async def answer(self, content: Text | str, reply_markup=None, autodelete_seconds: int | None = None, **args):
        return await self.message_manipulate(content=content, reply_markup=reply_markup,
                                             autodelete_seconds=autodelete_seconds, **args)

    async def delete_msg(self, message: Message | None = None, autodelete_seconds: int | None = None):
        if autodelete_seconds:
            await asyncio.sleep(autodelete_seconds)

        if not message:
            message = self.message

        return await self.force_delete(message.chat.id, message.message_id)

    async def force_delete(self, chat_id, msg_id):
        return await self.bot.delete_message(chat_id, msg_id)

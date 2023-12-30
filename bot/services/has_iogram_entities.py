from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import *


class HasIogramEntites:
    message: Message
    state: FSMContext
    message: Message
    bot: Bot
    chat: Chat

    def set_args(self, message: Message | None = None, bot: Bot | None = None, state: FSMContext | None = None) -> None:
        self.message = message
        self.chat = message.chat
        self.bot = bot
        self.state = state

    def __init__(self, message: Message, bot: Bot | None = None, state: FSMContext | None = None) -> None:
        self.set_args(message, bot, state)



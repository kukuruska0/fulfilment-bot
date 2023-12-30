from aiogram.utils.formatting import Text

from bot.services.messager import Messager


def messager(method: str = '', *args) -> Messager | Text:
    if method and hasattr(Messager, method) and callable(func := getattr(Messager, method)):
        return func(*args)
    return Messager


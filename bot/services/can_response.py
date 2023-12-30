from aiogram.types import *



from bot.services.responder import Responder


class CanResponse:
    message: Message

    async def response(self, text, reply_markup=None, autodelete_seconds: int | None = None, **args):
        return await Responder(self.message).answer(text, reply_markup, autodelete_seconds=autodelete_seconds, **args)

from bot.helpers import messager
from bot.keyboards.main import *
from bot.services.can_response import CanResponse
from bot.services.has_iogram_entities import HasIogramEntites


class CommandsController(HasIogramEntites, CanResponse):

    async def action_start(self):
        await self.response(messager('start'), reply_markup=start_kb())

    async def action_calculation(self):
        await self.response(messager('calculation'))

    async def action_product(self):
        await self.response(messager('product'))

    async def action_price(self):
        await self.response(messager('price'))

    async def action_shipment(self):
        await self.response(messager('shipment'), reply_markup=teams_kb())

    async def action_address(self):
        await self.response(messager('address'))

    async def action_spoilage(self):
        await self.response(messager('spoilage'))

    async def action_complaint(self):
        await self.response(messager('complaint'))

    async def action_links(self):
        await self.response(messager('links'), reply_markup=links_kb())

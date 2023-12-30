from aiogram import F
from aiogram.filters import Command
from aiogram.types import *

from bot.controllers.commands_controller import CommandsController
from bot.routes.router import Router
from messages.commands.cmds import *
from messages.messages_text.msg_txt import *

router = Router()

router.action_message(CommandsController, CommandsController.action_start, Command(commands=["start"]))
router.action_message(CommandsController, CommandsController.action_calculation, F.text == cmd_calculate)
router.action_message(CommandsController, CommandsController.action_product, F.text == cmd_product)
router.action_message(CommandsController, CommandsController.action_price, F.text == cmd_price)
router.action_message(CommandsController, CommandsController.action_shipment, F.text == cmd_shipment)
router.action_message(CommandsController, CommandsController.action_address, F.text == cmd_address)
router.action_message(CommandsController, CommandsController.action_spoilage, F.text == cmd_spoilage)
router.action_message(CommandsController, CommandsController.action_complaint, F.text == cmd_complaints)
router.action_message(CommandsController, CommandsController.action_links, F.text == cmd_links)


@router.message(F.text == cmd_technical_task)
async def technical_task(message: Message):
    await message.answer(cmd_technical_task_text)
    await message.answer_document(FSInputFile(path=r'D:\\Pictures\\ТЗ_OZON_ВАША_ФАМИЛИЯ_ДАТА_ОТПРАВКИ_ТЗ.xlsx'))
    await message.answer_document(FSInputFile(path=r'D:\\Pictures\\ТЗ_ВАША ФАМИЛИЯ_ДАТА ОТПРАВКИ ТЗ.xlsx'))


@router.message(F.text == cmd_agreement)
async def agreement(message: Message):
    await message.answer_document(FSInputFile(path=r'D:\\Pictures\\Contract_SAXARGROUP.docx'))


@router.callback_query(F.data == 'team_1')
async def team_1(callback: CallbackQuery):
    await callback.message.answer('Конакты команды Стаса:\nhttps://t.me/saxargroupFf')
    await callback.answer()


@router.callback_query(F.data == 'team_2')
async def team_2(callback: CallbackQuery):
    await callback.message.answer('Конакты команды Артема:\nhttps://t.me/SAXAR_GROUP_team_Artem')
    await callback.answer()

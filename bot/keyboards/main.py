from aiogram.types import *
from aiogram.utils.keyboard import *

from messages.commands.cmds import *


def start_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=cmd_calculate), KeyboardButton(text=cmd_technical_task)],
        [KeyboardButton(text=cmd_product), KeyboardButton(text=cmd_address)],
        [KeyboardButton(text=cmd_price), KeyboardButton(text=cmd_agreement)],
        [KeyboardButton(text=cmd_shipment), KeyboardButton(text=cmd_spoilage)],
        [KeyboardButton(text=cmd_complaints)],
        [KeyboardButton(text=cmd_links)]

    ])


def teams_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='👥 Команда Стаса', callback_data='team_1'),
         InlineKeyboardButton(text='👥 Команда Артёма', callback_data='team_2')],

    ])


def links_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Перейти на сайт', url='https://fulfillmentmoscow.ru/'),
         InlineKeyboardButton(text='Перейти в чат', url='https://t.me/+7BXfUVG5TvAzZTIy')],
        [InlineKeyboardButton(text='Инстаграм', url='https://instagram.com/fulfilment_saxar'),
         InlineKeyboardButton(text='VK', url='https://vk.com/fulfillment_moskva')]

    ])


def force_reply(placeholder: str | None = None):
    return ForceReply(input_field_placeholder=placeholder)

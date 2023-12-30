from aiogram.utils.formatting import *

from messages.messages_text.msg_txt import *


class Messager:

    @staticmethod
    def start():
        return as_list(
            Bold(start_cmd),
        )

    @staticmethod
    def calculation():
        return as_list(
            Bold(cmd_calculate_text),
        )

    @staticmethod
    def product():
        return as_list(
            Bold(cmd_product_text),
        )

    @staticmethod
    def price():
        return as_list(
            Bold(cmd_price_text),
        )

    @staticmethod
    def shipment():
        return as_list(
            Bold(cmd_shipment_text),
        )

    @staticmethod
    def address():
        return as_list(
            Bold(cmd_address_text),
        )

    @staticmethod
    def spoilage():
        return as_list(
            Bold(cmd_spoilage_text),
        )

    @staticmethod
    def complaint():
        return as_list(
            Bold(cmd_complaints_text),
        )

    @staticmethod
    def links():
        return as_list(
            Bold(cmd_links_text),
        )






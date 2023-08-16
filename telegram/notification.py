from asyncio import ensure_future
from aiogram import Bot, Dispatcher

from telegram.types import MessageInfo
from settings import TELEGRAM_TOKEN, GROUP_ID

class Notification:
    bot = Bot(token=TELEGRAM_TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    @classmethod
    async def _send_message_to_group(cls, group_id: int|str, text: str, photo: str):
        try:
            await cls.bot.send_photo(chat_id=group_id, caption=text, photo=photo)
        except Exception as ex:
            print(ex)
    
    @classmethod
    async def message_preparing(cls, message: MessageInfo):
        try:  
            stickers_infos = []

            for sticker in message.item.stickers:
                sticker_info = f'{sticker.slot + 1}. {sticker.name} (Wear {sticker.wear})'
                stickers_infos.append(sticker_info)

            stickers_str = '\n'.join(stickers_infos)

            message_text = f"<a href='{await cls._url(message)}'>{message.item.good.name}</a>\nFloat: {message.item.paintwear}\nPrice: {message.item.price}\nReference price (Steam): {message.item.good.steam_price_cny}\nStickers:\n{stickers_str}"
            await cls._send_message_to_group(group_id=GROUP_ID, text=message_text, photo=message.item.icon_url)
        except Exception as ex:
            print(ex)

    @classmethod
    def starter(cls):
        ensure_future(cls.dp.start_polling())

    @staticmethod
    async def _url(message: MessageInfo):
        base_url = f'https://buff.163.com/goods/{message.item.good.id}?'

        classid = f'classid={message.item.classid}&'
        instanceid = f'instanceid={message.item.instanceid}&'
        assetid = f'assetid={message.item.assetid}&'
        contextid = f'contextid={message.item.contextid}&'
        sell_order_id = f'sell_order_id={message.item.id}'
        
        return base_url + classid + instanceid + assetid + contextid + sell_order_id

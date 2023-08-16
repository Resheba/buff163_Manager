import asyncio

from api import RequestItems
from database import LogList, RuleList
from database.utils import RuleRow, LogRow, current_time
from telegram import Notification, MessageInfo


async def rule_processing(rule: RuleRow, page_num: int = 1):
    rule_params = rule.to_params(page_num)
    if not rule_params:
        log = LogRow(skin=rule.good_id, price='-', sticker=rule.sticker_id, overprice=rule.overprice, link='-', result='Not enough information')
        LogList.append(log)
        return

    response = await RequestItems.get(params=rule_params)

    if response:
        for item in response.data.items:
            link = await Notification._url(MessageInfo(item))
            if item.price <= rule.overprice:
                # log = LogRow(skin=response.data.items[0].good.name, sticker=rule.sticker_id, price=item.price, overprice=rule.overprice, link=link, result='Send notification')
                # LogList.append(log)
                message_info = MessageInfo(item)
                await Notification.message_preparing(message=message_info)
            else:
                # log = LogRow(skin=response.data.items[0].good.name, sticker=rule.sticker_id, price=item.price, overprice=rule.overprice, link=link, result='Overprice')
                # LogList.append(log)
                return
    else:
        # log = LogRow(skin=rule.good_id, price='-', sticker=rule.sticker_id, overprice=rule.overprice, link='-', result='Bad Response')
        # LogList.append(log)
        print('Bad response', current_time())
        return
    
    if response.data.total_page > rule_params.page_num:
        await rule_processing(rule, page_num + 1)


async def main():
    await asyncio.sleep(5)
    print('Start')
    while True:
        try:
            rules = RuleList.read()

            # awaitable_rules = [rule_processing(rule) for rule in rules]
            # await asyncio.gather(*awaitable_rules)

            for rule in rules:
                await rule_processing(rule)
                await asyncio.sleep(5)

            await asyncio.sleep(200)
        except Exception as ex:
            print(ex)
            await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())
    Notification.starter()

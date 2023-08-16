import aiohttp

from settings import HEADERS, COOKIES
from classes import ItemsResponseParser
from classes.types import ResponseItems, RequestBase, ParamsItems


class RequestItems(RequestBase):
    url = 'https://buff.163.com/api/market/goods/sell_order'

    @classmethod
    async def get(cls, params: ParamsItems) -> ResponseItems:
        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
                async with session.get(cls.url, params=params.to_dict(), headers=HEADERS, cookies=COOKIES) as request:
                    response_json = await request.json()
            # response_json = requests.get(cls.url, params=params.to_dict(), headers=HEADERS, cookies=COOKIES).json()
            response = ItemsResponseParser(response_json)
            return response
        except Exception as ex:
            print('req', ex)
            return None
"""
Buff163 Responses paresers

For more introduce just use main module::

    >> from classes import ...


This is a duplicate module.
"""


from classes.types.item import Good, Sticker, Item
from classes.types.response import ResponseGoods, ResponseItems, DataItems, DataGoods


def GoodsResponseParser(
        data: dict
        ) -> ResponseGoods:
    code: str = data.get('code')
    msg: str | None = data.get('msg')
    data: dict = data.get('data')

    assert code != 'OК', f'Bad Response: {msg}'
    
    goods_dicts: list[dict] = data.get('items')
    goods: list[Good] = []

    for good in goods_dicts:
        id: int = good.get('id')
        name: str = good.get('name')
        sell_num: int = good.get('sell_num')
        temp_dict: dict = good.get('goods_info')
        steam_price: float = float(temp_dict.get('steam_price'))
        steam_price_cny: float = float(temp_dict.get('steam_price_cny'))
        
        good = Good(
            id=id,
            name=name,
            sell_num=sell_num,
            steam_price=steam_price,
            steam_price_cny=steam_price_cny
        )
        goods.append(good)

    page_num: int = data.get('page_num')
    page_size: int = data.get('page_size')
    total_count: int = data.get('total_count')
    total_page: int = data.get('total_page')

    response_data = DataGoods(
        goods=goods,
        page_num=page_num,
        page_size=page_size,
        total_count=total_count,
        total_page=total_page 
    )

    return ResponseGoods(
        code=code,
        data=response_data,
        msg=msg
    )


def ItemsResponseParser(
        data: dict
) -> ResponseItems:
    code: str = data.get('code')
    msg: str | None = data.get('msg')
    data: dict = data.get('data')

    assert code != 'OК', f'Bad Response: {msg}'
    
    good_info: dict = tuple(data.get('goods_infos').items())[0][1]
    
    good_id: int = good_info.get('goods_id')
    good_name: str = good_info.get('name')
    steam_price: float = float(good_info.get('steam_price'))
    steam_price_cny: float = float(good_info.get('steam_price_cny'))
    
    good = Good(
        id=good_id,
        name=good_name,
        steam_price=steam_price,
        steam_price_cny=steam_price_cny
    )

    items_dicts: list[dict] = data.get('items')
    items: list[Item] = []

    for item in items_dicts:
        item_id: str = item.get('id')
        allow_bargain: bool = item.get('allow_bargain')
        price: float = float(item.get('price'))
        temp_dict: dict = item.get('asset_info')
        paintwear: float = float(temp_dict.get('paintwear'))
        temp_dict: dict = temp_dict.get('info')
        paintindex: int = temp_dict.get('paintindex')
        paintseed: int = temp_dict.get('paintseed')
        stickers_dicts: list[dict] = temp_dict.get('stickers')

        stickers: list[Sticker] = []

        for sticker in stickers_dicts:
            sticker_id: int = sticker.get('sticker_id')
            category: str = sticker.get('sticker')
            sticker_name: str = sticker.get('name')
            slot: int = sticker.get('slot')
            wear: float = sticker.get('wear')

            sticker = Sticker(
                sticker_id=sticker_id,
                category=category,
                name=sticker_name,
                slot=slot,
                wear=wear
            )
            stickers.append(sticker)

        item = Item(
            id=item_id,
            good=good,
            allow_bargain=allow_bargain,
            paintseed=paintseed,
            paintindex=paintindex,
            paintwear=paintwear,
            price=price,
            stickers=stickers
        )
        items.append(item)

    page_num: int = data.get('page_num')
    page_size: int = data.get('page_size')
    total_count: int = data.get('total_count')
    total_page: int = data.get('total_page')

    response_data = DataItems(
        page_num=page_num,
        page_size=page_size,
        total_count=total_count,
        total_page=total_page,
        items=items
    )

    return ResponseItems(
        code=code,
        data=response_data,
        msg=msg
    )


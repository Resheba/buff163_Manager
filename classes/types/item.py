from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Tag:
    id: int
    category: str
    internal_name: str
    localized_name: str


@dataclass
class Tags:
    category: Optional[Tag] = None
    category_group: Optional[Tag] = None
    custom: Optional[Tag] = None
    exterior: Optional[Tag] = None
    itemset: Optional[Tag] = None
    quality: Optional[Tag] = None
    rarity: Optional[Tag] = None
    type: Optional[Tag] = None
    weapon: Optional[Tag] = None
    weaponcase: Optional[Tag] = None


@dataclass
class Good:
    id: int
    name: str
    steam_price: float
    steam_price_cny: float
    sell_num: Optional[int] = None
    tags: Optional[Tags] = None


@dataclass
class Sticker:
    sticker_id: int
    category: str
    name: str
    slot: int
    wear: float


@dataclass
class Item:
    id: str
    good: Good
    allow_bargain: bool
    paintseed: int
    paintindex: int
    paintwear: float
    price: float
    icon_url: str
    assetid: str
    classid: str
    contextid: int
    instanceid: str
    stickers: list[Sticker] = field(default_factory=list)


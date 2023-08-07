from dataclasses import dataclass, field
from classes.types.item import Item, Good


@dataclass
class DataBase:
    page_num: int
    page_size: int
    total_count: int
    total_page: int


@dataclass
class DataGoods(DataBase):
    goods: list[Good] = field(default_factory=list)


@dataclass
class DataItems(DataBase):
    items: list[Item] = field(default_factory=list)


@dataclass
class ResponseBase:
    code: str | None
    data: DataBase | None
    msg: str | None


@dataclass
class ResponseGoods(ResponseBase):
    data: DataGoods


@dataclass
class ResponseItems(ResponseBase):
    data: DataItems


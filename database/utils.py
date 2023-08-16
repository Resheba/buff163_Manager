import time
from dataclasses import dataclass, field
from gspread import Worksheet

from classes.types import ParamsItems


def current_time() -> str:
    return time.strftime("%H:%M:%S", time.localtime())


@dataclass
class LogRow:
    skin: str
    sticker: str
    price: float
    overprice: float
    result: str
    link: str
    time: str = field(default_factory=current_time)

    def to_sheet(self):
        return [self.time, self.skin, self.sticker, self.price, self.overprice, self.result, self.link]


@dataclass
class RuleRow:
    good_id: int
    wear: tuple
    postition: int
    overprice: float
    sticker_id: int

    def __post_init__(self):
        try:
            self.good_id = int(self.good_id) if self.good_id else None
            self.sticker_id = int(self.sticker_id) if self.sticker_id else None
            self.postition = int(self.postition) if self.postition else None
            self.overprice = float(self.overprice.replace(',', '.')) if self.overprice else None
            self.wear = tuple(float(range) for range in self.wear.replace(',', '.').split('-')) if self.wear else (0,1)
        except Exception as ex:
            self.good_id = None
    
    def to_params(self, page_num: int = 1):
        if self.good_id and self.overprice and self.sticker_id:
            return ParamsItems(
                goods_id=self.good_id, 
                extra_tag_ids=[f'slot_{self.postition-1}_{self.sticker_id}' if self.postition else self.sticker_id], 
                min_paintwear=self.wear[0], 
                max_paintwear=self.wear[1],
                page_num=page_num)


class ListBase:
    _list: Worksheet = None
    start_row: int = 2
    

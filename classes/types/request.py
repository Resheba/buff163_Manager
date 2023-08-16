from dataclasses import dataclass


@dataclass
class ParamsItems:
    goods_id: int
    extra_tag_ids: list[int]
    min_paintwear: float = 0
    max_paintwear: float = 1
    page_num: int = 1
    sort_by: str = 'price.asc'
    wearless_sticker: int = 1
    game: str = 'csgo'

    def to_dict(self):
        self.extra_tag_ids = ','.join([str(tag_id) for tag_id in self.extra_tag_ids])
        return self.__dict__


class RequestBase:
    url = None

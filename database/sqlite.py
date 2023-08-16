import sqlite3


class StickerBase:
    db = sqlite3.connect('database/stickers/data.db')
    cur = db.cursor()

    @classmethod
    def get_sticker_extra(cls, sticker_id: int) -> int:
        try:
            sticker_row = cls.cur.execute(f'SELECT extra_tag_id FROM Stickers WHERE sticker_id == {sticker_id}').fetchone()
            sticker_extra = sticker_row[0] if sticker_row else None
            return sticker_extra
        except Exception as ex:
            print(ex)
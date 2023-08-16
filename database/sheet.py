from database.utils import ListBase, LogRow, RuleRow
from database.base import LIST_LOGS, LIST_RULES


class LogList(ListBase):
    _list = LIST_LOGS

    @classmethod
    def append(cls, row: LogRow):
        cls._list.append_row(row.to_sheet())


class RuleList(ListBase):
    _list = LIST_RULES

    @classmethod
    def read(cls) -> list[RuleRow]:
        rules: list[RuleRow] = []
        rows = cls._list.get_values(f'A{cls.start_row}:E')
        for row in rows:
            if row:
                if row[0].count(','):
                    ids = [id.strip() for id in row[0].split(',')]
                    for id in ids:
                        temp_row = [id] + row[1:]
                        rules.append(RuleRow(*temp_row))
                else:
                    rules.append(RuleRow(*row))
        return rules

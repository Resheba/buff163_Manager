import gspread

from settings import SERVICE_ACCOUNT, TABLE_ID




gc = gspread.service_account_from_dict(SERVICE_ACCOUNT)

SHEET = gc.open_by_key(TABLE_ID)

LIST_RULES = SHEET.worksheet('rules')
LIST_LOGS = SHEET.worksheet('logs')
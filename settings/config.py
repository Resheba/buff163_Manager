import dotenv, os, json


dotenv.load_dotenv()

# ENV VARIABLES
SERVICE_ACCOUNT = json.loads(os.getenv('SERVICE_ACCOUNT_CREDIT'))
TABLE_ID = os.getenv('TABLE_ID')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GROUP_ID = os.getenv('GROUP_ID')
HEADERS = eval(os.getenv('HEADERS'))
COOKIES = eval(os.getenv('COOKIES'))
#


if not all([SERVICE_ACCOUNT,TABLE_ID, TELEGRAM_TOKEN]):
    raise Exception('Some env variables are missing. Please, check all env variables in settings/config.py file.')
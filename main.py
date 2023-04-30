import requests
import time
from settings import BOT_TOKEN


API_URL: str = 'https://api.telegram.org/bot'
offset: int = -2
updates: dict
timeout = 60

def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            print(result['message']['text'])
            offset = result['update_id']
            do_something()

    time.sleep(1)
    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')
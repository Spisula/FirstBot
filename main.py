import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
API_DOGS_URL: str = 'https://random.dog/woof.json'
BOT_TOKEN: str = '5886220274:AAH6QAYckGGLKQAx22bQ4Jb2tUYLMS_a2sU'
ERROR_TEXT: str = 'Нет картинки (('
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
chat_id: int
dog_response: requests.Response
dog_link: str

while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            if 'message' in result: # проверяет есть ли ключ message в апдейте
                chat_id = result['message']['from']['id']
            else:  #если в апдейте ключ не message, а edited_message, тогда ничего не происходит и
                continue  # не выдает ошибку
            dog_response = requests.get(API_DOGS_URL)
            if dog_response.status_code == 200:
                dog_link = dog_response.json()['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={dog_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
    time.sleep(1)
    counter += 1
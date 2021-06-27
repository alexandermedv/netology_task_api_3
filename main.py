import requests
from pprint import pprint
import datetime
import time
import json


def get_questions():
    day_before_yesterday = datetime.date.today() - datetime.timedelta(2)
    print('Выгружаем вопросы, начиная с даты:', day_before_yesterday)
    unix_time = time.mktime(day_before_yesterday.timetuple())
    url = 'https://api.stackexchange.com/2.2/search/advanced?fromdate=' + \
          str(int(unix_time)) + '&order=desc&sort=activity&tagged=python&site=stackoverflow'
    resp = requests.get(url)
    # pprint(resp.json())
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(resp.json(), f, ensure_ascii=False, indent=4)
    return 'Список вопросов сохранен в файле result.json'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_questions())

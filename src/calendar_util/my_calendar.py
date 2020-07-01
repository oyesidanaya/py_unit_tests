from datetime import datetime
import requests


def today_is_a_weekday():
    today = datetime.today()
    return  0 <= today.weekday() < 5


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

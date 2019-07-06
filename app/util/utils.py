import json
import random
import time
from urllib.parse import unquote


def get_json(string: str) -> dict:
    return json.loads(unquote(string))


def get_random_filename() -> str:
    year = time.localtime(time.time()).tm_year
    month = time.localtime(time.time()).tm_mon
    day = time.localtime(time.time()).tm_mday
    hour = time.localtime(time.time()).tm_hour
    min = time.localtime(time.time()).tm_min
    rnum = random.randint(10000, 99999)
    return "{}{}{}{}{}{}".format(year, month, day, hour, min, rnum)


def to_online_pic(img: str):
    return "http://120.78.216.241/upload/" + img[img.rfind('/') + 1:]

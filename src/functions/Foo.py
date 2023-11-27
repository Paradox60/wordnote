from datetime import datetime
import datetime as date
from random import randint
import random

def Now_time():
    current_datetime = datetime.now()

    moment1 = date.datetime(1, 1, 1, 0, 0, 0)
    moment2 = date.datetime(current_datetime.year, current_datetime.month,current_datetime.day, current_datetime.hour, current_datetime.minute, current_datetime.second)
    delta = moment2 - moment1

    delta_s = delta.total_seconds()
    delta_s = int(delta_s)
    return delta_s
import datetime

import pytz

starter = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))

def to_timezone(tz):
    print(starter.astimezone(pytz.timezone(tz)))


to_timezone('America/Phoenix')
import datetime

def to_string(dt1):
    print(dt1.strftime('%d %B %Y'))

def from_string(dt2, dt3):
    print(datetime.datetime.strptime(dt2, dt3))




to_string(datetime.datetime.now())

from_string("09/24/12 18:30", "%m/%d/%y %H:%M")
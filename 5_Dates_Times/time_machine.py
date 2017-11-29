import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def delorean(hrs):
    ender = starter + datetime.timedelta(hours = (hrs))
    print(ender)

def time_machine(value1, string1):
    if string1 == 'years':
        value1 = value1 * 365
        string1 = 'days'
    else:
        pass
    ender = starter + datetime.timedelta(**{string1: value1})
    print(ender)

time_machine(4, 'years')
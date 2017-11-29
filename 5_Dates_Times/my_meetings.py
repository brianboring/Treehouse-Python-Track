import datetime
import pytz

def meeting(my_time):

    fmt = '%Y-%m-%d %H:%M:%S %Z%z'

    my_tz = pytz.timezone('America/Phoenix')
    tz_la = pytz.timezone('America/Los_Angeles')
    tz_den = pytz.timezone('America/Denver')
    tz_ny = pytz.timezone('America/New_York')
    tz_jun = pytz.timezone('America/Juneau')
    tz_chi = pytz.timezone('America/Chicago')
    tz_det = pytz.timezone('America/Detroit')

    my_meeting = my_tz.localize(my_time)

    print("My meeting in Arizona is at {}".format(my_meeting.strftime(fmt)))
    print("In Juneau, that will be {}".format(my_meeting.astimezone(tz_jun).strftime(fmt)))
    print("In Los Angeles, that will be {}".format(my_meeting.astimezone(tz_la).strftime(fmt)))
    print("In Denver, that will be {}".format(my_meeting.astimezone(tz_den).strftime(fmt)))
    print("In Chicago, that will be {}".format(my_meeting.astimezone(tz_chi).strftime(fmt)))
    print("In Detroit, that will be {}".format(my_meeting.astimezone(tz_det).strftime(fmt)))
    print("In New York, that will be {}".format(my_meeting.astimezone(tz_ny).strftime(fmt)))





meeting(datetime.datetime(2017, 9, 21, 23, 3, 21, 761533))
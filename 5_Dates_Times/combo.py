import datetime

def time_tango(d1, t1):
    # dt1 = datetime.datetime.strptime(d1, '%Y, %m, %d')
    # dt2 = datetime.datetime.strptime(t1, '%H:%M')
    # print(dt1)
    # print(dt2)
    print(datetime.datetime.combine(d1, t1))


time_tango("2016, 7, 12", "12:30")

#NOT COMPLETED
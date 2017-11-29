import datetime


def minutes(dt1, dt2):
    print(dt1)
    print(dt2)
    td = dt1-dt2
    print(td)
    print(round(datetime.timedelta.total_seconds(dt2 - dt1)/60))

minutes(datetime.datetime.now(), datetime.datetime.now()+datetime.timedelta(minutes=5))
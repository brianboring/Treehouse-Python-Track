import datetime


def timestamp_oldest(*args):
    time_list = []
    for timestamp in args:
        time_list.append(datetime.datetime.fromtimestamp(timestamp))
    time_list.sort()
    print(time_list)
    print(time_list[0])
    oldest = time_list[0]
    print(oldest)

timestamp_oldest(24.34523, 543.2342, 12.2342)


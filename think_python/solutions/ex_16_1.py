class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

current_time = Time(22, 45, 37)

def print_time(time:Time):
    print('%.2d: %.2d: %.2d' % (time.hour, time.minute, time.second))

def time_to_int(time)->int:
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds) -> Time:
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def mul_time(time:Time, num:int) ->Time:
    product = time_to_int(time) * num
    return int_to_time(product)

print_time(mul_time(current_time, 5))

finish_time = Time(1, 36, 24)
def average_pace(finish_time:Time, distance:int) -> Time:
    return mul_time(finish_time, 1 / distance)

print_time(average_pace(finish_time, 18))


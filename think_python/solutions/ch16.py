from copy import copy

class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0): # default value = 0
        self.hour = hour
        self.minute = minute
        self.second = second


adela_clock = Time(9, 59, 30) # positional argument
lina_clock = Time(8, 2, 17)

def print_time(c: Time):
    # print(f'{c.hour}:{c.minute}:{c.second}')
    print('%.2d: %.2d: %.2d' % (c.hour, c.minute, c.second))

    # %d, %f, %s 는 %로 formating 해줘야 한다.

print_time(adela_clock)
print_time(lina_clock)

def is_after(t1: Time, t2: Time) -> bool:
    t1_seconds = t1.hour * 3600 + t1.minute * 60 + t1.second
    t2_seconds = t2.hour * 3600 + t2.minute * 60 + t2.second
    return t2_seconds < t1_seconds

print(is_after(adela_clock, lina_clock))
# <C + n> : 자동완성, <C + p> : 이전 입력을 기반으로 고를 수 있게 한다.


# Pure function
  # 의존하는게 없다. (dependency가 없다.)
  # 입출력이 없을 가능성이 높다. 외부영향을 안 받는다.
    # haskell의 모나드로 입출력을 추상화시켜 순수 함수를 만들 수 있게 되었다.
  # It doens't modify any of the objects passed to it as arguments and it has no effect, like displaying a vlue or getting user input, other than returning a value.


def add_time(t1:Time, t2:Time) -> Time:
    sum = Time() 
    # reference : variable, parameter, return value에 primitive를 사용하는 것이 아니라면 reference를 대입하는 것. 
    # reference는 메모리 상의 Time 객체의 위치를 나타낸다. (변수에는 객체 전체를 다 넣을 수 없음.) 
    # 즉 <__main__.Time object at 0x102bbc0f0>를 나타낸다.
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
         sum.second -= 60
         sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

sum = Time(minute=20, second=10) # keyword argument

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
print_time(done)

# Ex16.3 Correct Version of increment that doesn't include loop
def increment(time:Time, seconds:int): 
    time.second += seconds
    if time.second >= 60: 
        incremented_min, remaining_sec = divmod(time.second, 60)
        time.second = remaining_sec
        time.minute += incremented_min

    if time.minute >= 60:
        incremented_hour, remaining_min = divmod(time.minute, 60)
        time.minute = remaining_min
        time.hour += incremented_hour
    return time

print("==========")
print_time(adela_clock)
print("----------")
print_time(increment(adela_clock, 600))

# Ex16.4 Pure Version of increment
def pure_increment(time: Time, seconds:int) -> Time:
    changed_time = Time()
    changed_time = copy(time)
    changed_time.second += seconds

    if changed_time.second >= 60:
        added_min, remaining_sec = divmod(changed_time.second, 60)
        changed_time.second = remaining_sec
        changed_time.minute += added_min
    if changed_time.minute >= 60:
        added_hour, remaining_min = divmod(changed_time.minute, 60)
        changed_time.minute = remaining_min
        changed_time.hour += added_hour
    return changed_time

print("===========")
adela_clock = Time(9, 59, 30) # positional argument
print_time(adela_clock)
print('-----------')
print_time(pure_increment(adela_clock, 600))

def time_to_int(time: Time)->int:
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds:int)->Time:
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

print(time_to_int(adela_clock))
print_time(int_to_time(60))
# Test
print(time_to_int(int_to_time(60)) == 60)

def add_time(t1:Time, t2:Time):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time obejct in add_time')
    # Or you can use assert()
    # assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

# Ex16.5 Rewrite increment using time_to_int and int_to_time
def re_increment(time:Time, seconds:int) -> Time:
    seconds += time_to_int(time)
    return int_to_time(seconds)

print_time(adela_clock)
print_time(re_increment(adela_clock, 60))


def valid_time(time: Time) -> bool:
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True




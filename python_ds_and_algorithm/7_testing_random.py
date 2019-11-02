import random

def testing_random():
    """ random 모듈 테스트 """
    values = [1, 2, 3, 4]
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    print(random.sample(values, 2)) # -> list형태로 나옴
    print(random.sample(values, 3)) # -> list형태로 나옴
    
    """ values 리스트를 섞기 """
    random.shuffle(values)
    print(values)

    """ 0~10 사이의 임의의 정수 생성하기"""
    print(random.randint(0, 10))
    print(random.randint(0, 10))



if __name__ == "__main__":
    testing_random()


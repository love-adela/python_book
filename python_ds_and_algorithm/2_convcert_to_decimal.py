def convert_to_decimal(number:int, base:int)->int:
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number //= 10
    return result


def test_convert_to_decimal():
    number, base = 1001, 2
    assert convert_to_decimal(number, base) == 9
    print('테스트 통과')


if __name__ == "__main__":
    test_convert_to_decimal()


def finding_gcd(a, b):
    while (b!=0):
        result = b
        a, b = b, a%b
    return result


def test_finding_gcd():
    number1 = 21
    number2 = 12
    assert finding_gcd(number1, number2) == 3
    print('테스트 통과')


def using_euclidean(a, b):
    if b  == 0:
        return a
    return euclidean(b, a%b)

def test_using_euclidean():
    number1 = 21
    number2 = 12
    assert using_euclidean(number1, number2) == 3
    print('테스트 통과')

if __name__ == "__main__":
    test_finding_gcd()

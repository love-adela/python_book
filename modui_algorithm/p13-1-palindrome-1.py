def palindrome(s):
    n = len(s)
    i = 0
    j = n - 1

    while i < j:  # 가능한 빨리 탈출하자.
        l = s[i].upper()
        rValue = s[j].upper()
        if l != rValue:
            return False

        i += 1
        j -= 1
    return True


def palindrome4(s):
    n = len(s)
    i = 0
    j = n - 1

    while i < j:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


def palindrome2(s):
    n = len(s)
    i = 0
    j = n - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


def palindrome3(s):
    n = len(s)
    i = 0
    j = n - 1

    result = True

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            result = False
            break

    return result


print(palindrome("Wow"))

# (('J' * 31) + 'o') * 31 ... + 'n'
# hash code = 234
# no of slots = 128. 32개 부족헤? -> 64개
# 234 % 128 = 106 slot으로 가즈아!
# 106에 누가 있아
# 1. 오픈 어드레싱 - 105번으로 가봐.
# 2. 세퍼레이트 체인 - 걔한테 Linked list로 붙어봐.

# 슬롯 개수가 100개인데 우리가 76개를 썼어. 그럼 두배로 늘리자. (75%) 75% <- 로드 팩터

# 31은 소수여서 겹치지 않는 수로 만들기 좋고 쉬프트 연산과 뺄셈으로 효과적으로 계산 됨

# 2 << 1
# '10' << 1  = '100' = 4
# 4 << 1 = 8
# 4 >> 1 = 2
# a * 2 == a << 1
# a * 4 == a << 2
# a * 8 == a << 3
# a * (2 ** n) == a << n
# a * 31 == (a << 5)- a
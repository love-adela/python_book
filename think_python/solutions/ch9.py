import random

#=============9-1================
print('Exercsise 9-1')
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)

print('')

#=============9-2================
print('Exercsise 9-2')
def has_no_e(word)->bool:
    return 'e' not in word

n = int(input('sample 개수를 입력하세요'))
def get_sample():
    fin = open('words.txt')
    word_list = [line.strip() for line in fin if len(line.strip())>0]
    sample = random.sample(word_list, n)
    return sample

count = 0
sample = get_sample()
for word in sample:
    if has_no_e(word) == True:
        count += 1
    # print(f'{word}: {has_no_e(word)}')
print(f'"e"가 없을 확률: {count / n * 100}')
print('')

#=============9-3================
print('Exercise 9-3')
def avoids(word, forbidden)->bool:
    for letter in word:
        if letter in forbidden:
            return False
    return True
print(avoids('radiogaga', 'gaga'))
print('')
#=============9-4================
print('Exercise 9-4')
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

print(uses_only('radiogaga','radio'))
print('')
#=============9-5================
print('Exercise 9-5')
def uses_all(word, required):
#    for letter in required:
#        if letter not in word:
#            return False
#    return True
    return uses_only(required, word)

print(uses_all('bohemianrhapsody', 'rhapsody'))
print('')

#=============9-6================
print('Exercise 9-6')
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

def is_abecedarian(word):
    if len(word) <=1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])

def is_abecedarian(word):
    i = 0
    while i < len(word) -1:
        if word[i+1] < word[i]:
            return False
        i+= 1
    return True

print(is_abecedarian('bohemian'))
print('')
#=============9-7================
print('Exercise 9-7')

def is_triple_double(word):
    i = 0
    count = 0 
    while i < len(word) - 1:
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            count = 0
            i += 1
    return False

def find_triple_double():
    with open('words.txt') as fin:
        for line in fin:
            word = line.strip()
            if is_triple_double(word):
                print(word)

find_triple_double()
print('')

#=============9-8================
print('Exercise 9-8')
def is_palindrome(word):
    return word == word[::-1]
	
def is_palindrome_num(num):
    part_one = num[2:6]
    num = str(int(num) + 1)
    part_two = num[1:6]
    num = str(int(num) + 1)
    part_three = num[1:5]
    num = str(int(num) + 1)
    part_four = num
    if is_palindrome(part_one):
        if is_palindrome(part_two):
            if is_palindrome(part_three):
                if is_palindrome(part_four):
                    return True
    return False
	
def check_num():
    for i in range(100000, 999999):
        if is_palindrome_num(str(i)):
            print(i)
			
check_num()
print('')

#=============9-9================
print('Exercise 9-9')

def is_reverse(a, b):
    return b == a[::-1]

def find_difference():
    diff = 15
    while diff < 50:
        count = 0
        me = 0
        while me < 99:
            mom = me + diff
            if is_reverse(str(me).zfill(2), str(mom)):
                count += 1
                if count == 8:
                    return diff
            me += 1
        diff += 1

def find_my_age(n):
    mom = n
    me = 0
    count = 0
    while me < 99:
        if is_reverse(str(me).zfill(2), str(mom)):
            count += 1
            if count == 6:
                return me
        mom += 1
        me += 1

print(f'내 나이는 find_my_age(find_difference())살')

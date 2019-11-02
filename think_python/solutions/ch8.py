# ===============8-1==============
# strip()
# replace()

# ===============8-2==============
print("8-2. count() 사용 예제")
print('banana'.count('a'))

# ===============8-3==============
def is_palindrome(s:str)->bool:
    return s == s[::-1]

print("8-3. [::-1] 사용 예제")
print(is_palindrome('plugandplayyalpdnagulp'))

# ===============8-4==============
print("8-4. is_lower() 사용 예제")
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
    return False

def any_lowercase2(s):
    for c in s:
        if not c.islower():
            return False
    return True

def any_lowercase3(s):
    flag = False
    for c in s:
        flag = c.islower() # 소문자
        if flag == True:
            break
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# TEST
print('case1')
print(any_lowercase1('orange'))
print(any_lowercase1('Orange'))
print(any_lowercase1('oRange'))
print(any_lowercase1('ORANGE'))
print('case2')
print(any_lowercase2('orange'))
print(any_lowercase2('Orange'))
print(any_lowercase2('oRange'))
print(any_lowercase2('ORANGE'))
print('case3')
print(any_lowercase3('orange'))
print(any_lowercase3('Orange'))
print(any_lowercase3('oRange'))
print(any_lowercase3('ORANGE'))
print('case4')
print(any_lowercase4('orange'))
print(any_lowercase4('Orange'))
print(any_lowercase4('oRange'))
print(any_lowercase4('ORANGE'))

# ===============8-5===============
print("8-5. Caesar Cypher")
def rotate_word(s, n):
	s_c = "" #initialize
	i = 0 #initialize
	for c in s:
		if ord(c) >= ord('A') and ord(c) <= ord('Z'):
			i = (ord(c) - ord('A') + n ) % 26 + ord('A') 
		elif ord(c) >= ord('a') and ord(c) <= ord('z'):
			i = (ord(c) - ord('a') + n ) % 26 + ord('a')
		else:
			i = ord(c) # other characters does not change
		s_c +=  chr(i)
	return s_c
	
print (rotate_word("apple+apple", 3))
print (rotate_word("APPLE", 3))	



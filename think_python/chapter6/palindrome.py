def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

print(first('zerodarkthirty'))
print(last('zerodarkthirty'))
print(middle('zerodarkthirty'))

# Error
# print(first(''))
# print(last(''))
# print(middle(''))

def is_palindrome(word):
    if word == word[::-1]:
            return True
    else:
            return False
		
print(is_palindrome("adeleda"))

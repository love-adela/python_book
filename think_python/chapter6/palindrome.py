def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) < 2:
        return True
    else:
        return first(word) == last(word) and is_palindrome(middle(word))
    
print(is_palindrome('')) # True
print(is_palindrome('a')) # True
print(is_palindrome('aa')) # True
print(is_palindrome('ab')) # False
print(is_palindrome("aba")) # True


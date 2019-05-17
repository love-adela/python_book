1. In a print statement, what happens if you leave out one of the parentheses, or both?
```
>>> print 'OOPS it"s a mistake'
File "<stdin>", line 1
  print 'OOPS it"s a mistake'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('OOPS it"s a mistake')?

>>> print ('OOPS it"s a mistake'
...
...

>>> print 'OOPS it"s a mistake')
  File "<stdin>", line 1
    print 'OOPS it"s a mistake')
                              ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('OOPS it"s a mistake'))?
```

2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?
```
>>> print('OOPS it"s a mistake)
File "<stdin>", line 1
  print("OOPS it"s a mistake)
                            ^
SyntaxError: EOL while scanning string literal

>>> print(Hello World)
  File "<stdin>", line 1
    print(Hello World)
                    ^
SyntaxError: invalid syntax
```

3. You can use a minus sign to make a negative number like -2. What happens of you put a plus sign before a number? What about 2 ++ 2?
```
>>> 645 + - 2342
-1697

>>> 2 ++ 2
4
```

4. In math notation, leading zeros are okay, as in 02. What happens if you try this in Python?
```
>>> 02 + 6
File "<stdin>", line 1
  02 + 6
   ^ + 6
SyntaxError: invalid token
```

5. What happens if you have two values with no operator between them?
```
>>> 2 2
File "<stdin>", line 1
  2 2 
    ^ 
SyntaxError: invalid syntax
```
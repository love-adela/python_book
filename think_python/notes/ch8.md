## Chapter8. Strings

Strings are not like integers, floats, and booleans. A string is a sequence of characters, which means it is an ordered collection of other values. 

### 8.1 A String Is a Sequence

* Index : 
  * The expression in brackets. The index indicates which character in the sequence you want.
  * The index is an offset from the beginning of the string, and offset of the first letter is zero.
  * As an index, you can use an expression that contains variables and operators.
  * The value of the index has to be an integer. Otherwise you get: 
  ```
  TypeError: string indicies must be integers
  ```
  * Negative indicies, which count backward from the end of string.

### 8.2 Traversal with a for Loop

* while loop
* for loop: Each time through the loop, the next character in the string is assigned to the variable letter. The loop continues until no characters are left.

  ```
  for letter in fruit:
      print(letter)
  ```

### 8.3 String Slices

A segment of string is called a slice. Selecting a slice is similar to selecting a character:

* counterintuitive
  * Counterintuitive is the behavior the operator [n:m] returns the part of the string from the 'n-eth' character to the 'm-eth' character, including the first but excluding the last. 
  * It might help to imagine the indicies pointing between the characters.

If you omit the first index (before the colon), the slice starts at the beginning of the string. If you omit the second index, the slice goes to the end of the string.

### 8.4 Strings are immutable

Strings are immutable, which means you can't change an existing string. The best you can do is create a new string that is variation on the original.

For now, an object is the same thing as a value, but we will refine that definition later ('Objects and Values')

### 8.5 Searching

Search is the pattern of computation - traversing a sequence and returning when we find what we are looking for.

### 8.6 Looping and Counting

Counter is another pattern of computation. o

### 8.7 String Methods
Strings provide methods that perform a variety of useful operations.

A method is similar to a function - it takes arguments and returns a value- but the syntax is different. 

This form of dot notation specifies the name of the method, upper, and the name of the string to apply the mthod to, word. The empty parentheses indicate that this method takes no arguments.

A method call is called an *invocation*. In this case, we would say that we are invoking upper on word.

By default, find starts at the beginning of the string, but it can take a second argument, the index where it should start. 


```
>>> name = 'bob'
>>> name.find('b', 1, 2)
-1
```

### 8.8 The in Operator

The word *in* is a boolean operator that takes two strings and returns True if the first appears as a substring in the second:

```
>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False
```

### 8.9 String Comparison

The relational operators work on strings. 
Relational operations are useful for putting words in alphabetical order:
We should convert strings to a sandard format, such as all lowercase, before performing the comparison.

* Question
Python doesn't handle uppercase and lowercase letters the same way people do. All the uppercase letters come before all the lowercase letters.

* Question
A common way to address this problem is to convert strings to a standard format, such as all lowercase, before performing the comparison. Keep that in mind in case you have to defend yourself against a man armed with a Pineapple.



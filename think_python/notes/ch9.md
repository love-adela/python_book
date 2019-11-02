## Chapter9. Case Study: Word Play

### 9.1 Reading Word Lists

'fin' is a common name for a file object used for input. The file object provides several methods for reading, including readline, which reads characters from the file until it gets to a newline and returns the result as a string.

```
>>> fin = open('words.txt')
>>> fin.readline()
'aa\r\n'
```

The first word in this particular list is 'aa', which is a kind of lava. The sequence \r\n represents two whitespace characters, a carriage return and a newline, that seperate this word from the next.

The file object keeps track of where it is in the file, so if you call readline again, you get the new word:

```
>>> fin.readline()
'aah\r\n'
>>> line = fin.readline()
>>> word = line.strip()
>>> word
'aahed'
```

You can also use a file object as part of a for loop. This program reads words.txt and prints each word, one per line:

```
fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)
```

### 9.2 Search

You could write this function more concisely using the in operator.

* Reduction to a previously solved problem
It means that you recognize the problem you are working on as an instance of a solved problem and apply an existing solution.

### 9.3 Looping with Indices

* for loop

* while loop



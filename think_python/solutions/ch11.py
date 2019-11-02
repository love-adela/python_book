# Use the number as an index into the list, and increment the appropriate counter.

def count():
    word = input()

    alphabet = [chr(i + ord('a')) for i in range(26)]
    count = [0] * 26

    for letter in word:
        count[ord(letter) - ord('a')] += 1

    counted = [(letter, number) for (letter, number) in list(zip(alphabet, count)) if number != 0]

    return counted
print(count())


def count1():
    word = input()
    alphabet = [chr(i + ord('a')) for i in range(26)]
    count = [0] * 26
    answer = []

    for letter in word:
        count[ord(letter) - ord('a')] += 1

    for index, value in enumerate(count):
        if value > 0:
            answer.append((chr(index + ord('a')), value))
    print(answer)

# Use get to write histogram more concisely. You should be able to eliminate the if statement.

def histogram(word:str):
    d = dict()
    for letter in word:
        d[letter] = 1 + d.get(letter, 0)
    return d

print(histogram('banana'))

# Exercise 11-1
print('#############Exercise 11-1###############')


def is_reverse(word1, word2):
    if len(word1) != len(word2): # The Guardian Pattern
        return False
    for i in range(len(word1)):
        if i == 0:
            return word1[i] is word2[-1]
        if word1[i]== word2[-i-1]:
            return True

print(is_reverse('string', 'gnitrs'))
print(is_reverse('string', 'string'))

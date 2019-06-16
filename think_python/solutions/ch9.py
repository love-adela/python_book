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

def get_sample_word():
    fin = open('words.txt')
    word_list = [line.strip() for line in fin if len(line.strip())>0]
    sample = random.sample(word_list, 20)
    return sample

for word in get_sample_word():
    print(f'{word}: {has_no_e(word)}')

print('')

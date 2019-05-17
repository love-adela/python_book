f2e = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}
e2f = {right: left for left, right in f2e.items()}

print(e2f)
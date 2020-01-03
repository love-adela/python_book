class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

class Stack(object):
    def __init__(self):
        self.head = None
        self.count =0

    def is_empty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def pop(self):
        if self.count > 0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            return node.value
        else:
            print('Stack is empty')

    def peek(self):
        if self.count > 0 and self.head:
            return self.head.value
        else:
            print('Stack is empty')

    def size(self):
        return self.count

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end= ' ')
            node = node.pointer
        print()


def reverse_string_with_stack(string):
    s = Stack()
    result = ''

    for c in string:
        s.push(c)

    while not s.is_empty():
        result += s.pop()

    return result

print(reverse_string_with_stack('버피는 천사다'))
print(reverse_string_with_stack('pop'))


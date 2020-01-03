class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0 

    def is_empty(self)->bool:
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
            print(node.value, end=' ')
            node = node.pointer
        print()


if __name__ == "__main__":
    stack = Stack()
    print(f'스택이 비었나요? {stack.is_empty()}')
    print('스택에 숫자 0~9를 추가합니다.')
    for i in range(10):
        stack.push(i)
    stack._printList()
    print(f'스택이 크기: {stack.size()}')
    print(f'peek: {stack.peek()}')
    print(f'pop: {stack.pop()}')
    print(f'peek: {stack.peek()}')
    print(f'스택이 비었나요? {stack.is_empty()}')
    stack._printList()


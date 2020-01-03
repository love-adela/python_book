class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self)->bool:
        return not bool(self)

    def push(self, value):
        return self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print('Stack is empty')
    
    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print('Stack is empty')

    def __repr__(self):
        return repr(self.items)


if __name__ == '__main__':
    stack = Stack()
    print(f'스택이 비었나요? {stack.is_empty()}')
    print(f'스택에 숫자 0~9를 추가합니다.')
    for i in range(10):
        stack.push(i)
    print(f'스택 크기: {stack.size()}')
    print(f'peek: {stack.peek()}')
    print(f'pop: {stack.pop()}')
    print(f'peek: {stack.peek()}')
    print(f'스택이 비었나요? {stack.is_empty()}')
    print(stack)

from complex_number import ComplexNumber
from stack_impl import Stack

if __name__ == '__main__':
    stack = Stack()
    for i in range(5):
        stack.push(ComplexNumber(i / 5, i / 10))
        print(stack)

    print('popped', stack.pop())
    print('popped', stack.pop())
    print('size', stack.size())
    print('stack is', stack)

from complex_number import ComplexNumber
from stack_impl import Stack

if __name__ == '__main__':
    stack = Stack()
    cache_of_nums = []
    for i in range(5):
        num = ComplexNumber(i / 5, i / 10)
        stack.push(num)
        cache_of_nums.append(num)
        print(stack)

    print('element to find', cache_of_nums[-1])
    print('found with idx', stack.find(cache_of_nums[-1]))

    print('popped', stack.pop())
    print('popped', stack.pop())
    print('size', stack.size())
    print('stack is', stack)
    stack.sum_two_top_elements()
    print('stack after summing two top elements', stack)

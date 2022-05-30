from complex_number import ComplexNumber


class Node:
    def __init__(self, value: ComplexNumber):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top_el = Node(None)
        self.size_of_stack = 0

    def is_empty(self):
        return self.top_el is None

    def clear(self):
        self.top_el = Node(None)

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top_el.next.value

    def size(self):
        return self.size_of_stack

    def push(self, complex_num: ComplexNumber):
        node = Node(complex_num)
        node.next = self.top_el.next
        self.top_el.next = node
        self.size_of_stack += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return_val = self.top_el.next
        self.top_el.next = self.top_el.next.next
        self.size_of_stack -= 1
        return return_val.value

    def find(self, elem: ComplexNumber):
        idx = -1
        cur = self.top_el.next
        while cur:
            idx += 1
            if elem == cur.value:
                break
            cur = cur.next
        else:
            return -1

        return idx

    def sum_two_top_elements(self):
        if self.size() < 2:
            raise Exception("Stack does not have enough elements for the operation")
        self.top_el.next.next.value = self.top_el.next.value + self.top_el.next.next.value
        self.top_el.next = self.top_el.next.next
        self.size_of_stack -= 1

    def __str__(self):
        cur = self.top_el.next
        result = ""
        while cur:
            result += str(cur.value) + ", "
            cur = cur.next
        return f'[{result[:-2]}]'

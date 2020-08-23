'''
Theory:
    A stack is a linear data structure which works on last in first out (LIFO).
    All three basic operations (delete, insert, display) is applicable to the
    most recent element of the stack.

Space and time complexity:
    1. Space complexity: O(n)
    2. Insert: O(1)
    3. Delete: O(1)
    4. Display: O(1)
    5. Is empty: O(1)
    6. Get length: O(1)

'''


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):

        '''
        Push the input value at the top of the stack
        '''

        self.stack.append(value)

    def pop(self):

        '''
        Remove and output the element at the top of the stack
        '''

        self.stack.pop()

    def top(self):

        '''
        Output the element at the top of the stack
        '''

        return self.stack[-1]

    def is_empty(self):

        '''
        Output boolean value for whether the stack is empty or not
        '''

        if self.stack == []:
            return True

        else:
            return False

    def get_length(self):

        '''
        Return the number of elements in the stack
        '''

        return len(self.stack)

    def print_all_elements(self):

        print(self.stack)

stack = Stack()
stack.is_empty()
stack.push(12)
stack.push(6)
stack.push(87)
stack.push(90)
top_elem = stack.top()
print(top_elem)
len_stack = stack.get_length()
print(len_stack)
stack.pop()
stack.pop()
stack.print_all_elements()

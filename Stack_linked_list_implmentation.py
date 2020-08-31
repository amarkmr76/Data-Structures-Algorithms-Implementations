'''
Theory:
    A stack is a data structure which works on last in first out (LIFO).
    All three basic operations (delete, insert, display) is applicable to the
    most recent element of the stack.

Space and time complexity:
    1. Space complexity: O(n)
    2. Insert: O(1)
    3. Delete: O(1)
    4. Display: O(1)
    5. Is empty: O(1)

'''


class Node:
    '''
    Node of a linked list
    '''

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DLinkedListWithTail:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):

        '''
        Function:
            Return a boolean var for whether or not the linked list is empty
        '''

        if self.head is None:
            print('The linked list is empty!')
            return True

        else:
            print('The linked list is not empty!')
            return False

    def insert(self, val):

        '''
        Function:
            Add an elements to the end of the linked list.
        Input:
            val (int/float): The value of the elements we want to add
        '''

        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            end_node = self.tail
            end_node.next = new_node
            new_node.previous = end_node
            self.tail = new_node

    def show_element_at_end(self):

        '''
        Function:
            If the linked list is populated, return the value to which the tail
            pointer points at

        Output:
            Value of the node to which the tail is pointing at. None if the
            linked list is empty
        '''

        if self.head is None:
            return None

        else:
            return self.tail.data

    def delete_last_node(self):

        '''
        Function:
            Remove the current tail node of the linked list. The tail pointer
            will now point at the node right before the previous tail node
        '''

        if self.head is not None:
            output = self.tail.data
            end_node = self.tail
            previous_node = end_node.previous

            if previous_node is not None:
                previous_node.next = None
            else:
                self.head = None
            self.tail = previous_node

            return output

    def print_all_elements(self):

        '''
        Function:
            Print all the values present in the linked list
        '''

        curr_node = self.head

        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


class Stack:

    def __init__(self):
        self.stack = DLinkedListWithTail()

    def push(self, value):

        '''
        Push the input value at the top of the stack
        '''

        self.stack.insert(value)

    def pop(self):

        '''
        Remove and output the element at the top of the stack
        '''

        return self.stack.delete_last_node()

    def top(self):

        '''
        Output the element at the top of the stack
        '''

        return self.stack.show_element_at_end()

    def is_empty(self):

        '''
        Output boolean value for whether the stack is empty or not
        '''

        return self.stack.is_empty()

    def print_all_elements(self):

        self.stack.print_all_elements()

stack = Stack()
stack.is_empty()
stack.push(12)
stack.push(6)
stack.push(87)
stack.push(90)
top_elem = stack.top()
print(top_elem)
stack.pop()
stack.pop()
stack.print_all_elements()

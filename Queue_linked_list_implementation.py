'''
Theory:
    Queue is a data structure which works on First in first out (FIFO).
    All three basic operations (delete, insert, display) is applicable to the
    oldest element of the queue.

Space and time complexity:
    1. Space complexity: O(n)
    2. Enqueue: O(1)
    3. Dequeue: O(1)
    4. Display front element: O(1)
    5. Display back element: O(1)
    6. Is empty: O(1)
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

    def show_element_at_start(self):

        '''
        Function:
            If the linked list is populated, return the value to which the head
            pointer points at

        Output:
            Value of the node to which the head is pointing at. None if the
            linked list is empty
        '''

        if self.head is None:
            return None

        else:
            return self.head.data

    def delete_head_node(self):

        '''
        Function:
            Remove the current head node of the linked list. The head pointer
            will now point at the node to which the previous head node was
            pointing at
        '''

        if self.head is not None:
            output = self.head.data
            next_node = self.head.next
            self.head = next_node
            if next_node is not None:
                next_node.previous = None

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


class Queue:

    def __init__(self):
        self.queue = DLinkedListWithTail()

    def enqueue(self, value):

        '''
        Push the input value at the end of the queue
        '''

        self.queue.insert(value)

    def dequeue(self):

        '''
        Remove and output the element at the start of the queue
        '''

        return self.queue.delete_head_node()

    def display_front_element(self):

        '''
        Output the element at the start of the queue
        '''

        return self.queue.show_element_at_start()

    def is_empty(self):

        '''
        Output boolean value for whether the queue is empty or not
        '''

        return self.queue.is_empty()

    def print_all_elements(self):

        self.queue.print_all_elements()

queue = Queue()
queue.is_empty()
queue.enqueue(50)
queue.enqueue(-2)
queue.enqueue(23)
queue.enqueue(17)
queue.display_front_element()
queue.dequeue()
queue.print_all_elements()
queue.dequeue()
queue.print_all_elements()

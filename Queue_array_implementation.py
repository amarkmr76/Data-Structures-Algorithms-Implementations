'''
Theory:
    Queue is a linear data structure which works on First in first out (FIFO).
    All three basic operations (delete, insert, display) is applicable to the
    oldest element of the queue.

Space and time complexity:
    1. Space complexity: O(n)
    2. Enqueue: O(1)
    3. Dequeue: O(1)
    4. Display front element: O(1)
    5. Display back element: O(1)
    6. Is empty: O(1)
    7. Get length: O(1)
'''


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, value):

        '''
        Push the input value at the end of the queue
        '''

        self.queue.append(value)

    def dequeue(self):

        '''
        Remove and output the element at the start of the queue
        '''

        self.queue.pop(0)

    def display_front_element(self):

        '''
        Output the element at the start of the queue
        '''

        return self.queue[0]

    def is_empty(self):

        '''
        Output boolean value for whether the queue is empty or not
        '''

        if self.queue == []:
            return True

        else:
            return False

    def print_all_elements(self):

        print(self.queue)

queue = Queue()
queue.is_empty()
queue.enqueue(50)
queue.enqueue(-2)
queue.enqueue(23)
queue.enqueue(17)
queue.display_front_element()
queue.dequeue()
queue.print_all_elements()

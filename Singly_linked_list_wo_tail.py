'''
Theory:
    Linked lists are different from array in the context that they're not
    contiguous. They consist of nodes with each node carrying a value and a
    pointer to the next node. They can be broadly categorized as:
        1. Singly linked lists and Doubly linked lists
            a) Without tail (Only head pointer)
            b) With tail (Both head and tail pointers)

Space and Time complexities for a Singly linked list WITHOUT tail:
    1. Space complexity: O(n)
    2. Get element at start: O(1)
    3. Inserting an element at start: O(1)
    4. Deleting an element at start: O(1)
    5. Get element at end: O(n)
    6. Inserting an element at end: O(n)
    7. Deleting an element at end: O(n)
    8. Inserting an element in middle BEFORE a given node: O(n)
    9. Inserting an element in middle AFTER a given node: O(1)
    10. Deleting an element in middle: O(n)
    11. Check whether the linked list is empty: O(1)
    12. Check whether an element is present: O(n)

'''


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SLinkedListWithoutTail:

    '''
    Class for Singly linked list without tail
    '''
    def __init__(self):
        self.head = None

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

    def populate_an_empty_list(self, list_input):

        '''
        Function:
            Populate a list of elements to an empty linked list. The head
            pointer would point to the first value of the array.
        Input:
            list_input (list): Array of elements we want to populate
        '''

        self.head = Node(list_input[0])
        curr_node = self.head

        for i in range(1, len(list_input)):
            new_node = Node(list_input[i])
            curr_node.next = new_node
            curr_node = new_node

        curr_node.next = None

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
            print('The linked list is empty')

        else:
            print('The element at start is ' + str(self.head.data))

    def show_element_at_end(self):

        '''
        Function:
            If the linked list is populated, return the value at the end
        Output:
            Value of the end node. None if the linked list is empty
        '''

        if self.head is None:
            print('The linked list is empty')

        else:
            curr_node = self.head

            while curr_node:
                if curr_node.next is None:
                    print('The element at end is ' + str(curr_node.data))

                curr_node = curr_node.next

    def print_all_elements(self):

        '''
        Function:
            Print all the values present in the linked list
        '''

        curr_node = self.head

        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def is_element_present(self, value):

        '''
        Function:
            Check if a particular value is present in the linked list
        Input:
            value (int): The value we want to check
        Output:
            Boolean var for whether or not the input value is present
        '''

        if self.head is None:
            print('The linked list is empty')

        else:
            curr_node = self.head
            fl_found = 0

            while curr_node:
                if curr_node.data == value:
                    fl_found = 1
                    break

                curr_node = curr_node.next

            if fl_found == 1:
                print('The value ' + str(value) + ' is present in the list')
                return True

            else:
                print('The value ' + str(value) + ' is missing from the list')
                return False

    def insert_element_at_start(self, value):

        '''
        Function:
            Enter a value to be placde at the start of the linked list. The
            head pointer would now point at this value. The node corresponding
            to this value will point at the previous head node
        Input:
            value (int): The value we want to insert in the linked list
        '''

        new_node = Node(value)
        head_node = self.head
        self.head = new_node
        new_node.next = head_node

    def insert_element_at_end(self, value):

        '''
        Function:
            Enter a value to be placed at the end of the linked list. Traverse
            through the linked list to identify the last element and add
            a new node at the end
        Input:
            value (int): The value we want to insert in the linked list
        '''

        if self.head is None:
            print('The list is empty! Please use insert_element_at_start')

        else:
            new_node = Node(value)
            curr_node = self.head

            while curr_node:
                if curr_node.next is None:
                    curr_node.next = new_node
                    break

                curr_node = curr_node.next

    def insert_element_after_a_node(self, value, curr_value):

        '''
        Function:
            Insert a node of input value after a node whose value is curr_value
        Input:
            value (int): The value we want to insert in the linked list
            curr_value (int): The value of the node after which we want to
                                insert the new value
        '''

        if self.head is None:
            print('The list is empty! Please use insert_element_at_start')

        else:
            new_node = Node(value)
            tmp_node = self.head

            while tmp_node:
                if tmp_node.data == curr_value:
                    next_node = tmp_node.next
                    tmp_node.next = new_node
                    new_node.next = next_node

                tmp_node = tmp_node.next

    def insert_element_before_a_node(self, value, curr_value):

        '''
        Function:
            Insert a node of input value before a node whose value is
            curr_value
        Input:
            value (int): The value we want to insert in the linked list
            curr_value (int): The value of the node before which we want to
                                insert the new value
        '''

        if self.head is None:
            print('The list is empty! Please use insert_element_at_start')

        else:
            new_node = Node(value)
            tmp_node = self.head

            while tmp_node:
                if tmp_node.next is not None:
                    if tmp_node.next.data == curr_value:
                        curr_next_node = tmp_node.next
                        tmp_node.next = new_node
                        new_node.next = curr_next_node
                        break

                    tmp_node = tmp_node.next

                else:
                    print('Reached the end of the Linked List!')
                    break

    def delete_top_node(self):

        '''
        Function:
            Remove the current head node of the linked list. The head pointer
            will now point at the node to which the previous head node was
            pointing at
        '''

        if self.head is None:
            print('The list is empty!')

        else:
            self.head = self.head.next

    def delete_last_node(self):

        '''
        Function:
            Remove the current end node of the linked list.
        '''

        if self.head is None:
            print('The list is empty!')

        else:
            curr_node = self.head

            while curr_node:
                if curr_node.next.next is None:
                    curr_node.next = None

                curr_node = curr_node.next

    def delete_node_from_middle(self, node_value):

        '''
        Function:
            Remove the node which takes the value node_value
        Input:
            node_value (int): Value of the node we want to remove
        '''

        if self.head is None:
            print('The list is empty!')

        else:
            curr_node = self.head

            while curr_node:
                if curr_node.next is not None:
                    if curr_node.next.data == node_value:
                        curr_node.next = curr_node.next.next
                        break

                    curr_node = curr_node.next

                else:
                    print('Reached the end of the Linked List!')
                    break

llist = SLinkedListWithoutTail()
llist.is_empty()
llist.populate_an_empty_list([41, 37, 25, -7, 925])
llist.is_empty()
llist.print_all_elements()
llist.show_element_at_start()
llist.show_element_at_end()
llist.is_element_present(-9)
llist.is_element_present(-7)
llist.insert_element_at_start(64)
llist.print_all_elements()
llist.insert_element_at_end(72)
llist.print_all_elements()
llist.insert_element_after_a_node(value=21, curr_value=-7)
llist.print_all_elements()
llist.insert_element_before_a_node(value=1, curr_value=37)
llist.print_all_elements()
llist.delete_top_node()
llist.print_all_elements()
llist.delete_last_node()
llist.print_all_elements()
llist.delete_node_from_middle(37)
llist.print_all_elements()

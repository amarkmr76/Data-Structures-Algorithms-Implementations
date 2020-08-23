
'''
Theory:
    Arrays are contiguous data structures which store a group of elements.

Space and time complexities (n = number of elements):
    1. Space complexity: O(n)
    2. Searching for an element in unsorted array: O(n)
    3. Searching for an element in sorted array using Binary Search: O(log(n))
    4. Inserting an element at start: O(n)
    5. Inserting an element in middle: O(n)
    6. Inserting an element at end: O(1)
    7. Deleting the element at start: O(n)
    8. Deleting an element in the middle: O(n)
    9. Deleting the element at end: O(1)
    10. Fetch the value at a given index: O(1)
    11. Set the value at an index: O(1)
    12. Get length of the list: O(1)

    List is the in-built implementation of arrays in Python
'''


class Array:

    '''
    Array operations when input type is int
    '''

    def __init__(self):
        self.array = []

    def get_length(self):

        '''
        Function:
            Returns the length of the array
        '''

        if self.array == []:
            print('The array is empty!')
            return

        else:
            print('The length of the array is: ' + str(len(self.array)))
            return len(self.array)

    def insert_element_at_end(self, value):

        '''
        Function:
            Insert the input value at the end of the array
        Input:
            value (int): The value we want to insert
        '''

        self.array.append(value)

    def insert_element_at_start(self, value):

        '''
        Function:
            Insert the input value at the end of the array
        Input:
            value (int): The value we want to insert
        '''

        # In order to insert elements at the start of an array, a copy of the
        # array is created copy in O(n) time, copy the exisitng elements and
        # at the start insert the new element

        self.array.insert(0, value)

    def insert_element_at_given_index(self, index, value):

        '''
        Function:
            Insert a new value in the array while keeping all others
        Input:
            index (int): The index at which we want to insert the new value
            value (int): The new value we want to insert
        '''

        self.array.insert(index, value)

    def search_key(self, key):

        '''
        Function:
            Search if a key is present. If yes, print its count.
        Input:
            key (int): The value we want to search for
        '''

        if self.array == []:
            print('The array is empty!')
            return

        count = 0
        fl_found = 0

        for element in self.array:
            if element == key:
                fl_found = 1
                count += 1

        if fl_found == 1:
            print(str(key) + ' occurs ' + str(count) + ' times in the array!')

        else:
            print(str(key) + ' not found in the array!')

    def delete_key_if_present(self, key):

        '''
        Function:
            Delete all instances of an input key if it is present in the array
        Input:
            key (int): The value we want to delete from the array
        '''

        self.array = list(filter(lambda value: value != key, self.array))

    def fetch_value_at_index(self, idx):

        '''
        Function:
            Print the value present at the input index
        Input:
            idx (int): The index whose value we want to print
        '''

        print('The value at index ' + str(idx) + ' is ' + str(self.array[idx]))

    def set_value_at_index(self, idx, value):

        '''
        Function:
            Replace the value at the input index with the new value
        Input:
            idx (int): The index whose value we want to replace
            value (int): The new value
        '''

        self.array[idx] = value

    def print_all_elements(self):

        for element in self.array:
            print(element, end=' ')

# Running the commands
array = Array()
# Check if the array is empty. If not empty return the length of the array
array.get_length()
# Lets populate the array with a few integers.
array.insert_element_at_end(56)
array.insert_element_at_end(21)
array.insert_element_at_end(19)
array.insert_element_at_end(79)
array.insert_element_at_end(67)
array.print_all_elements()
array.insert_element_at_start(33)
array.print_all_elements()
array.insert_element_at_given_index(2, 777)
array.print_all_elements()
array.search_key(41)
array.search_key(777)
array.delete_key_if_present(22)
array.print_all_elements()
array.delete_key_if_present(19)
array.print_all_elements()
array.fetch_value_at_index(4)
array.set_value_at_index(5, -90)
array.print_all_elements()
array.get_length()

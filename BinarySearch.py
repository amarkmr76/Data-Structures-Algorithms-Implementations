'''
For a sorted array, an element can be searched for in logarithmic time
complexity using Binary Search.
'''


class BinarySearch:

    '''
    Search algorithm for sorted arrays
    '''

    def __init__(self, array, key):
        self.array = array
        self.key = key
        self.low = 0
        self.high = len(self.array) - 1

    def binary_search(self):

        '''
        Function:
            Search if the key is present in the input array and return its
            index if it's present. None if it's not present
        '''

        if self.array == []:
            return

        middle = int((self.low + self.high)/2)

        if self.key == self.array[middle]:
            return middle

        elif self.low == self.high:
            return

        elif self.key > self.array[middle]:
            self.low = middle + 1
            return self.binary_search()

        else:
            self.high = middle - 1
            return self.binary_search()

# Testing
array = [2, 9, 16, 19, 23, 24, 29]
key = 24  # Expected output: 5
print(BinarySearch(array, key).binary_search())

key = 25  # Expected output: None
print(BinarySearch(array, key).binary_search())

key = 2  # Expected output: 0
print(BinarySearch(array, key).binary_search())

array = []
key = 54  # Expected output: None
print(BinarySearch(array, key).binary_search())

array = [4]
key = 4  # Expected output: 0
print(BinarySearch(array, key).binary_search())

'''
Theory:
    Priority queue is an abstract data structure in which every element is
    given a priroity order and elemenets are extracted in that given order.
    This implementation has been done using Binary max-Heap. A binary max-heap
    is a tree-like data structure in which the parent node takes values at
    least of their child nodes. Though the implementation is done in such a
    way that we don't require any parent/child pointers. All access can be
    done using array indexes.

For an alternative dictionary based implementation (where we keep each priority
value mapped to an element) check out BinaryMinHeap.py
'''


class BinaryMaxHeap:

    def __init__(self, max_size):
        self.max_size = max_size
        self.size = None
        self.heap = None

    def parent_index(self, idx):

        '''
        Function:
            For an input index, return the array index of its parent
        Input:
            idx (int): The index whose parent value we require
        Output:
            The parent index
        '''

        if idx != 0:
            return int((idx-1)/2)

        else:
            return idx

    def left_child_index(self, idx):

        '''
        Function:
            For an input index, return the array index of its left child
        Input:
            idx (int): The index whose left child value we require
        Output:
            The array index for the left child
        '''

        return 2*idx + 1

    def right_child_index(self, idx):

        '''
        Function:
            For an input index, return the array index of its right child
        Input:
            idx (int): The index whose right child value we require
        Output:
            The array index for the right child
        '''

        return 2*idx + 2

    def swap(self, idx1, idx2):

        '''
        Function:
            In the heap, swap the values present at idx1 and idx2
        Input:
            idx1, idx2 (int): The indexes whose values we want to interchange
        '''

        tmp = self.heap[idx1]
        self.heap[idx1] = self.heap[idx2]
        self.heap[idx2] = tmp

    def shift_up(self, idx):

        '''
        Function:
            If a heap value violates the max-heap property i.e. if the value is
            greater than that of its parent's value, we use this operation to
            place them at correct position by shifting the value up
        Input:
            idx (int): Array index of the value
        '''

        if self.heap is None:
            return

        curr_idx = idx

        while (curr_idx > 0) & (self.heap[curr_idx] >
                                self.heap[self.parent_index(curr_idx)]):
            self.swap(curr_idx, self.parent_index(curr_idx))
            curr_idx = self.parent_index(curr_idx)

    def shift_down(self, idx):

        '''
        Function:
            If a heap value violates the max-heap property i.e. if the value is
            lesser than that of either of its child's value, we use this
            operation to place them at correct position by shifting the value
            down
        Input:
            idx (int): Array index of the value
        '''

        if self.heap is None:
            return

        max_idx = idx
        left_child_idx = self.left_child_index(idx)

        if left_child_idx < self.size:
            if self.heap[max_idx] < self.heap[left_child_idx]:
                max_idx = left_child_idx

        right_child_idx = self.right_child_index(idx)

        if right_child_idx < self.size:
            if self.heap[max_idx] < self.heap[right_child_idx]:
                max_idx = right_child_idx

        if idx != max_idx:
            self.swap(idx, max_idx)
            self.shift_down(max_idx)

    def build_heap(self, array):

        '''
        Function:
            Given an empty heap, populate the values present in the input array
            at places such that the max-heap property is satistied at all
            levels
        Input:
            array (list): Values we want to populate the heap with
        '''

        if len(array) > self.max_size:
            self.heap = array[: self.max_size]

        else:
            self.heap = array

        self.size = len(self.heap)

        for idx in range(int(self.max_size/2) - 1, -1, -1):
            self.shift_down(idx)

    def insert(self, key):

        '''
        Function:
            Insert an input value into the heap such that the max-heap property
            isn't violdated
        Input:
            key (int): Value to be inserted
        '''

        if self.size == self.max_size:
            print('Heap already at max capacity!')
            return

        self.size += 1
        self.heap.append(key)
        self.shift_up(self.size - 1)

    def extract_max(self):

        '''
        Function:
            Return and remove the root node of the binary max heap
        Output:
            result (int): Value of the root node
        '''

        result = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.heap = self.heap[:-1]
        self.size -= 1
        self.shift_down(0)

        return result

    def get_max(self):

        '''
        Function:
            Return the root node without removing it
        Output:
            Value of the root node
        '''

        if self.size > 0:
            return self.heap[0]

        return

    def remove(self, idx):

        '''
        Function:
            Remove the value at an input array index without violating the max-
            heap property
        Input:
            idx (int): The array index whose value we want to remove
        '''

        self.heap[idx] = self.get_max() + 1
        self.shift_up(idx)
        self.extract_max()

    def change_priority(self, idx, new_key):

        '''
        Function:
            Change the existing priority of an input index to a new priority
        Input:
            idx (int): The array index of the element whose priority we want to
                        change
            new_key (int): The new priority of the element at the input index
        '''

        self.heap[idx] = new_key

        if self.heap[idx] > self.heap[self.parent_index(idx)]:
            self.shift_up(idx)

        else:
            self.shift_down(idx)

    def print_heap(self):
        print(self.heap)


def heap_sort(array):

    heap = BinaryMaxHeap(len(array))
    heap.build_heap(array)

    for i in range(heap.size):
        heap.swap(0, heap.size - 1)
        heap.size -= 1
        heap.shift_down(0)

    return heap.heap


def k_largest_elements(array, k):

    heap = BinaryMaxHeap(len(array))
    heap.build_heap(array)

    for i in range(k):
        print(heap.extract_max())

# Building a heap
heap = BinaryMaxHeap(max_size=15)
array = [76, 90, 113, 15, -7, 36, 64, 20]
heap.build_heap(array)
# Expected output: 113, 90, 76, 20, -7, 36, 64, 15
heap.print_heap()
# Inserting 107. Expected Output: 113, 107, 76, 90, -7, 36, 64, 15, 20
heap.insert(107)
heap.print_heap()
# Removing the root: 113. Expected output: 107, 90, 76, 20, -7, 36, 64, 15
heap.remove(0)  # Input is the index of the element to be removed
heap.print_heap()

heap.get_max()  # 107
# Changing -7 to 555, Expected output: 555, 107, 76, 20, 90, 36, 64, 15
heap.change_priority(idx=4, new_key=555)
heap.print_heap()
# Changing 555 to -75, Expected output: 107, 90, 76, 20, -75, 36, 64, 15
heap.change_priority(idx=0, new_key=-75)
heap.print_heap()

# Heap Sort
array = [107, 90, 76, 20, -75, 36, 64, 15]
sorted_array = heap_sort(array)
print(sorted_array)
k_largest_elements(array, k=5)

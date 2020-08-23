'''
Theory:
    Binary min heap is another data structure which can allow us to create a
    priority queue. It's a tree like structure for which the parent node must
    take a value smaller than its children nodes. Though the implementation is
    done in such a way that we don't require any parent/child pointers. All
    access can be done using array indexes.
'''


class BinaryMinHeap:

    def __init__(self, max_size):
        self.max_size = max_size
        self.size = None
        self.heap = []
        self.dict_mapping = {}  # A dictionary to map the values to nodes. Will
        # serve as helper function for Djikstra algorithm

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
            If a heap value violates the min-heap property i.e. if the value is
            lesser than that of its parent's value, we use this operation to
            place them at correct position by shifting the value up
        Input:
            idx (int): Array index of the value
        '''

        if self.heap is None:
            return

        curr_idx = idx

        while (curr_idx > 0) & (self.heap[curr_idx] <
                                self.heap[self.parent_index(curr_idx)]):

            self.swap(curr_idx, self.parent_index(curr_idx))
            curr_idx = self.parent_index(curr_idx)

    def shift_down(self, idx):

        '''
        Function:
            If a heap value violates the min-heap property i.e. if the value is
            greater than that of either of its child's value, we use this
            operation to place them at correct position by shifting the value
            down
        Input:
            idx (int): Array index of the value
        '''

        if self.heap is None:
            return

        min_idx = idx
        left_child_idx = self.left_child_index(idx)

        if left_child_idx < self.size:
            if self.heap[min_idx] > self.heap[left_child_idx]:
                min_idx = left_child_idx

        right_child_idx = self.right_child_index(idx)

        if right_child_idx < self.size:
            if self.heap[min_idx] > self.heap[right_child_idx]:
                min_idx = right_child_idx

        if idx != min_idx:
            self.swap(idx, min_idx)
            self.shift_down(min_idx)

    def build_heap(self, dict_mapping):

        '''
        Function:
            Given an empty heap, populate the values present in the input array
            at places such that the min-heap property is satistied at all
            levels
        Input:
            dict_mapping (dict): Mapping of the elements and their priorities
        '''

        self.dict_mapping = dict_mapping
        array = list(self.dict_mapping.values())

        if len(array) > self.max_size:
            self.heap = array[: self.max_size]
        else:
            self.heap = array

        self.size = len(self.heap)

        for idx in range(int(self.max_size/2) - 1, -1, -1):
            self.shift_down(idx)

    def insert(self, dict_key):

        '''
        Function:
            Insert an input value into the heap such that the min-heap property
            isn't violdated
        Input:
            dict_key (dict): Element mapped to its priority value. Eg. {'A': 5}
        '''

        if self.size == self.max_size:
            print('Heap already at max capacity!')
            return

        self.size += 1
        self.heap.append(list(dict_key.values())[0])
        self.dict_mapping.update(dict_key)
        self.shift_up(self.size - 1)

    def extract_min(self):

        '''
        Function:
            Return and remove the root node of the binary min heap
        Output:
            result (int): Value of the root node
        '''

        result = self.heap[0]

        for node_id, node_value in self.dict_mapping.items():
            if node_value == result:
                del(self.dict_mapping[node_id])
                break

        self.heap[0] = self.heap[self.size - 1]
        self.heap = self.heap[:-1]
        self.size -= 1
        self.shift_down(0)

        return result

    def get_min(self):

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
            Remove the value at an input array index without violating the min-
            heap property
        Input:
            idx (int): The array index whose value we want to remove
        '''

        for node_id, node_value in self.dict_mapping.items():

            if node_value == self.heap[idx]:
                del(self.dict_mapping[node_id])
                break

        self.heap[idx] = self.get_min() + 1
        self.shift_up(idx)
        self.extract_min()

    def change_priority(self, idx, new_key):

        '''
        Function:
            Change the existing priority of an input index to a new priority
        Input:
            idx (int): The array index of the element whose priority we want to
                        change
            new_key (int): The new priority of the element at the input index
        '''

        for node_id, node_value in self.dict_mapping.items():

            if node_value == self.heap[idx]:
                self.dict_mapping[node_id] = new_key
                break

        self.heap[idx] = new_key

        if self.heap[idx] < self.heap[self.parent_index(idx)]:
            self.shift_up(idx)
        else:
            self.shift_down(idx)

    def print_heap(self):
        print(self.heap)

# Building a heap
heap = BinaryMinHeap(max_size=15)
dict_mapping = {'A': 76, 'B': 90, 'C': 113, 'D': 15, 'E': -7, 'F': 36,
                'G': 64, 'H': 20}
array = list(dict_mapping.values())
heap.build_heap(dict_mapping)
# Expected output: -7, 15, 36, 20, 90, 113, 64, 76
heap.print_heap()

# Inserting 17. Expected Output: -7, 15, 36, 17, 90, 113, 64, 76, 20
heap.insert({'P': 17})
heap.print_heap()
# Removing the root: -7. Expected output: 15, 17, 36, 20, 90, 133, 64, 76
heap.remove(0)  # Input is the index of the element to be removed
heap.print_heap()

heap.get_min()  # 15
# Changing 17 to 186, Expected output: 15, 20, 36, 76, 90, 113, 64, 186
heap.change_priority(idx=1, new_key=186)
heap.print_heap()
# Changing 15 to 39, Expected output: 20, 39, 36, 76, 90, 113, 64, 186
heap.change_priority(idx=0, new_key=39)
heap.print_heap()

# Expected dict_mapping: {'A' : 76, 'B' : 90, 'C' : 113, 'D' : 39, 'F' : 36,
#                'G' : 64, 'H' : 20, 'P' : 186}
print(heap.dict_mapping)

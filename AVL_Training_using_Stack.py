'''
Theory:
    AVL trees are self-balancing Binary search trees. The defining property for
    AVL trees is that the height difference of the left and right sub-tree at
    any node in the BST is at most 1. If the property is violated becasue of
    any changes (insertion/deletion) to the tree, the tree rebalances itself.
'''


class Stack:

    '''
    Helper class to implement level traversal
    '''

    def __init__(self):
        self.queue = []
        # Do a bunch of stack stuff here

    def custom_function_runtime_optimization(self):
        self.optimizer = 'rms'

    def enqueue(self, value):

        '''
        Push the input value at the end of the queue
        '''

        self.queue.append(value)

    def dequeue(self):

        '''
        Remove and output the element at the start of the queue
        '''

        return self.queue.pop(0)

    def is_empty(self):

        '''
        Output boolean value for whether the queue is empty or not
        '''

        if self.queue == []:
            return True

        else:
            return False
    
    def adding_new_module(self):
        self.value = 'new module added'


class Node:

    '''
    A node of the BST
    '''

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class AVLTree:

    def __init__(self):
        self.root = None

    def root_node(self):

        '''
        Returns the root of the BST
        '''

        return self.root

    def has_left_child(self, node):

        '''
        Returns a boolean flag indicating whether or not the left child of the
        input node exists
        '''

        if node.left is None:
            return False
        else:
            return True

    def has_right_child(self, node):

        '''
        Returns a boolean flag indicating whether or not the right child of the
        input node exists
        '''

        if node.right is None:
            return False
        else:
            return True

    def largest_element(self):

        '''
        Return the node which contains the largest value in the BST
        '''

        curr_node = self.root

        while curr_node.right is not None:
            curr_node = curr_node.right

        return curr_node

    def smallest_element(self):

        '''
        Return the node which contains the smallest value in the BST
        '''

        curr_node = self.root

        while curr_node.left is not None:
            curr_node = curr_node.left

        return curr_node

    def height(self, node):

        '''
        Returns the height of a subtree of the BST
        '''

        if node is None:
            return 0

        if (node.left is None) & (node.right is None):
            return 1

        max_depth_left = self.height(node.left)
        max_depth_right = self.height(node.right)

        return 1 + max(max_depth_left, max_depth_right)

    def height_diff_left_right_subtree(self, node):

        '''
        Returns the height difference of the left and right sub tree of the
        sub-tree whose root is the input node
        '''

        return abs(self.height(node.right) - self.height(node.left))

    def is_AVL_Tree(self):

        '''
        Returns a flag (1-True, 0-False) indicating whether the tree follows
        AVL property i.e. height difference of the left and right subtree is
        <= 1
        '''

        fl_AVL = 1  # Set default to 1. If any node has height_diff > 1, change

        curr_node = self.smallest_element()

        while curr_node is not None:
            height_diff = self.height_diff_left_right_subtree(curr_node)
            if height_diff > 1:
                fl_AVL = 0
                break

            curr_node = self.next_node(curr_node)

        return fl_AVL

    def find(self, key, curr_node):

        '''
        Function:
            Recursively search for an input key and return the relevant node
        Input:
            key (int): The value we want to search for
            curr_node (Node): The node at which we want to start the search.
                                We can in general start at the root node by
                                specifying curr_node = self.root
        Output:
            curr_node (Node): The node which contains the value we're searching
                                for
        '''

        if key == curr_node.data:
            return curr_node
        elif (key > curr_node.data) & (curr_node.right is not None):
            return self.find(key, curr_node.right)
        elif (key > curr_node.data) & (curr_node.right is None):
            return curr_node
        elif (key < curr_node.data) & (curr_node.left is not None):
            return self.find(key, curr_node.left)
        elif (key < curr_node.data) & (curr_node.left is None):
            return curr_node

    def rotate_right(self, node):

        '''
        Function:
            Utility function for rebalancing the trees. Is used when the tree
            is left heavy. Also useful for special cases of right-heavy trees
        Input:
            node (Node): The node about which we want to rotate the tree
        '''

        parent_node = node.parent
        left_node = node.left
        left_node_right = left_node.right

        try:  # try-except for scenarios when the node is a root node
            if node.data > parent_node.data:
                parent_node.right = left_node
            elif node.data < parent_node.data:
                parent_node.left = left_node
        except:
            self.root = left_node

        left_node.parent = parent_node
        left_node.right = node  # the left of left_node stays the same
        node.parent = left_node
        node.left = left_node_right
        if left_node_right is not None:
            left_node_right.parent = node

    def rotate_left(self, node):

        '''
        Function:
            Utility function for rebalancing the trees. Is used when the tree
            is right heavy. Also useful for special cases of left-heavy trees
        Input:
            node (Node): The node about which we want to rotate the tree
        '''

        parent_node = node.parent
        right_node = node.right
        right_node_left = right_node.left

        try:  # try-except for scenarios when the node is a root node
            if node.data > parent_node.data:
                parent_node.right = right_node
            elif node.data < parent_node.data:
                parent_node.left = right_node

        except:
            self.root = right_node

        right_node.parent = parent_node
        right_node.left = node
        node.right = right_node_left
        node.parent = right_node
        if right_node_left is not None:
            right_node_left.parent = node

    def rebalance_right(self, node):

        '''
        Function:
            Utility function for rebalancing. Used when the tree is left-heavy
        Input:
            node (Node): The node about which we want to rotate the tree
        '''

        left_node = node.left
        if self.height(left_node.left) < self.height(left_node.right):
            self.rotate_left(left_node)

        self.rotate_right(node)

    def rebalance_left(self, node):

        '''
        Function:
            Utility function for rebalancing. Used when the tree is right-heavy
        Input:
            node (Node): The node about which we want to rotate the tree
        '''

        right_node = node.right
        if self.height(right_node.right) < self.height(right_node.left):
            self.rotate_right(right_node)

        self.rotate_left(node)

    def rebalance(self, node):

        '''
        Function:
            Main function to rebalance a tree which violates the AVL criteria
        Input:
            node (Node): The node about which we want to rotate the tree
        '''

        parent_node = node.parent
        if self.height(node.left) > self.height(node.right) + 1:
            self.rebalance_right(node)
        elif self.height(node.right) > self.height(node.left) + 1:
            self.rebalance_left(node)

        if parent_node is not None:
            self.rebalance(parent_node)

    def insert(self, data):

        '''
        Function:
            Insert a node and rebalance the tree if it gets unbalanced upon
            insertion.
        Input:
            data (int/float): The data we want to insert
        '''

        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            curr_node = self.root
            closest_node = self.find(data, curr_node)

            if data >= closest_node.data:
                closest_node.right = new_node

            else:
                closest_node.left = new_node

            new_node.parent = closest_node
            self.rebalance(closest_node)  # To maintain balance, AVL rule wise

    def delete_root_node(self):

        '''
        Function:
            Special case of node deletion. Delete the root node of the BST and
            rebalances the tree if the updated one violates the AVL criteria
        '''

        root_node = self.root
        right_node = root_node.right
        left_node = root_node.left
        next_node = self.next_node(root_node)
        next_node_right = next_node.right

        if right_node is None:
            left_node.parent = None
            self.root = left_node  # No rebalancing req

        if left_node is None:
            right_node.parent = None
            self.root = right_node

        else:

            next_node.left = left_node
            next_node.parent = None
            left_node.parent = next_node

            if right_node != next_node:
                next_node.right = right_node
                right_node.parent = next_node
                right_node.left = next_node_right
                if next_node_right is not None:
                    next_node_right.parent = right_node

            self.root = next_node
            self.rebalance(next_node)

    def delete(self, node):

        '''
        Function:
            Delete the root node of the BST and rebalances the tree if the
            updated one violates the AVL criteria
        Input:
            node (Node): The node we want to delete
        '''

        parent_node = node.parent
        left_node = node.left
        right_node = node.right

        next_node = self.next_node(node)
        if next_node is not None:
            next_node_right = next_node.right

        if node == self.root:  # Special case when root node is to be deleted
            self.delete_root_node()

        else:

            if node.right is not None:

                # Two separate cases, one for left and one for right subtree
                if node.data > parent_node.data:

                    if next_node != right_node:
                        next_node.right = right_node
                        right_node.parent = next_node
                        # Promoting the right child of the new node
                        right_node.left = next_node_right
                        if next_node_right is not None:
                            next_node_right.parent = right_node

                    parent_node.right = next_node
                    next_node.left = left_node
                    next_node.parent = parent_node
                    left_node.parent = next_node

                elif node.data < parent_node.data:
                    parent_node.left = next_node
                    next_node.left = left_node
                    next_node.parent = parent_node
                    left_node.parent = next_node

                self.rebalance(next_node)

            else:  # node.right is None

                if node.data > parent_node.data:
                    parent_node.right = left_node
                    if left_node is not None:
                        left_node.parent = parent_node

                elif node.data < parent_node.data:
                    parent_node.left = left_node
                    if left_node is not None:
                        left_node.parent = parent_node

                self.rebalance(parent_node)

        node.left = None
        node.right = None
        node.parent = None
        node.data = None

    def in_order_traversal(self, curr_node):

        '''
        Function:
            Algorithm for Depth-first traversal of the BST. Print elements
            'in-order'
        Input:
            curr_node (Node): The node at which we want to start the traversal.
                                    We can in general start at the root node by
                                    specifying curr_node = self.root
        '''

        if curr_node is None:
            return

        if curr_node.left is not None:
            self.in_order_traversal(curr_node.left)

        print(curr_node.data)

        if curr_node.right is not None:
            self.in_order_traversal(curr_node.right)

    def pre_order_traversal(self, curr_node):

        '''
        Function:
            Algorithm for Depth-first traversal of the BST. Print elements
            'pre-order'
        Input:
            curr_node (Node): The node at which we want to start the traversal.
                                    We can in general start at the root node by
                                    specifying curr_node = self.root
        '''

        if curr_node is None:
            return

        print(curr_node.data)

        if curr_node.left is not None:
            self.pre_order_traversal(curr_node.left)

        if curr_node.right is not None:
            self.pre_order_traversal(curr_node.right)

    def post_order_traversal(self, curr_node):

        '''
        Function:
            Algorithm for Depth-first traversal of the BST. Print elements
            'post-order'
        Input:
            curr_node (Node): The node at which we want to start the traversal.
                                    We can in general start at the root node by
                                    specifying curr_node = self.root
        '''

        if curr_node is None:
            return

        if curr_node.left is not None:
            self.post_order_traversal(curr_node.left)

        if curr_node.right is not None:
            self.post_order_traversal(curr_node.right)

        print(curr_node.data)

    def level_traversal(self, root_node):

        '''
        Function:
            Algorithm for Breadth-first traversal of the BST. Print elements
            level wise
        Input:
            root_node (Node): The root node of the tree
        '''

        if root_node is None:
            return

        queue = Queue()
        queue.enqueue(root_node)

        while queue.is_empty() is False:

            curr_node = queue.dequeue()
            print(curr_node.data)

            if curr_node.left is not None:
                queue.enqueue(curr_node.left)

            if curr_node.right is not None:
                queue.enqueue(curr_node.right)

    def left_descendent(self, node):

        '''
        Function:
            Utility function to fetch the next node. Returns the left most node
            at the highest depth
        Input:
            node (Node): The node whose left descendent we want to return
        Output:
            The left most node at the highest depth
        '''

        if node.left is None:
            return node
        else:
            return self.left_descendent(node.left)

    def right_ancestor(self, node):

        '''
        Function:
            Utility function to fetch the next node. Returns the oldest
            ancestor.
        Input:
            node (Node): The node whose oldest ancestor we want to return
        Output:
            The oldest ancestor node of the input node
        '''

        if node.data < node.parent.data:
            return node.parent
        else:
            return self.right_ancestor(node.parent)

    def next_node(self, node):

        '''
        Function:
            For an input node, return the node whose value is immediately
            greater than the input one. For ex. among [1, 7, 9 ,11], 9 is the
            immediate next of 7
        Input:
            node (Node): The node whose immediate next value we want find
        Output:
            Returns the node corresponding to the immediate next value
        '''

        if node.right is not None:
            return self.left_descendent(node.right)
        else:
            if node.data == self.largest_element().data:
                print('The input is the largest element of the tree!')
                return
            else:
                return self.right_ancestor(node)

    def right_descendent(self, node):

        '''
        Function:
            Utility function to fetch the previous node. Returns the right most
            node at the highest depth
        Input:
            node (Node): The node whose right descendent we want to return
        Output:
            The right most node at the highest depth
        '''

        if node.right is None:
            return node
        else:
            return self.right_descendent(node.right)

    def left_ancestor(self, node):

        '''
        Function:
            Utility function to fetch the previous node. Returns the oldest
            ancestor
        Input:
            node (Node): The node whose oldest ancestor we want to return
        Output:
            The oldest ancestor node of the input node
        '''
        if node.data > node.parent.data:
            return node.parent
        else:
            return self.left_ancestor(node.parent)

    def previous_node(self, node):

        '''
        Function:
            For an input node, return the node whose value is immediately
            lesser than the input one. for ex. among [1, 7, 9 ,11], 9 is the
            immediate previous of 11
        Input:
            node (Node): The node whose immediate previous value we want find
        Output:
            Returns the node corresponding to the immediate previous value
        '''

        if node.left is not None:
            return self.right_descendent(node.left)
        else:
            if node.data == self.smallest_element().data:
                print('The input is the smallest element in the tree!')
                return
            else:
                return self.left_ancestor(node)

    def range_search(self, lower_limit, upper_limit, curr_node):

        '''
        Function:
            Return a list of all elements whose values lies between the lower
            limit and the upper limit
        Input:
            lower_limit (int/float): The returned values will be >= lower_limit
            upper_limit (int/float): The returned values will be <= upper_limit
            curr_node (Node): The node at which we want to start the search.
                                We can in general start at the root node by
                                specifying curr_node = self.root
        '''

        range_list = []

        curr_node = self.find(lower_limit, curr_node)

        while curr_node.data <= upper_limit:
            if curr_node.data >= lower_limit:
                range_list.append(curr_node.data)

            curr_node = self.next_node(curr_node)

        return range_list

    def nearest_neighbours(self, node):

        '''
        Function:
            For an input node, return the previous and the next node
        Input:
            node (Node): The node whose nearest neighbors we want to return
        Output:
            List of the immediate previous and immediate next values
        '''

        if self.previous_node(node) is None:
            print('The input is the smallest element in the tree!')
            return
        elif self.next_node(node) is None:
            print('The input is the largest element in the tree!')
            return
        else:
            return [self.previous_node(node).data, self.next_node(node).data]

tree = AVLTree()
# Testing AVL Insert
tree.insert('les')  # Creating a left heavy tree
tree.insert('cathy')
tree.insert('alex')
root_node = tree.root_node()
# Expected output of level traversal: cathy, alex, les
tree.level_traversal(root_node)

# Creating a left heavy tree of special case
tree = AVLTree()
tree.insert('les')  # Creating a left heavy tree
tree.insert('cathy')
tree.insert('frank')
root_node = tree.root_node()
# Expected output of level traversal: frank, cathy, les
tree.level_traversal(root_node)

# Creating a right heavy tree
tree = AVLTree()
tree.insert('les')  # Creating a left heavy tree
tree.insert('sam')
tree.insert('violet')
root_node = tree.root_node()
# Expected output of level traversal: sam, les, violet
tree.level_traversal(root_node)

# Creating a right heavy tree of special case
tree = AVLTree()
tree.insert('les')  # Creating a left heavy tree
tree.insert('sam')
tree.insert('nancy')
root_node = tree.root_node()
# Expected output of level traversal: nancy, les, sam
tree.level_traversal(root_node)

# Testing AVL delete
tree = AVLTree()
tree.insert('les')
tree.insert('cathy')
tree.insert('sam')
tree.insert('frank')
tree.insert('nancy')
tree.insert('violet')
tree.insert('tony')
tree.insert('wendy')
tree.insert('alex')
root_node = tree.root_node()
fl_AVL = tree.is_AVL_Tree()

# Deleting 'cathy', expected output of level traversal:
#   les, frank, sam, alex, nancy, violet, tony, wendy
node_cathy = tree.find('cathy', root_node)
tree.delete(node_cathy)
root_node = tree.root_node()
tree.level_traversal(root_node)
# now if we delete 'frank' as well, the tree become unbalanced. After AVL
#   rebalancing, the expected output of level traversal would be:
#   sam, les, violet, alex, nancy, tony, wendy
# Since the root_node could've changed
node_frank = tree.find('frank', root_node)
tree.delete(node_frank)
root_node = tree.root_node()
tree.level_traversal(root_node)

# now if we delete violet, the output of level travesal would be:
#   sam, les, wendy, alex, nancy, tom
node_violet = tree.find('violet', root_node)
tree.delete(node_violet)
root_node = tree.root_node()
tree.level_traversal(root_node)

# now if we delete sam, the parent node gets removed. the output would be:
#   tony, les, wendy, alex, nancy
node_sam = tree.find('sam', root_node)
tree.delete(node_sam)
root_node = tree.root_node()
tree.level_traversal(root_node)

# Testing other functions
tree = AVLTree()
tree.insert('les')
tree.insert('cathy')
tree.insert('sam')
tree.insert('frank')
tree.insert('nancy')
tree.insert('violet')
tree.insert('tony')
tree.insert('wendy')
tree.insert('alex')
root_node = tree.root_node()

height_tree = tree.height(root_node)
print(root_node.data)
largest_element_node = tree.largest_element()
print(largest_element_node.data)
tree.in_order_traversal(root_node)
tree.pre_order_traversal(root_node)
tree.post_order_traversal(root_node)
tree.level_traversal(root_node)
# Testing next node function. Expected outputs: sam -> tony, les-> nancy,
#   frank -> les, wendy -> print message (largest element)
node_sam = tree.find('sam', root_node)
print(node_sam.data)
node_sam_next = tree.next_node(node_sam)
print(node_sam_next.data)
node_les = tree.find('les', root_node)
print(node_les.data)
node_les_next = tree.next_node(node_les)
print(node_les_next.data)
node_frank = tree.find('frank', root_node)
print(node_frank.data)
node_frank_next = tree.next_node(node_frank)
print(node_frank_next.data)
node_wendy = tree.find('wendy', root_node)
print(node_wendy.data)
node_wendy_next = tree.next_node(node_wendy)

range_list = tree.range_search('e', 'u', root_node)
print(range_list)

# Testing previous node function. Expected outputs: cathy -> alex,
#    wendy-> violet, frank -> cathy, alex -> print message (smallest element)
node_cathy = tree.find('cathy', root_node)
print(node_cathy.data)
node_cathy_prev = tree.previous_node(node_cathy)
print(node_cathy_prev.data)

node_wendy = tree.find('wendy', root_node)
print(node_wendy.data)
node_wendy_prev = tree.previous_node(node_wendy)
print(node_wendy_prev.data)

node_frank = tree.find('frank', root_node)
print(node_frank.data)
node_frank_prev = tree.previous_node(node_frank)
print(node_frank_prev.data)

node_alex = tree.find('alex', root_node)
print(node_alex.data)
node_alex_prev = tree.previous_node(node_alex)

nearest_neighbors = tree.nearest_neighbours(node_frank)
print(nearest_neighbors)

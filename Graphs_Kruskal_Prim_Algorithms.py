'''
Theory:
    Kruskal and Prim algorithms are used to find the optimum total cost in a
    minimum spanning tree. A minimum spanning tree is a subset of the edges of
    a undirected graph in which each edge is associated with a weight. The
    edges are shortlisted so as to optimize the total cost of connecting all
    the vertices
'''


class DisjointSet:

    '''
    Helper class for Kruskal's algorithm
    '''

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, i):

        '''
        Function:
            For an input value i, make a disjoint set comprising of just that
            value
        Input:
            i: The value whose set we want to create
        '''

        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i):

        '''
        Function:
            Each set is associated with an ID. Return the ID for the input val
        Input:
            i: The value whose set ID we want to return
        Output:
            The corresponding set ID
        '''

        while i != self.parent[i]:
            i = self.parent[i]

        return i

    def union(self, i, j):

        '''
        Function:
            Combine the two sets which contain the elements i and j into a
            single set
        Input:
            i, j: The values whose sets we want to combine into one
        '''

        i_id = self.find(i)
        j_id = self.find(j)

        rank_i_id = self.rank[i]
        rank_j_id = self.rank[j]

        if rank_i_id > rank_j_id:
            self.parent[j_id] = i_id

        else:
            self.parent[i_id] = j_id
            if rank_i_id == rank_j_id:
                self.rank[j_id] += 1


class BinaryMinHeap:

    '''
    Helper class for Prim's algorithm
    '''

    def __init__(self, max_size):

        self.max_size = max_size
        self.size = None
        self.heap = []
        self.dict_mapping = {}  # A dictionary to map the values to nodes. Will
        # serve as helper function for Djikstra algorithm

    def is_empty(self):

        '''
        Output boolean value for whether the min-heap is empty or not
        '''

        if self.heap == []:
            return True

        else:
            return False

    def parent_index(self, idx):

        '''
        For an input index, return the array index of its parent
        '''

        if idx != 0:
            return int((idx-1)/2)

        else:
            return idx

    def left_child_index(self, idx):

        '''
        For an input index, return the array index of its left child
        '''

        return 2*idx + 1

    def right_child_index(self, idx):

        '''
        For an input index, return the array index of its right child
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

    def extract_min(self):

        '''
        Function:
            Return and remove the root node of the binary min heap
        Output:
            result (int): Value of the root node
        '''

        for node_id, node_value in self.dict_mapping.items():
            if node_value == self.heap[0]:
                result = {node_id: node_value}
                del(self.dict_mapping[node_id])
                break

        self.heap[0] = self.heap[self.size - 1]
        self.heap = self.heap[:-1]
        self.size -= 1
        self.shift_down(0)

        return result

    def get_index(self, node_id):

        '''
        Get the heap array index for a input node key
        '''

        node_value = self.dict_mapping[node_id]
        idx = 0

        for val in self.heap:
            if val == node_value:
                return idx

            idx += 1

    def change_priority(self, node_id, new_key):

        '''
        Function:
            Change the existing priority of an input index to a new priority
        Input:
            node_id (str): The node key whose priority needs to be changed
            new_key (int): The new priority of the element at the input index
        '''

        idx = self.get_index(node_id)

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
        print(self.dict_mapping)


class Graph:

    def __init__(self, dict_graph):

        self.dict_graph = dict_graph  # Edge tuple as key, its weight as
        # value. Ex- # If an edge of weight 5 is there between A and B we
        # specify {(A, B) : 5}. Check more examples at the end of the script.

    def get_list_vertices(self):

        '''
        Returns the list of vertices present in the input graph.
        '''

        list_vertices = []

        for edge in list(self.dict_graph.keys()):
            list_vertices.append(edge[0])
            list_vertices.append(edge[1])

        list_vertices = list(set(list_vertices))

        return list_vertices

    def get_list_edges(self):

        '''
        Returns the list of directed edges present in the input graph.
        '''

        return list(self.dict_graph.keys())

    def get_list_neighbors(self, vertex):

        '''
        Return a list of vertices to which the input vertex is connected with
        '''

        list_neighbors = []

        for edge in list(self.dict_graph.keys()):
            if edge[0] == vertex:
                list_neighbors.append(edge[1])

            elif edge[1] == vertex:  # Undirected graph so processing both ways
                list_neighbors.append(edge[0])

        return list_neighbors

    def kruskal(self):

        '''
        Function:
            Algorithm to find the optimum total cost of connecting all the
            vertices of a minimum spanning tree. It works by repeatedly adding
            the lightest edge if it doesn't produces a cycle
        Output:
            connections_list (list): A list of tuples. Each tuple contain a
                                    pair of edges whose connection leads to the
                                    optimum total cost
            total_cost (int/float): Sum of the costs of the connected edges
        '''

        dis_set_vertices = DisjointSet()

        for vertex in self.get_list_vertices():
            dis_set_vertices.make_set(vertex)

        connections_list = []
        total_cost = 0

        dict_graph_sorted = {k: v for k, v in sorted(self.dict_graph.items(),
                                                     key=lambda x: x[1])}

        for edge in list(dict_graph_sorted.keys()):
            if dis_set_vertices.find(edge[0]) != \
                    dis_set_vertices.find(edge[1]):

                dis_set_vertices.union(edge[0], edge[1])
                connections_list.append((edge[0], edge[1]))
                total_cost += self.dict_graph[(edge[0], edge[1])]

        return connections_list, total_cost

    def prim(self):

        '''
        Function:
            Algorithm to find the optimum total cost of connecting all the
            vertices of a minimum spanning tree. It works by repeatedly
            attaching a new vertex to the current tree by the lightest edge
        Output:
            connections_list (list): A list of tuples. Each tuple contain a
                                    pair of edges whose connection leads to the
                                    optimum total cost
            total_cost (int/float): Sum of the costs of the connected edges
        '''

        dict_cost = {}
        dict_parent = {}

        extra = 0  # To make sure no two vertices have the same cost if they've
        #  not been found. Incremental variable

        for vertex in self.get_list_vertices():
            dict_cost[vertex] = len(self.get_list_vertices()) + 1000 + extra
            dict_parent[vertex] = None
            extra += 1

        origin = self.get_list_vertices()[0]  # Can be set to any other as well
        dict_cost[origin] = 0

        priority_queue_cost = BinaryMinHeap(len(self.get_list_vertices()))
        priority_queue_cost.build_heap(dict_cost.copy())

        while priority_queue_cost.is_empty() is False:
            curr_vertex = list(priority_queue_cost.extract_min().keys())[0]
            list_neighbors = self.get_list_neighbors(curr_vertex)

            for neighbor in list_neighbors:
                # Undirected graph, so order doesn't matter
                if (curr_vertex, neighbor) in self.dict_graph:
                    edge_cost = self.dict_graph[(curr_vertex, neighbor)]

                else:
                    edge_cost = self.dict_graph[(neighbor, curr_vertex)]

                if (neighbor in list(priority_queue_cost.dict_mapping.keys()))\
                        & (dict_cost[neighbor] > edge_cost):

                    dict_cost[neighbor] = edge_cost
                    dict_parent[neighbor] = curr_vertex
                    priority_queue_cost.change_priority(neighbor, edge_cost)

        total_cost = sum(list(dict_cost.values()))
        connections_list = []

        for vertex1 in list(dict_cost.keys()):
            for vertex2, parent in dict_parent.items():
                if parent == vertex1:
                    connections_list.append((vertex2, parent))

        return connections_list, total_cost

dict_graph = {}
dict_graph[('A', 'B')] = 4
dict_graph[('A', 'D')] = 2
dict_graph[('A', 'E')] = 1
dict_graph[('B', 'C')] = 8
dict_graph[('B', 'E')] = 5
dict_graph[('B', 'F')] = 6
dict_graph[('C', 'F')] = 1
dict_graph[('D', 'E')] = 3
dict_graph[('E', 'F')] = 9

undirected_graph = Graph(dict_graph)
# Expected output : Cost-14, Connections- [(A,B), (A,D), (A,E), (B,F), (C,F)]
# Note that the vertices could appear in reverse, since it's an undirected
# graph
connections_list_kr, total_cost_kr = undirected_graph.kruskal()
print(total_cost_kr)
print(connections_list_kr)

connections_list_pr, total_cost_pr = undirected_graph.prim()
print(total_cost_pr)
print(connections_list_pr)

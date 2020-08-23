'''
Theory:
    Dijkstra and Bellman-Ford algorithms can be used to find the fastest routes
    in graph representations. For Dijkstra, we can't supply negative edge
    weights as input. Bellman-Ford can be used to solve such problems as long
    as there aren't any negative cycles in the graph.
'''


class BinaryMinHeap:

    '''
    Helper class for Dijkstra
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
        self.dict_graph = dict_graph  # Edge tuple as key, time distance as
        # value. Ex- # If an edge of weight 5 goes from A to B we specify
        # {(A, B) : 5}. Check more examples at the end of the script.

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
        Return a list of vertices to which the input vertex points towards
        '''

        list_neighbors = []
        for edge in list(self.dict_graph.keys()):
            if edge[0] == vertex:  # It's a directed graph, so
                                                # reverse edges not processed
                list_neighbors.append(edge[1])

        return list_neighbors

    def dijkstra(self, origin):

        '''
        Function:
            Algorithm to find the fastest paths from an input origin to the
            rest of the vertices. All edge weights must be positive
        Input:
            origin (str): The origin vertex
        Output:
            dict_distance (dict): A dictionary containing the vertices as the
                                    keys and their fasted distance from origin
                                    as the value
            dict_previous_vertex (dict): A dictionary mapping the vertices to
                                    their immediate previous vertices. Helps
                                    reconstruct the fastest path found.
        '''

        dict_distance = {}
        dict_previous_vertex = {}
        extra = 0  # To make sure no two vertices have the same distance from
        # origin if they've not been found. Incremental variable

        for vertex in self.get_list_vertices():
            dict_distance[vertex] = len(self.get_list_vertices()) + 1000 + \
                                                                        extra
            dict_previous_vertex[vertex] = None
            extra += 1

        dict_distance[origin] = 0
        priority_queue_distances = BinaryMinHeap(len(self.get_list_vertices()))
        priority_queue_distances.build_heap(dict_distance.copy())

        while priority_queue_distances.is_empty() is False:

            min_vertex = list(priority_queue_distances.extract_min().keys())[0]
            list_neighbors = self.get_list_neighbors(min_vertex)

            for neighbor in list_neighbors:

                if dict_distance[neighbor] > dict_distance[min_vertex] +\
                                self.dict_graph[(min_vertex, neighbor)]:

                    dict_distance[neighbor] = dict_distance[min_vertex] +\
                                self.dict_graph[(min_vertex, neighbor)]

                    priority_queue_distances.change_priority(
                                                    neighbor,
                                                    dict_distance[neighbor])
                    dict_previous_vertex[neighbor] = min_vertex

        return dict_distance, dict_previous_vertex

    def get_fastest_path(self, origin, destination):

        '''
        Function:
            Output the fastest path from the origin to the destination node
            by running Dijkstra's algorithm over the input graph
        Input:
            origin_node (str): The origin vertex
            destination_node (str): The destination vertex
        Output:
            A list of the vertices through which the destination is reached
        '''

        dict_distance, dict_previous_vertex = self.dijkstra(origin)
        fastest_path_reverse = [destination]

        curr_vertex = destination
        while dict_previous_vertex[curr_vertex] is not None:
            fastest_path_reverse.append(dict_previous_vertex[curr_vertex])
            curr_vertex = dict_previous_vertex[curr_vertex]

        return fastest_path_reverse[::-1]

    def bellman_ford(self, origin):

        '''
        Function:
            Algorithm to find the fastest paths from an input origin to the
            rest of the vertices without the restriction of positive edges.
            However, there must not be any negative cycles in the graph.
        Input:
            origin (str): The origin vertex
        Output:
            dict_distance (dict): A dictionary containing the vertices as the
                                    keys and their fastest distance from origin
                                    as the value
            dict_previous_vertex (dict): A dictionary mapping the vertices to
                                    their immediate previous vertices. Helps
                                    reconstruct the fastest path found.
        '''

        dict_distance = {}
        dict_previous_vertex = {}
        extra = 0  # To make sure no two vertices have the same distance from
        # origin if they've not been found. Incremental variable

        for vertex in self.get_list_vertices():
            dict_distance[vertex] = len(self.get_list_vertices()) + 1000 + \
                                                                        extra
            dict_previous_vertex[vertex] = None
            extra += 1

        dict_distance[origin] = 0
        iter_num = 1
        list_edges = self.get_list_edges()

        while iter_num < len(self.get_list_vertices()) + 1:  # +1 to detect
            # negative cycles if any
            for edge in list_edges:
                start_vertex = edge[0]
                end_vertex = edge[1]

                if dict_distance[end_vertex] > dict_distance[start_vertex] +\
                        self.dict_graph[edge]:

                    dict_distance[end_vertex] = dict_distance[start_vertex] +\
                                                    self.dict_graph[edge]

                    dict_previous_vertex[end_vertex] = start_vertex

            # Detecting presence of a negative cycle, if it's there break
            if iter_num == len(self.get_list_vertices()) - 1:
                dict_distance_last_step = dict_distance.copy()

            if iter_num == len(self.get_list_vertices()):
                dict_distance_last_plus_1_step = dict_distance.copy()

                if dict_distance_last_step != dict_distance_last_plus_1_step:
                    print("There's a negative cycle in the graph!")
                    return

            iter_num += 1

        return dict_distance, dict_previous_vertex

# If an edge of weight 5 goes from A to B we specify {(A, B) : 5}
dict_graph = {}
dict_graph[('S', 'A')] = 3
dict_graph[('S', 'B')] = 10
dict_graph[('A', 'B')] = 8
dict_graph[('A', 'C')] = 3
dict_graph[('A', 'D')] = 5
dict_graph[('B', 'A')] = 2
dict_graph[('B', 'D')] = 5
dict_graph[('C', 'B')] = 3
dict_graph[('C', 'D')] = 1
dict_graph[('C', 'E')] = 2
dict_graph[('D', 'E')] = 0

directed_graph = Graph(dict_graph)
# Expected output: S-0, A-3, B-9, C-6, D-7, E-7
dict_distance_dj, dict_previous_vertex_dj = directed_graph.dijkstra('S')
print(dict_distance_dj)
# Expected output: S, A, C, D, E
fastest_path = directed_graph.get_fastest_path('S', 'E')
print(fastest_path)

# For negative , use Bellman Ford algorithm
dict_graph = {}
dict_graph[('S', 'A')] = 4
dict_graph[('S', 'B')] = 3
dict_graph[('A', 'B')] = -2
dict_graph[('A', 'C')] = 4
dict_graph[('B', 'C')] = -3
dict_graph[('B', 'D')] = 1
dict_graph[('C', 'D')] = 2

directed_graph = Graph(dict_graph)
# Expected output:
# S:0, A:4, B:2, C:-1, D: 1
dict_distance_bf, dict_previous_vertex_bf = directed_graph.bellman_ford('S')
print(dict_distance_bf)

# Test case with a negative cycle (B-C-D)
dict_graph = {}
dict_graph[('S', 'A')] = 4
dict_graph[('S', 'B')] = 3
dict_graph[('A', 'B')] = -2
dict_graph[('A', 'C')] = 4
dict_graph[('B', 'C')] = -3
dict_graph[('C', 'D')] = 2
dict_graph[('D', 'B')] = -10

directed_graph = Graph(dict_graph)
# Expected output:
# S:0, A:4, B:2, C:-1, D: 1
directed_graph.bellman_ford('S')

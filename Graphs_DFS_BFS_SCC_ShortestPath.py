'''
Theory:
    Graphs represent connections between objects like internet (websites
    connected to each other, maps- points connected by roads, social networks).
    In this script, we implement basic algorithms for exploring and finding
    shorted distances in undirected and directed graphs. In addition to DFS and
    BFS, we also implement programs to fetch list of strongly connected
    components, implement topological sort and reconstruct shortest paths
    between two vertices. Examples for using the script are provided at the end
'''


class Queue:

    '''
    Helper class for breadth first search
    '''

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

        return self.queue.pop(0)

    def is_empty(self):

        '''
        Output boolean value for whether the queue is empty or not
        '''

        if self.queue == []:
            return True
        else:
            return False


class Graph:

    def __init__(self, dict_graph):

        '''
        Ex: {'A': ['B', 'C']}.
        For a directed graph it would mean A points to both B and C, however,
        they don't point to A. For an undirected graph, it would mean B and C
        are neighbors of A. Make sure to specify {'B' : ['A'], 'C': ['A']} as
        well in that scenario. See example at the end of script.
        '''

        self.dict_graph = dict_graph

    def get_list_vertices(self, dict_graph):

        '''
        Returns the list of vertices present in the input graph. If the list
        for the default graph is required, specify dict_graph = self.dict_graph
        '''

        return list(dict_graph.keys())

    def get_list_edges(self, dict_graph):

        '''
        Returns the list of edges present in the input graph. If the list
        for the default graph is required, specify dict_graph = self.dict_graph
        '''

        list_edges = []

        for start_vertex, list_end_vertices in dict_graph.items():
            for end_vertex in list_end_vertices:
                list_edges.append([start_vertex, end_vertex])

        return list_edges

    def explore_vertex(self, vertex, dict_graph, dict_dfs_info):

        '''
        Function:
            Helper function for DFS. Recursively explore the input vertex and
            its neighbors. Also keeps track of the connected components and the
            pre, post-visit clocks for the vertices
        Input:
            vertex (str): Vertex to explore
            dict_graph (dict): The graph to which the vertex belongs. If we
                                want to search in the main graph, specify
                                dict_graph = self.dict_graph
            dict_dfs_info (dict): Originates from the depth_first_search
                                    function. Keeps track of the connected
                                    components and the pre, post-visit clocks
                                    for the vertices
        Output:
            dict_dfs_info (dict): The updated dictionary
        '''

        dict_dfs_info['dict_previsit_clock'][vertex] = dict_dfs_info['clock']
        dict_dfs_info['clock'] += 1
        dict_dfs_info['dict_visited'][vertex] = 1
        dict_dfs_info['connected_component'][vertex] = dict_dfs_info['cc']
        list_neighbors_vertices = dict_graph.get(vertex)

        for neighbor_vertex in list_neighbors_vertices:
            if dict_dfs_info['dict_visited'][neighbor_vertex] == 0:
                dict_dfs_info = self.explore_vertex(neighbor_vertex,
                                                    dict_graph, dict_dfs_info)

        dict_dfs_info['dict_postvisit_clock'][vertex] = dict_dfs_info['clock']
        dict_dfs_info['clock'] += 1

        return dict_dfs_info

    def depth_first_search(self, dict_graph):

        '''
        Function:
            Algorithm to explore the entire graph. label connected components
            and keep track of the pre/post visit clocks of the exploration
        Input:
            dict_graph (dict): The graph which we want to explore. If we
                                want to explore the default graph, specify
                                dict_graph = self.dict_graph
        Output:
            dict_dfs_info (dict): Dictionary containing details of the
                                    connected components and the pre/post visit
                                    clocks for the vertices
        '''

        dict_dfs_info = {}
        dict_dfs_info['dict_visited'] = {}

        for vertex in self.get_list_vertices(dict_graph):
            dict_dfs_info['dict_visited'][vertex] = 0

        dict_dfs_info['dict_previsit_clock'] = {}
        dict_dfs_info['dict_postvisit_clock'] = {}
        dict_dfs_info['cc'] = 1
        dict_dfs_info['connected_component'] = {}
        dict_dfs_info['clock'] = 1

        for vertex in self.get_list_vertices(dict_graph):
            if dict_dfs_info['dict_visited'][vertex] == 0:
                dict_dfs_info = self.explore_vertex(vertex, dict_graph,
                                                    dict_dfs_info)
                dict_dfs_info['cc'] += 1

        return dict_dfs_info

    def topological_sort(self, dict_graph):

        '''
        Function:
            Derive a linear order of the vertices for a directed graph. The
            ordering is done in the decending order of the post-visit clocks
        Input:
            dict_graph (dict): The dictionary for the directed graph
        Output:
            A list of the linearly ordered vertices
        '''

        dict_dfs_info = self.depth_first_search(dict_graph)
        dict_postvisit_clock = dict_dfs_info['dict_postvisit_clock']

        dict_postvisit_clock = sorted(dict_postvisit_clock.items(),
                                      key=lambda x: x[1], reverse=True)

        return list(dict_postvisit_clock.keys())

    def reverse_graph(self, dict_graph):

        '''
        Function:
            For a directed graph, obtain a graph with reversed directions
        Input:
            dict_graph (dict): The dictionary for the directed graph
        Output:
            reverse_graph (dict): The dictionary for the directed reverse graph
        '''

        list_edges = self.get_list_edges(dict_graph)
        list_edges_reversed = []

        for edge in list_edges:
            list_edges_reversed.append([edge[1], edge[0]])

        list_vertices = self.get_list_vertices(dict_graph)
        reverse_graph = {}

        for vertex in list_vertices:
            reverse_graph[vertex] = []
            for edge_reverse in list_edges_reversed:
                if edge_reverse[0] == vertex:
                    reverse_graph[vertex].append(edge_reverse[1])

        return reverse_graph

    def remove_vertex(self, vertex, dict_graph):

        '''
        Function:
            Helper function to fetch the strongly connected components of a
            directed graph. Removes the input vertex and outputs the updated
            dictionary
        Input:
            vertex (str): The vertex we want to delete
            dict_graph (str): The graph from which we want to delete the vertex
        Output:
            dict_graph (dict): The updated graph representation
        '''

        del(dict_graph[vertex])

        for vertex_from_dict, list_neighbors in dict_graph.items():
            if vertex in list_neighbors:
                dict_graph[vertex_from_dict] = list(set(list_neighbors) -
                                                    set(list(vertex)))

        return dict_graph

    def strongly_connected_componenets(self, dict_graph):

        '''
        Funnction:
            Fetch a list of lists of the strongly connected components present
            in a directed graph
        Input:
            dict_graph (dict): The graph for which we want to fetch the SCCs
        Output:
            list_all_scc (list): A list of sub-lists. Each sub-list contains a
                                group of strongly connected vertices
        '''

        reverse_graph = self.reverse_graph(self.dict_graph)
        dict_dfs_info_reverse = self.depth_first_search(reverse_graph)
        dict_postvisit_clock_reverse = \
            dict_dfs_info_reverse['dict_postvisit_clock']

        list_all_scc = []

        while len(reverse_graph) > 0:
            source_node_original = max(dict_postvisit_clock_reverse,
                                       key=dict_postvisit_clock_reverse.get)

            dict_visited_vertex_reverse = {}

            for vertex in self.get_list_vertices(reverse_graph):
                dict_visited_vertex_reverse[vertex] = 0

            dict_dfs_info_reverse['dict_visited'] = dict_visited_vertex_reverse
            dict_dfs_info_vertex = self.explore_vertex(source_node_original,
                                                       dict_graph,
                                                       dict_dfs_info_reverse)

            dict_visited_vertex_reverse = dict_dfs_info_vertex['dict_visited']
            list_scc_vertex = []

            for vertex, fl_visited in dict_visited_vertex_reverse.items():
                if fl_visited == 1:
                    list_scc_vertex.append(vertex)

            for vertex in list_scc_vertex:
                dict_graph = self.remove_vertex(vertex, dict_graph)
                reverse_graph = self.remove_vertex(vertex, reverse_graph)
                del(dict_postvisit_clock_reverse[vertex])

            list_all_scc.append(list_scc_vertex)

        return list_all_scc

    def breadth_first_search(self, dict_graph, origin_node):

        '''
        Function:
            Algorithm to fetch the shortest distance from an input origin
            vertex to all the vertices present in the graph. The algorithm
            works by assuming a weight of 1 for all the edges in the graph
        Input:
            dict_graph (dict): The dictionary representation of the graph
            origin_node (str): The vertex from which we want to calculate the
                                distances
        Output:
            dict_distance (dict): A dictionary containing the vertices as the
                                    keys and their distance from origin as the
                                    value
            dict_prev_node (dict): A dictionary mapping the vertices to their
                                    immediate previous vertices (as per BFS).
                                    Helps reconstruct the shortest path found.
        '''

        dict_distance = {}
        dict_prev_node = {}

        for vertex in self.get_list_vertices(dict_graph):
            dict_distance[vertex] = len(self.get_list_vertices(dict_graph)) \
                                                                        + 1000
            dict_prev_node[vertex] = None

        dict_distance[origin_node] = 0
        queue_vertices_dict_known = Queue()
        queue_vertices_dict_known.enqueue(origin_node)

        while queue_vertices_dict_known.is_empty() is False:
            curr_vertex = queue_vertices_dict_known.dequeue()
            list_neighbors = dict_graph[curr_vertex]

            for neighbor in list_neighbors:
                if dict_distance[neighbor] == \
                                len(self.get_list_vertices(dict_graph)) + 1000:
                    queue_vertices_dict_known.enqueue(neighbor)
                    dict_distance[neighbor] = dict_distance[curr_vertex] + 1
                    dict_prev_node[neighbor] = curr_vertex

        return dict_distance, dict_prev_node

    def get_shortest_path(self, dict_graph, origin_node, destination_node):

        '''
        Function:
            Output the shortest path from the origin to the destination node
            by running BFS over the input graph
        Input:
            dict_graph (dict): The dictionary representation of the graph
            origin_node (str): The origin vertex
            destination_node (str): The destination vertex
        Output:
            A list of the vertices through which the destination is reached
        '''

        dict_distance, dict_prev_node = self.breadth_first_search(dict_graph,
                                                                  origin_node)

        if dict_distance[destination_node] == \
                len(self.get_list_vertices(dict_graph)) + 1000:

            print('The destination node is unreachable from the origin node!')
            return

        output_path_reverse = [destination_node]
        curr_node = destination_node

        while dict_prev_node[curr_node] is not None:
            output_path_reverse.append(dict_prev_node[curr_node])
            curr_node = dict_prev_node[curr_node]

        return output_path_reverse[::-1]

# Example of an undirected graph.
dict_undirected_graph = {}
dict_undirected_graph['A'] = ['B', 'C', 'D']
dict_undirected_graph['B'] = ['A', 'C']
dict_undirected_graph['C'] = ['A', 'B']
dict_undirected_graph['D'] = ['A']
dict_undirected_graph['E'] = ['F']
dict_undirected_graph['F'] = ['E']
dict_undirected_graph['G'] = ['H', 'I']
dict_undirected_graph['H'] = ['G', 'I']
dict_undirected_graph['I'] = ['G', 'H']

undirected_graph = Graph(dict_undirected_graph)
dict_dfs_info = undirected_graph.depth_first_search(dict_undirected_graph)
print(dict_dfs_info['dict_visited'])
print(dict_dfs_info['dict_previsit_clock'])
print(dict_dfs_info['dict_postvisit_clock'])
print(dict_dfs_info['connected_component'])

# Example on directed graph
dict_directed_graph = {}
dict_directed_graph['A'] = ['B']
dict_directed_graph['B'] = ['E', 'F']
dict_directed_graph['C'] = ['B']
dict_directed_graph['D'] = ['A', 'G']
dict_directed_graph['E'] = ['A', 'C', 'H']
dict_directed_graph['F'] = []
dict_directed_graph['G'] = ['H']
dict_directed_graph['H'] = ['I']
dict_directed_graph['I'] = ['F', 'H']

directed_graph = Graph(dict_directed_graph)
dict_directed_graph_reverse = directed_graph.reverse_graph(dict_directed_graph)
list_all_scc = directed_graph.strongly_connected_componenets(
                                                        dict_directed_graph)

# Since dict_directed_graph would have chnaged, we reverse the reverse_graph
# to get it back
dict_directed_graph = directed_graph.reverse_graph(dict_directed_graph_reverse)

dict_distance, dict_prev_node = directed_graph.breadth_first_search(
                                                        dict_directed_graph,
                                                        origin_node='A')

output_path = directed_graph.get_shortest_path(dict_directed_graph, 'A', 'I')
output_path = directed_graph.get_shortest_path(dict_directed_graph, 'A', 'F')
output_path = directed_graph.get_shortest_path(dict_directed_graph, 'A', 'D')

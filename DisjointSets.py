'''
Theory:
    Disjoint set is a type of data structure which can be used to track a list
    of elements which are being shuffled. Each subset is disjoint (no-overlap).
    It can be implemented using trees (with the flexibility of a parent having
    many child nodes)
'''


class DisjointSet:

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, val):

        '''
        Function:
            For an input value val, make a disjoint set comprising of just that
            value
        Input:
            val: The value whose set we want to create
        '''

        self.parent[val] = val
        self.rank[val] = 0

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

    def print_all_sets(self):

        set_info = {}

        for key in list(self.parent.keys()):
            if self.find(key) not in set_info:
                set_info[self.find(key)] = []

            set_info[self.find(key)].append(key)

        print(set_info)

# Testing
dis_set = DisjointSet()
dis_set.make_set(1)
dis_set.make_set(2)
dis_set.make_set(3)
dis_set.make_set(4)
dis_set.make_set(5)
dis_set.make_set(6)

dis_set.print_all_sets()

dis_set.union(2, 4)
dis_set.print_all_sets()

dis_set.union(5, 2)
dis_set.union(3, 1)
dis_set.print_all_sets()

dis_set.union(2, 3)
dis_set.union(2, 6)
dis_set.print_all_sets()

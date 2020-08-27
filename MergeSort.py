'''
Merfe sort is a sorting algorithm which uses the divide and conquer principle
to sort an array in O(nlog(n)) worse time
'''


class MergeSort:

    def __init__(self, array):
        self.array = array

    def merge_sort(self, array):

        if len(array) > 1:
            middle = int(len(array)/2)
            left_array = array[:middle]
            right_array = array[middle:]
            left_array = self.merge_sort(left_array)
            right_array = self.merge_sort(right_array)
            sorted_array = self.merge(left_array, right_array)

        else:
            sorted_array = array

        return sorted_array

    def merge(self, array1, array2):

        sorted_array = []
        while (array1 != []) & (array2 != []):

            if array1[0] <= array2[0]:
                sorted_array.append(array1[0])
                array1.pop(0)

            else:
                sorted_array.append(array2[0])
                array2.pop(0)

        if array1 != []:
            sorted_array = sorted_array + array1

        if array2 != []:
            sorted_array = sorted_array + array2

        return sorted_array

# Examples
array = [34, 21, 65, 2, -76, 546, 43]
print(MergeSort(array).merge_sort(array))

array = []
print(MergeSort(array).merge_sort(array))

array = [6]
print(MergeSort(array).merge_sort(array))

array = [12, 11, 10, 8, 7, 2]
print(MergeSort(array).merge_sort(array))

array = [2, 7, 8, 10, 11, 12]
print(MergeSort(array).merge_sort(array))

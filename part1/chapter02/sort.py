'''
# insertion sort（插入排序）
# O(n^2)
'''

def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i>=0 and array[i]>key:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = key

'''
# selection sort（选择排序）
# O(n^2)
'''
def selection_sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                temp_value = array[i] 
                array[i] = array[j]
                array[j] = temp_value


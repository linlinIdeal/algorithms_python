from part1.chapter02 import sort
int_array = [3, 78, 6, 24, 8, 9, 2, 25, 1, 7, 21, 9, 3, 8, 4, 19, 32]

def main():
    insertion_array = int_array[:]
    sort.insertion_sort(insertion_array)
    print('insertion_sort result:')
    print(insertion_array)
    print('---------------------------------')
    selection_array = int_array[:]
    sort.selection_sort(selection_array)
    print('selection_array result:')
    print(insertion_array)
    print('---------------------------------')
main()
# File: sort_int.py

from utilities import *
from sequence import *
from sorting import *

if __name__ == '__main__':
    array = StaticArray.int_from_file(input('Enter file name: '))
    print(f'Read count == {len(array)}')
    print('Array data:')
    print(array)
    sorter = None
    response = input('(m)erge  (q)uick  (i)nsert  (s)elect  (h)eap: ').upper()
    match response:
        case 'M':
            sorter = MergeSorter(c_int, len(array))
        case 'Q':
            sorter = QuickSorter()
        case 'I':
            sorter = InsertSorter()
        case 'S':
            sorter = SelectSorter()
        case 'H':
            sorter = HeapSorter(array, 0, len(array) - 1)
        case _:
            print('Invalid choice.')
            exit()
    sorter.sort(array, 0, len(array) - 1)
    print('Array data:')
    print(array)
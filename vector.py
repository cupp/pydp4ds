from StaticArray import StaticArray
from ctypes import *
import re

class Vector:

    def __init__(self, dtype=c_int):
        self.data = StaticArray(dtype, 1)
        self.cap = 1
        self.size = 0
        self.dtype = dtype

    def __getitem__(self, i: int) -> object:
        if i < 0 or self.size <= i:
            raise IndexError(f'Vector index out of bounds: index == {i}')
        return self.data[i]
    
    def __setitem__(self, i: int, val) -> None:
        if i < 0 or self.size <= i:
            raise IndexError(f'Vector index out of bounds: index == {i}')
        self.data[i] = val

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        r = '('
        for i in range(self.size - 1):
            r += str(self.data[i])
            r += ', '
        if self.size > 0:
            r += str(self.data[self.size - 1])
        r += ')'
        return r

    def __double_capacity(self):
        self.cap *= 2
        new_data = StaticArray(self.dtype, self.cap)
        for k in range(self.size):
            new_data[k] = self.data[k]
        self.data = new_data

    def append(self, val) -> None:
        if self.size == self.cap:
            self.__double_capacity()
        self.data[self.size] = val
        self.size += 1

    def append_values_from_file(self, filename: str=None) -> None:
        x = []
        typ = int if self.dtype == c_int else float
        if filename == None:
            x = prompt_list(typ)
        else:
            f = open(filename, 'r')
            value_str = f.read()
            x = re.split('\\s+', value_str)
            x = [typ(x[i]) for i in range(len(x))]
        for value in x:
            self.append(value)

    def add_values_from_user(self) -> None:
        self.append_from_file()
    
    def insert(self, i: int, val) -> None:
        raise ValueError('Vector.insert: Exercise for the student.')

    def remove(self, i: int) -> object:
        raise ValueError('Vector.remove: Exercise for the student.')

    def write_to_file(self, filename: str) -> None:
        f = open(filename, 'w')
        f.write(self)


if __name__ == '__main__':
    v = Vector(c_int)
    response = ''
    while response.upper() != 'Q':
        response = input('\n(c)ap  (s)ize  (a)ppend  (f)ileAppend  (i)nsert  (r)emove  se(t)  (w)rite  (q)uit: ').upper()
        match response:
            case 'C':
                print(f'\nThe capacity is {v.cap}')
            case 'S':
                print(f'\nThe size is {len(v)}')
            case 'A':
                value = int(input('Append what integer value? '))
                v.append(value)
            case 'F':
                filename = input('Enter name of integer file: ')
                v.int_from_file(filename)
            case 'I':
                value = int(input('Insert what integer value? '))
                index = int(input('Insert at what location? '))
                v.insert(index, value)
            case 'R':
                index = int(input('Remove from what location? '))
                value = v.remove(index)
                print(f'\n{value} removed.')
            case 'T':
                value = int(input('Set what integer value? '))
                index = int(input('Set at what location? '))
                v[index] = value
                print(f'\nValue at index {index} is now {v[index]}')
            case 'W':
                print(f'\n{v}')
            case 'Q':
                pass
            case _:
                print('\nIllegal command.')

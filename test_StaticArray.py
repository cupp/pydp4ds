from sequence import StaticArray
from ctypes import *

if __name__ == '__main__':
    a = StaticArray(dtype=c_int, size=4)
    b = StaticArray(size=5, dtype=c_double)
    c = StaticArray(size=3, dtype=c_bool)
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    a[2] = 99
    print(f'a = {a}')
    print(a[2])
    a.fill([1,2,3,4,5,6,7,8,9,10])
    b.fill([1,2])
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(f'The length of b is {len(b)}')
    d = StaticArray.double_from_prompt()
    print(f'd = {d}')
    e = StaticArray.int_from_prompt()
    print(f'e = {e}')
    f = StaticArray.int_from_file('data/integers')
    print(f)
    g = StaticArray.double_from_file('data/numbers')
    print(g)
    f.write_to_file('test.txt',20)
    g.write_to_file('test2.txt',20)
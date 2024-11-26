from utilities import *
from ctypes import *
import re
class StaticArray:
    pass

class StaticArray:
    def __init__(self, dtype=c_int, size: int=0) -> None:
        arr = dtype * size
        self.body = arr()
        self.size = size
        self.dtype = dtype

    def __repr__(self) -> str:
        r = '['
        for x in self.body:
            r += str(x)
            r += ', '
        return r[:-2] + ']'
    
    def __getitem__(self, idx) -> object:
        return self.body[idx]
    
    def __setitem__(self, idx, val) -> None:
        self.body[idx] = val

    def __len__(self) -> int:
        return self.size

    def fill(self, x: list) -> None:
        for i in range(self.size):
            self.body[i] = x[i % len(x)]

    @classmethod
    def int_from_prompt(cls) -> StaticArray:
        x = prompt_list(int)
        d = StaticArray(size=len(x), dtype=c_int)
        d.fill(x)
        return d

    @classmethod
    def double_from_prompt(cls) -> StaticArray:
        x = prompt_list(float)
        d = StaticArray(size=len(x), dtype=c_double)
        d.fill(x)
        return d

    @classmethod
    def int_from_file(cls, filename: str) -> StaticArray:
        f = open(filename, 'r')
        value_str = f.read()
        x = re.split('\\s+', value_str)
        x = [int(x[i]) for i in range(len(x))]
        d = StaticArray(size=len(x), dtype=c_int)
        d.fill(x)
        return d

    @classmethod
    def double_from_file(cls, filename: str) -> StaticArray:
        f = open(filename, 'r')
        value_str = f.read()
        x = re.split('\\s+', value_str)
        x = [float(x[i]) for i in range(len(x))]
        d = StaticArray(size=len(x), dtype=c_double)
        d.fill(x)
        return d

    def write_to_file(self, filename: str, length: int) -> None:
        f = open(filename, 'w')
        size = len(self)
        for i in range(min(length, size)):
            f.write(f'{self[i]:12}')
            if i % 6 == 5:
                f.write('\n')
        f.write('\n')

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

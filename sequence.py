from utilities import *
from ctypes import *
from abc import *
import re

# Forward declarations

class Sequence:
    pass

class StaticArray:
    pass

class Vector:
    pass

###############################################################################
###############################################################################
################################## Sequence ###################################
###############################################################################
###############################################################################

class Sequence(ABC):
    @abstractmethod
    def __getitem__(self, i: int) -> object:
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __setitem__(self, i: int, val) -> None:
        pass

    @abstractmethod
    def capacity(self) -> int:
        pass


###############################################################################
###############################################################################
################################# StaticArray #################################
###############################################################################
###############################################################################

class StaticArray(Sequence):
    def __init__(self, dtype=c_int, capacity: int=0) -> None:
        arr = dtype * capacity
        self.body = arr()
        self.cap = capacity
        self.dtype = dtype
    
    def __getitem__(self, idx) -> object:
        return self.body[idx]

    def __len__(self) -> int:
        return self.cap

    def __repr__(self) -> str:
        r = '['
        for x in self.body:
            r += str(x)
            r += ', '
        return r[:-2] + ']'

    def __setitem__(self, idx, val) -> None:
        self.body[idx] = val
    
    def capacity(self) -> int:
        return self.cap

    def fill(self, x: list) -> None:
        for i in range(self.capacity()):
            self.body[i] = x[i % len(x)]

    @classmethod
    def int_from_prompt(cls) -> StaticArray:
        x = prompt_list(int)
        d = StaticArray(capacity=len(x), dtype=c_int)
        d.fill(x)
        return d

    @classmethod
    def double_from_prompt(cls) -> StaticArray:
        x = prompt_list(float)
        d = StaticArray(dtype=c_double, capacity=len(x))
        d.fill(x)
        return d

    @classmethod
    def int_from_file(cls, filename: str) -> StaticArray:
        f = open(filename, 'r')
        value_str = f.read().strip()
        x = re.split('\\s+', value_str)
        x = [int(x[i]) for i in range(len(x))]
        d = StaticArray(dtype=c_int, capacity=len(x))
        d.fill(x)
        return d

    @classmethod
    def double_from_file(cls, filename: str) -> StaticArray:
        f = open(filename, 'r')
        value_str = f.read().strip()
        x = re.split('\\s+', value_str)
        x = [float(x[i]) for i in range(len(x))]
        d = StaticArray(capacity=len(x), dtype=c_double)
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


###############################################################################
###############################################################################
################################### Vector ####################################
###############################################################################
###############################################################################

class Vector(Sequence):
    def __init__(self, dtype=c_int):
        self.data = StaticArray(dtype, 1)
        self.cap = 1
        self.size = 0
        self.dtype = dtype

    def __getitem__(self, i: int) -> object:
        if i < 0 or self.size <= i:
            raise IndexError(f'Vector index out of bounds: index == {i}')
        return self.data[i]

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

    def __setitem__(self, i: int, val) -> None:
        if i < 0 or self.size <= i:
            raise IndexError(f'Vector index out of bounds: index == {i}')
        self.data[i] = val

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

    def capacity(self):
        return self.cap

    def extend_from_file(self, filename: str=None) -> None:
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

    def extend_from_user(self) -> None:
        self.append_from_file()
    
    def insert(self, i: int, val) -> None:
        raise ValueError('Vector.insert: Exercise for the student.')

    def remove(self, i: int) -> object:
        raise ValueError('Vector.remove: Exercise for the student.')

    def write_to_file(self, filename: str) -> None:
        f = open(filename, 'w')
        f.write(self)

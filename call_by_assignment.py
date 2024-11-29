from sequence import *

def swap_seq(lst):
    lst[0], lst[-1] = lst[-1], lst[0]

def swap(a, b):
    print(f'a == {a}, b == {b}')
    a, b = b, a
    print(f'a == {a}, b == {b}')

x = list(range(8))
print(f'\nbefore swap_seq:\t{x}')
swap_seq(x)
print(f'after swap_seq:\t\t{x}')

print()
print('#' * 80)
print()

i = 4
j = 8
print(f'before swap:\ti == {i}, j == {j}')
swap(i, j)
print(f'after swap:\ti == {i}, j == {j}\n')

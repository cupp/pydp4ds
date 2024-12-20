# File: utilities.py

import re

PI = 3.1415926535898

def prompt_float_ge(prompt: str, limit: float) -> float:
    """Prompts the user with message prompt, requesting value >= limit.
    Continually prompts with error message when value input is not >= limit.
    Post: Double precision real >= limit is returned."""

    d = float(input(f'{prompt} (>= {limit}): '))
    while d < limit:
        print(f'Must be greater than or equal to {limit}.')
        d = float(input(f'{prompt} (>= {limit}): '))
    return d

def prompt_int_ge(prompt: str, limit: int) -> int:
    """Prompts the user with message prompt, requesting value >= limit.
    Continually prompts with error message when value input is not >= limit.
    Post: Integer >= limit is returned."""

    i = int(input(f'{prompt} (>= {limit}): '))
    while i < limit:
        print(f'Must be greater than or equal to {limit}.')
        i = int(input(f'{prompt} (>= {limit}): '))
    return i

def prompt_int_between(prompt: str, lo: int, hi: int) -> int:
    """Prompts the user with message prompt, requesting value in lo..hi.
    Continually prompts with error message when value input is not in lo..hi.
    Post: Integer value in lo..hi is returned."""

    i = int(input(f'{prompt} ({lo}..{hi}): '))
    while i < lo or i > hi:
        print(f'Must be between {lo} and {hi}.')
        i = int(input(f'{prompt} ({lo}..{hi}): '))
    return i

def prompt_file_open() -> object:
    """Prompts the user for a file name and opens it."""

    in_file_name = input('File Name? ')
    try:
        f = open(in_file_name, 'r')
    except:
        print(f'Cannot open {in_file_name}.')
    return f

def sgn(i: int) -> int:
    """Post: If 0 <= i then 1 is returned, else -1 is returned."""
    
    return 1 if 0 <= i else -1

def gcd(m: int, n: int) -> int:
    """Pre: 0 <= m, n.
    Post: The greatest common divisor of m and n is returned."""

    return m if 0 == n else gcd(n, m % n)

def abs(i: int) -> int:
    """Post: The absolute value of i is returned."""

    return i if 0 <= i else -i

def prompt_list(dtype=int) -> list:
    x = input('Enter list of values separated by spaces: ')
    return [dtype(val) for val in re.split('\\s+', x)]

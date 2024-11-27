# File: shape.py

from abc import *
from typing import *
from utilities import *
import math


class AShape(ABC):
 
    @abstractmethod
    def area(self) -> float:
        """Post: The area of this shape is returned."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Post: The perimeter of this shape is returned."""
        pass

    @abstractmethod
    def scale(self, factor: float) -> None:
        """Pre: factor > 0.0
        Post: This shape's dimensions are multiplied by factor."""
        pass
    
    @abstractmethod
    def prompt_and_set_dimensions(self) -> None:
        """Post: This shape's dimensions are prompted and set.
        No dimension is negative."""
        pass

class NullShape(AShape):
    def __init__(self):
        pass

    def __repr__(self) -> str:
        return '\n'

    def area(self) -> float:
        return 0.0
    
    def perimeter(self) -> float:
        return 0.0
    
    def scale(self, factor: float) -> None:
        raise ValueError('scale: Exercise for the student.')

    def prompt_and_set_dimensions(self) -> None:
        pass

class Line(AShape):
    def __init__(self, length: float=0.0):  
        if length < 0.0:
            raise ValueError('Line precondition violated: length cannot be negative.')
        self.length = length

    def __repr__(self) -> str:
        return f'Line\nLength: {self.length}\n'

    def area(self) -> float:  
        return 0.0

    def perimeter(self) -> float:
        return self.length

    def scale(self, factor: float) -> None:
        raise ValueError('scale: Exercise for the student.')

    def prompt_and_set_dimensions(self) -> None:
        self.length = prompt_float_ge("Length?", 0.0)

class Rectangle(AShape):
    def __init__(self, length: float=0.0, width: float=0.0):
        if length < 0.0 or width < 0.0:
            raise ValueError('Rectangle precondition violated: length and width cannot be negative.')
        self.length = length
        self.width = width

    def __repr__(self) -> str:
        return 'Rectangle\nLength: {self.length}\nWidth: {self.width}\n'

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2.0 * (self.length + self.width)

    def scale(self, factor: float) -> None:
        raise ValueError('scale: Exercise for the student.')

    def prompt_and_set_dimensions(self) -> None:
        self.length = prompt_float_ge("Length?", 0.0)
        self.width = prompt_float_ge("Width?", 0.0)

class Circle(AShape):
    def __init__(self, radius: float=0.0):  
        if radius < 0.0:
            raise ValueError('Circle precondition violated: radius cannot be negative.')
        self.radius = radius

    def __repr__(self) -> str:
        return f'Circle\nRadius: {self.radius}\n'

    def area(self) -> float:  
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:  
        return 2.0 * math.pi * self.radius;

    def scale(self, factor: float) -> None:  
        raise ValueError('scale: Exercise for the student.')

    def prompt_and_set_dimensions(self) -> None:
        self.radius = prompt_float_ge("Radius?", 0.0)

class RightTriangle(AShape):
    def __init__(self, base: float, height: float):
        raise ValueError('RightTriangle: Exercise for the student.')

    def __repr__(self):
        raise ValueError('RightTriangle: Exercise for the student.')

    def area(self) -> float:
        raise ValueError('RightTriangle: Exercise for the student.')

    def perimeter(self) -> float:
        raise ValueError('RightTriangle: Exercise for the student.')

    def scale(self, factor: float) -> None:
        raise ValueError('RightTriangle: Exercise for the student.')

    def prompt_and_set_dimensions(self) -> None:
        raise ValueError('RightTriangle: Exercise for the student.')

# MysteryShape class (Exercise for the student)

### LOCAL FUNCTIONS ###

def make_shape() -> AShape:
    match shape_type():
        case 'L':
            sh = Line()
        case 'R':
            sh = Rectangle()
        case 'C':
            sh = Circle()
        case 'T':
            sh = RightTriangle()
        case 'M':
            # Exercise for the student.
            pass
        case _:
            pass
    sh.prompt_and_set_dimensions()
    return sh

def shape_type() -> str:
    ch = input('(l)ine  (r)ectangle  (c)ircle  right(t)riangle  (m)ystery: ').upper()
    while ch not in ('L', 'R', 'C', 'T', 'M'):
        ch = input('Must be l, r, c, t, or m.  Which type? ').upper()
    return ch


def display_shape(sh: AShape):
    print(f'sh.length = {sh.length}')

    print()
    print(sh)

if __name__ == '__main__':
    NUM_SHAPES = 5
    shapes = []
    for i in range(NUM_SHAPES):
        shapes.append(NullShape())
    response = ''
    while response != 'Q':
        print(f'There are [0..{NUM_SHAPES - 1}] shapes.')
        response = input('(m)ake  (c)lear  (a)rea  (p)erimeter  (s)cale  (d)isplay  (q)uit: ').upper()
        if response in 'MCAPSD':
            idx = prompt_int_between('Which shape?', 0, NUM_SHAPES - 1)
        match response:
            case 'M':
                shapes[idx] = make_shape()
            case 'C':
                shapes[idx] = NullShape()
            case 'A':
                print(f'\nArea: {shapes[idx].area()}\n')
            case 'P':
                print(f'\nPerimeter: {shapes[idx].perimeter()}\n')
            case 'S':
                factor = prompt_float_ge('Scale factor?', 0.0)
                shapes[idx].scale(factor)
            case 'D':
                print()
                print(shapes[idx])
            case 'Q':
                pass
            case _:
                print('\nIllegal command.\n')

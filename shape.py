# # File: Shape/ShapeMain.py

from abc import *
from typing import *
from utilities import *


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
        # Exercise for the student
        pass

    def prompt_and_set_dimensions(self) -> None:
        pass

class Line(AShape):
    def __init__(self, length: float=0.0):  
        if length < 0.0:
            raise ValueError('Line precondition violated: length cannot be negative.')
        self.length = length

    def __repr__(self) -> str:
        return 'Line\nLength: {self.length}\n'

    def area(self) -> float:  
        return 0.0

    def perimeter(self) -> float:
        return self.length

    def scale(self, factor: float) -> None:
       raise ValueError('scale: Exercise for the student.')

    def prompt_and_set_dimensions(self) -> None:
        self.length = prompt_float_ge("Length?", 0.0)


### LOCAL FUNCTIONS ###

def initialize(shapes: List[AShape], cap: int) -> None:
    for i in range(cap):
        shapes.append(NullShape())

def prompt_loop(shapes: List[AShape], cap: int) -> None:
    response = ''
    while response != 'Q':
        print(f'There are [0..] {cap - 1} shapes.')
        response = input('(m)ake  (c)lear  (a)rea  (p)erimeter  (s)cale  (d)isplay  (q)uit: ').upper()
        match response:
            case 'M':
                make_shape(shapes[prompt_int_between('Which shape?', 0, cap - 1)])
            case 'C':
                clear_shape(shapes[prompt_int_between('Which shape?', 0, cap - 1)])
            case 'A':
                print_area(shapes[prompt_int_between("Which shape?", 0, cap - 1)])
            case 'P':
                print_perimeter(shapes[prompt_int_between("Which shape?", 0, cap - 1)])
            case 'S':
                scale_shape(shapes[prompt_int_between("Which shape?", 0, cap - 1)])
            case 'D':
                display_shape(shapes[prompt_int_between("Which shape?", 0, cap - 1)])
            case 'Q':
                pass
            case _:
                print('\nIllegal command.\n')

def make_shape(sh: AShape) -> None:
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

def shape_type() -> str:
    ch = input('(l)ine  (r)ectangle  (c)ircle  right(t)riangle  (m)ystery: ').upper()
    while ch not in ('L', 'R', 'C', 'T', 'M'):
        ch = input('Must be l, r, c, t, or m.  Which type? ').upper()
    return ch

if __name__ == '__main__':
    NUM_SHAPES = 5
    shapes = []
    initialize(shapes, NUM_SHAPES)
    prompt_loop(shapes, NUM_SHAPES)





# void clearShape(AShape *&sh) {
#     delete sh;
#     sh = new NullShape;
# }

# void printArea(AShape *sh) {
#     cout << "\nArea: " << sh->area() << endl;
# }

# void printPerimeter(AShape *sh) {
#     cout << "\nPerimeter: " << sh->perimeter() << endl;
# }

# void scaleShape(AShape *sh) {
#     sh->scale(promptDoubleGE("Scale factor?", 0.0));
# }

# void displayShape(AShape *sh) {
#     cout << endl;
#     sh->display(cout);
# }


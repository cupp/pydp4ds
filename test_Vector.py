from sequence import Vector
from ctypes import c_int

if __name__ == '__main__':
    v = Vector(c_int)
    response = ''
    while response.upper() != 'Q':
        response = input('\n(c)ap  (l)ength  (a)ppend  (f)ileAppend  (i)nsert  (r)emove  se(t)  (w)rite  (q)uit: ').upper()
        match response:
            case 'C':
                print(f'\nThe capacity is {v.capacity()}')
            case 'L':
                print(f'\nThe length is {len(v)}')
            case 'A':
                value = int(input('Append what integer value? '))
                v.append(value)
            case 'F':
                filename = input('Enter name of integer file: ')
                v.extend_from_file(filename)
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

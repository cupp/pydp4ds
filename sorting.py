from sequence import *
import random

###############################################################################
###############################################################################
################################### Sorter ####################################
###############################################################################
###############################################################################

class Sorter(ABC):
    def sort(self, a: Sequence, lo: int, hi: int) -> None:
        if lo < 0 or hi > a.capacity():
            raise ValueError('Invalid sort parameters.\nlo == {lo}\nhi == {hi}\ncapacity == {a.capacity()}')
        if lo < hi:
            mid = self.split(a, lo, hi)
            self.sort(a, lo, mid - 1)
            self.sort(a, mid, hi)
            self.join(a, lo, mid, hi)

    @abstractmethod
    def split(self, a: Sequence, lo: int, hi: int) -> int:
        pass

    @abstractmethod
    def join(self, a: Sequence, lo: int, mid: int, hi: int) -> None:
        pass

###############################################################################
###############################################################################
################################# MergeSorter #################################
###############################################################################
###############################################################################

class MergeSorter(Sorter):
    def __init__(self, dtype=c_int, cap: int=0) -> None:
        self.temp_array = StaticArray(dtype, cap)

    def split(self, a: Sequence, lo: int, hi: int) -> int:
        return (lo + hi + 1) // 2
    
    def join(self, a: Sequence, lo: int, mid: int, hi: int) -> None:
        raise ValueError('MergeSorter.join: Exercise for the student.')


###############################################################################
###############################################################################
################################# QuickSorter #################################
###############################################################################
###############################################################################


class QuickSorter(Sorter):
    def __init__(self) -> None:
        pass

    def  split(self, a: Sequence, lo: int, hi: int) -> int:
        if hi - lo > 4:
            mdn = 0
            mdn1 = random.randint(lo, hi)
            mdn2 = random.randint(lo, hi)
            mdn3 = random.randint(lo, hi)
            if a[mdn2] <= a[mdn1] <= a[mdn3] or a[mdn3] <= a[mdn1] <= a[mdn2]:
                mdn = mdn1
            elif a[mdn1] <= a[mdn2] <= a[mdn3] or a[mdn3] <= a[mdn2] <= a[mdn1]:
                mdn = mdn2
            else:
                mdn = mdn3
            a[mdn], a[hi] = a[hi], a[mdn]
        key = a[hi]
        mid = lo
        for j in range(lo, hi + 1):
            if a[j] <= key:
                a[j], a[mid] = a[mid], a[j]
                mid += 1
        return min(hi, mid)
    
    def join(self, a: Sequence, lo: int, mid: int, hi: int) -> None:
        pass


###############################################################################
###############################################################################
################################ SelectSorter #################################
###############################################################################
###############################################################################


class SelectSorter(Sorter):
    def __init__(self) -> None:
        pass

    def split(self, a: Sequence, lo: int, hi: int) -> int:
        index_of_max = lo
        for i in range(hi):
            if a[index_of_max] < a[i]:
                index_of_max = i
        a[hi], a[index_of_max] = a[index_of_max], a[hi]
        return hi

    def join(self, a: Sequence, lo: int, mid: int, hi: int) -> None:
        pass


###############################################################################
###############################################################################
################################ InsertSorter #################################
###############################################################################
###############################################################################


class InsertSorter(Sorter):
    def __init__(self) -> None:
        pass

    def split(self, a: Sequence, lo: int, hi: int) -> int:
        return hi

    def join(self, a: Sequence, lo: int, mid: int, hi: int) -> None:
        raise ValueError('InsertSorter.join: Exercise for the student.')


###############################################################################
###############################################################################
################################# HeapSorter ##################################
###############################################################################
###############################################################################

class HeapSorter(Sorter):
    def __init__(self, a: Sequence, lo: int, hi: int) -> None:
        for i in range((lo + hi - 1) // 2, lo - 1, -1):
            self.sift_down(a, lo, i, hi)

    def split(self, a: Sequence, lo: int, hi: int) -> int:
        a[hi], a[lo] = a[lo], a[hi]
        self.sift_down(a, lo, lo, hi - 1)
        return hi

    def join(self, a: Sequence, lo: int, mid: int, hi: int) -> None:
        pass

    def sift_up(self, a: Sequence, lo: int, i: int) -> None:
        temp = a[i]
        parent = (i + lo - 1) // 2
        while lo < i and a[parent] < temp:
            raise ValueError('HeapSorter.sift_up: Exercise for the student.')
        a[i] = temp

    def sift_down(self, a: Sequence, lo: int, i: int, hi: int) -> None:
        child = 2 * i - lo + 1   # index of the left child
        if child <= hi:
            if child < hi and a[child] < a[child + 1]:
                child += 1
            if a[i] < a[child]:
                a[i], a[child] = a[child], a[i]
                self.sift_down(a, lo, child, hi)

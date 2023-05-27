"""Max Heap implemented using an array"""
from __future__ import annotations
__author__ = "Brendon Taylor, modified by Jackson Goerner"
__docformat__ = 'reStructuredText'

from typing import Generic
from referential_array import ArrayR, T


class MaxHeap(Generic[T]):
    MIN_CAPACITY = 1

    def __init__(self, max_size: int, an_array: ArrayR[T] = None, verbose=False) -> None:
        """
        :complexity best: = worst: O(n) initialising ArrayR or apply bottom-up heap construction using self.heapify()
        where n is the max(self.MIN_CAPACITY, max_size) + 1
            """
        if an_array is None:
            self.length = 0 
        else:
            self.length = max_size = len(an_array) 
        
        self.the_array = ArrayR(max(self.MIN_CAPACITY, max_size) + 1)
        
        # if an_array is given then apply bottom-up heap construction
        if an_array:
            self.heapify(an_array, verbose)

    def __len__(self) -> int:
        return self.length

    def is_full(self) -> bool:
        return self.length + 1 == len(self.the_array)

    def rise(self, k: int) -> None:
        """
        Rise element at index k to its correct position
        :pre: 1 <= k <= self.length
        """
        item = self.the_array[k]
        while k > 1 and item > self.the_array[k // 2]:
            self.the_array[k] = self.the_array[k // 2]
            k = k // 2
        self.the_array[k] = item

    def add(self, element: T) -> bool:
        """
        Swaps elements while rising
        """
        if self.is_full():
            raise IndexError

        self.length += 1
        self.the_array[self.length] = element
        self.rise(self.length)

    def largest_child(self, k: int) -> int:
        """
        Returns the index of k's child with greatest value.
        :pre: 1 <= k <= self.length // 2
        """
        
        if 2 * k == self.length or \
                self.the_array[2 * k] > self.the_array[2 * k + 1]:
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k: int) -> None:
        """ Make the element at index k sink to the correct position.
            :pre: 1 <= k <= self.length
            :complexity: ???
        """
        item = self.the_array[k]

        while 2 * k <= self.length:
            max_child = self.largest_child(k)
            if self.the_array[max_child] <= item:
                break
            self.the_array[k] = self.the_array[max_child]
            k = max_child

        self.the_array[k] = item
        
    def get_max(self) -> T:
        """ Remove (and return) the maximum element from the heap. """
        if self.length == 0:
            raise IndexError

        max_elt = self.the_array[1]
        self.length -= 1
        if self.length > 0:
            self.the_array[1] = self.the_array[self.length+1]
            self.sink(1)
        return max_elt
    
    def heapify(self, an_array: ArrayR[T], verbose=False) -> None:
        """
        Apply bottom-up heap construction in O(n) time.

        The complexity of the given code is O(n), where n is the length of the input array an_array.

        The code starts by copying the elements of an_array to self.the_array (shifted by 1 position). 
        This operation takes O(n) time because it iterates over the elements of an_array and assigns them to the corresponding positions 
        in self.the_array.

        After that, the code performs a bottom-up heap construction by calling the sink method on each parent node. 
        The loop that iterates over the parent nodes runs for self.length // 2 times, which is approximately n/2 times. 
        Within the loop, the sink operation has a time complexity of O(log n), 
        as it involves swapping elements and moving down the tree to maintain the heap property.
        """
        # replace the array
        
        # copy an_array to self.the_array (shift by 1)
        for i in range(self.length):
            self.the_array[i + 1] = an_array[i]

        if verbose:
            print('the_array before bottom-up heap construction')
            for i in self.the_array:
                print(i)

        # heapify every parent
        for i in range(self.length // 2, 0, -1):
            if verbose:
                print('sinking the parent', i)

            self.sink(i)
            for i in self.the_array:
                if verbose:
                    print(i)

        if verbose:
            print('the_array after bottom-up heap construction')
            for i in self.the_array:
                print(i)

if __name__ == '__main__':
    items = [ int(x) for x in input('Enter a list of numbers: ').strip().split() ]
    heap = MaxHeap(len(items))

    for item in items:
        heap.add(item)
        
    while(len(heap) > 0):
        print(heap.get_max())

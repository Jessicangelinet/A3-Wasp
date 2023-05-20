from dataclasses import dataclass
from heap import MaxHeap

@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

    def get_emerald(self):
        return min(self.capacity,self.volume) * self.nutrient_factor

    def __lt__(self, other):
        """
        Defines behavior for the less-than operator, < between self and other change doc 🏁

        :complexity:
        :best = O(1) + O(comp)
        :worst: O(n) + O(comp), n is the len(.name)
        """
        if isinstance(other, Beehive):
            return self.get_emerald() < other.get_emerald

    def __eq__(self, other):
        """
        Defines behavior for the equality operator, == between self and other

        :complexity:
        :best = O(1) + O(comp)
        :worst: O(n) + O(comp), n is the len(.name)
        """
        if isinstance(other, Beehive):
            return self.get_emerald() == other.get_emerald()

    def __gt__(self, other):
        """
        Defines behavior for the greater-than operator, > between self and other

        :complexity:
        :best = O(1) + O(comp)
        :worst: O(n) + O(comp), n is the len(.name)
        """
        if isinstance(other, Beehive):
            return self.get_emerald() > other.get_emerald()
        
    def __le__(self, other):
        """
        Defines behavior for the less-than-or-equal-to operator, <=.between self and other

        :complexity:
        :best = O(1) + O(comp)
        :worst: O(n) + O(comp), n is the len(.name)
        """
        if isinstance(other, Beehive):
            return self.get_emerald() <= other.get_emerald()
        
    def __ge__(self, other):
        """
        Defines behavior for the greater-than-or-equal-to operator, >= between self and other

        :complexity:
        :best = O(1) + O(comp)
        :worst: O(n) + O(comp), n is the len(.name)
        """
        if isinstance(other, Beehive):
            return self.get_emerald() >= other.get_emerald

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.BeehiveHeap = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]):
        self.BeehiveHeap.heapify(hive_list) #heapify add the method int he heap.py
    
    def add_beehive(self, hive: Beehive):
        self.BeehiveHeap.add(hive)
        # print(self.BeehiveHeap.get_max()) #what this works tho
    
    def harvest_best_beehive(self):
        if self.BeehiveHeap.length != 0:
            # print(self.BeehiveHeap.get_max())
            # return self.BeehiveHeap.get_max().get_emerald()
            # ind = self.BeehiveHeap.largest_child(1)
            # print([hive.get_emerald() for hive in self.BeehiveHeap.the_array if hive is not None])
            # return self.BeehiveHeap.the_array[ind-1].get_emerald()
            current_largest = self.BeehiveHeap.get_max()

            if current_largest.capacity > current_largest.volume:
                current_largest.volume = 0
            else: 
                new_volume = current_largest.volume - current_largest.capacity
                current_largest.volume = new_volume
                self.BeehiveHeap.add(current_largest)
            
            return current_largest.get_emerald()

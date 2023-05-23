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
        # if self.volume == 0:
        #     return self.nutrient_factor
        return min(self.capacity, self.volume) * self.nutrient_factor

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
        while self.BeehiveHeap:
            self.BeehiveHeap.get_max
        self.BeehiveHeap.heapify(hive_list)
    
    def add_beehive(self, hive: Beehive):
        if hive.volume != 0:
            self.BeehiveHeap.add(hive)
    
    def harvest_best_beehive(self):
        if self.BeehiveHeap.length != 0:
            current_largest = self.BeehiveHeap.get_max()
            emerald = current_largest.get_emerald()
            
            if current_largest.capacity <= current_largest.volume:
                
                new_value = current_largest
                new_volume = new_value.volume - new_value.capacity
                new_value.volume = new_volume

                self.add_beehive(new_value)
            return emerald
            
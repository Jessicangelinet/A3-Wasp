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

    def __lt__(self, other):
        """
        Defines behavior for the less-than operator, < between self and other change doc 🏁

        :complexity:
        :best = O(1) + O(comp)
        :worst: O(n) + O(comp), n is the len(.name)
        """
        if isinstance(other, Beehive):
            if self.capacity == other.capacity:
                if self.volume == other.volume:
                    return self.nutrient_factor < other.nutrient_factor
                return self.volume < other.volume
            return self.capacity < other.capacity

    def __eq__(self, other):
        """
        Defines behavior for the equality operator, == between self and other

        :complexity:
        :best = O(1) + O(comp)
        :worst: O(n) + O(comp), n is the len(.name)
        """
        if isinstance(other, Beehive):
            if self.capacity == other.capacity:
                if self.volume == other.volume:
                    return self.nutrient_factor == other.nutrient_factor
                return self.volume == other.volume
            return self.capacity == other.capacity

    def __gt__(self, other):
        """
        Defines behavior for the greater-than operator, > between self and other

        :complexity:
        :best = O(1) + O(comp)
        :worst: O(n) + O(comp), n is the len(.name)
        """
        if isinstance(other, Beehive):
            if self.capacity == other.capacity:
                if self.volume == other.volume:
                    return self.nutrient_factor > other.nutrient_factor
                return self.volume > other.volume
            return self.capacity > other.capacity
        
    def __le__(self, other):
        """
        Defines behavior for the less-than-or-equal-to operator, <=.between self and other

        :complexity:
        :best = O(1) + O(comp)
        :worst: O(n) + O(comp), n is the len(.name)
        """
        if isinstance(other, Beehive):
            if self.capacity == other.capacity:
                if self.volume == other.volume:
                    return self.nutrient_factor <= other.nutrient_factor
                return self.volume <= other.volume
            return self.capacity <= other.capacity
        
    def __ge__(self, other):
        """
        Defines behavior for the greater-than-or-equal-to operator, >= between self and other

        :complexity:
        :best = O(1) + O(comp)
        :worst: O(n) + O(comp), n is the len(.name)
        """
        if isinstance(other, Beehive):
            if self.capacity == other.capacity:
                if self.volume == other.volume:
                    return self.nutrient_factor >= other.nutrient_factor
                return self.volume >= other.volume
            return self.capacity >= other.capacity

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.BeehiveHeap = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]):
        raise NotImplementedError()
    
    def add_beehive(self, hive: Beehive):
        self.BeehiveHeap.add(hive)
        # print(self.BeehiveHeap.get_max()) #what this works tho
    
    def harvest_best_beehive(self):
        largest = self.BeehiveHeap.largest_child(0)
        if self.BeehiveHeap.length != 0:
            return self.BeehiveHeap.get_max()

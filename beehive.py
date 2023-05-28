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

    def get_emerald(self) -> int:
        """
        :complexity best = worst: O(1) because no matter what the input, arithmetic operations take O(1) time
        """
        return min(self.capacity, self.volume) * self.nutrient_factor

    def __lt__(self, other):
        """
        Defines behavior for the less-than operator, < between self and other's get_emerald() return values

        :complexity best = worst: O(1) because no matter what the input, arithmetic operations take O(1) time
        """
        if isinstance(other, Beehive):
            return self.get_emerald() < other.get_emerald()

    def __eq__(self, other):
        """
        Defines behavior for the equality operator, == between self and other's get_emerald() return values

        :complexity best = worst: O(1) because no matter what the input, comparison between integers takes O(1) time
        """
        if isinstance(other, Beehive):
            return self.get_emerald() == other.get_emerald()

    def __gt__(self, other):
        """
        Defines behavior for the greater-than operator, > between self and other's get_emerald() return values

        :complexity best = worst: O(1) because no matter what the input, comparison between integers takes O(1) time
        """
        if isinstance(other, Beehive):
            return self.get_emerald() > other.get_emerald()
        
    def __le__(self, other):
        """
        Defines behavior for the less-than-or-equal-to operator, <=.between self and other's get_emerald() return values

        :complexity best = worst: O(1) because no matter what the input, comparison between integers takes O(1) time
        """
        if isinstance(other, Beehive):
            return self.get_emerald() <= other.get_emerald()
        
    def __ge__(self, other):
        """
        Defines behavior for the greater-than-or-equal-to operator, >= between self and other's get_emerald() return values

        :complexity best = worst: O(1) because no matter what the input, comparison between integers takes O(1) time
        """
        if isinstance(other, Beehive):
            return self.get_emerald() >= other.get_emerald

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        """
        :complexity best: = worst: O(n) initialising ArrayR 
        """
        self.BeehiveHeap = MaxHeap(max_beehives)
        self.max = max_beehives

    def set_all_beehives(self, hive_list: list[Beehive]):
        """
        :complexity:
        :best = worst case: O(M), where M is len(hive_list), because no matter how big M value is, all the code will still run
        """
        self.BeehiveHeap = MaxHeap(self.max, hive_list)
    
    def add_beehive(self, hive: Beehive):
        """
        :complexity:
        :best = worst case: O(Heap.MaxHeap.add()) == O(logN), where N is the number of nodes in BeehiveHeap, because no matter what, all the code will still run
        """
        if hive.volume:
            self.BeehiveHeap.add(hive)
    
    def harvest_best_beehive(self):
        """
        :complexity:
        :best = worst case: O(compK<=) + O(logN) + O(logN), where N is the number of nodes in BeehiveHeap, because no matter what, all the code will still run
        where k is the key of each node in BeehiveHeap
        """
        if self.BeehiveHeap.length != 0:
            current_largest = self.BeehiveHeap.get_max() #O(Heap.MaxHeap.get_max()) == O(logN)
            emerald = current_largest.get_emerald()
            
            if current_largest.capacity <= current_largest.volume:
                
                new_value = current_largest
                new_volume = new_value.volume - new_value.capacity
                new_value.volume = new_volume

                self.add_beehive(new_value) #O(self.add_beehive()) == O(logN)
            return emerald
            
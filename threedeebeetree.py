from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field
from referential_array import ArrayR

I = TypeVar('I')
Point = Tuple[int, int, int]

@dataclass
class BeeNode:
    key: Point
    item: I 
    subtree_size: int = 1
    child_nodes: ArrayR = field(default_factory=lambda: ArrayR(8))

    def set_subtree_size(self, subtree_size: int) -> None:
        """
            Sets the subtree_size of a specific instance of the class

            :Best and Worst Case: O(1)
        """

        self.subtree_size = subtree_size

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        """
            Returns a child node of the current node at a specific point or None

            :Best and Worst Case: O(CompK) as the octant_check has a time complexity of O(CompK) for its
            best and worst case where CompK is the comparison of two keys.
        """
        octant = octant_check(self.key, point)
        return self.child_nodes[octant]

class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        """
            Attempts to get an item in a tree using a key starting from the root
            :Best Case: O(1) when the item looked for is the root node.
            :Worst Case: O(log(n)) where n is the maximum depth of the tree when the method reaches
            the lowest leaf regardless of whether the item is there or not
        """
        return self.get_tree_node_by_key_aux(self.root, key)
    
    def get_tree_node_by_key_aux(self, current: BeeNode, key: Point) -> BeeNode:
        """ 
            Attempts to get an item by traversing down a tree until it reaches the item.

            :Best Case: O(CompK) where CompK is the time complexity of comparing
            the keys when the node to be insert is a child of the root node or when the node is inserted as the root node.
            :Worst Case: O(log(n) * CompK) where CompK is the time complexity of comparing
            the keys and n is the maximum depth of the tree when the item is to be inserted at the lowest level leaf
        """
        if current is None:
            raise KeyError('Key not found: {0}'.format(key))
        elif key == current.key:
            return current
        else:
            octant = octant_check(current.key, key)
            if current.child_nodes[octant].key == key:
                return current.child_nodes[octant]
            else:
                return self.get_tree_node_by_key_aux(current.child_nodes[octant], key)
            
    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I):
        """
            Attempts to find the location the node should be inserted at and then inserts it.

            :Best Case: O(CompK) where CompK is the time complexity of comparing
            the keys when the node to be insert is a child of the root node or when the node is inserted as the root node.
            :Worst Case: O(log(n) * CompK) where CompK is the time complexity of comparing
            the keys and n is the maximum depth of the tree when the item is to be inserted at the lowest level leaf
        """
        if current is None:  # base case: at the leaf
            current = BeeNode(key, item)
            self.length += 1

        elif key != current.key:
            octant = octant_check(current.key, key)
            current.subtree_size += 1
            current.child_nodes[octant] = self.insert_aux(current.child_nodes[octant], key, item)

        elif key == current.key:  # key == current.key
            raise ValueError('Inserting duplicate item', key, item)
        return current
        
    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. 

            :Best Case: O(CompK) where CompK is the time complexity of comparing each element to None
             when the first element of the array that holds its child nodes is not None.
            :Worst Case: O(CompK) where CompK is the time complexity of comparing each element to None
            where the last element of the array that holds its child nodes is not None or
            when the function iterates to the end and no non None nodes have been found since the tuple size
            is fixed to 8.
        """
        return all(nodes is None for nodes in current.child_nodes)

def octant_check (current: Tuple, key: Point) -> int:
    """
        Takes in 2 tuples of fixed size 3, a key and the key of the current node, and compares their 
        value at each index to generate a binary string that is converted into an interger from 0 to 7.

        :Best Case and Worst Case: O(CompK) where CompK is the time complexity
        of the 2 keys as this method will always iterate 3 times due to the fixed size of the tuple.
    """
    octant = ""
    for i in range(len(key)): #O(1) since the tuples have a constant fix size of 3
        if key[i] > current[i]:
            octant = octant + "1"
        else:
            octant = octant + "0"
    return int(octant, 2)
    
if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2
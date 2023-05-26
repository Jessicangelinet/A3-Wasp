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
        self.subtree_size = subtree_size

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        octant = octant_check(self, point)
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
        return self.get_tree_node_by_key_aux(self.root, key)
    
    def get_tree_node_by_key_aux(self, current: BeeNode, key: Point) -> BeeNode:
        if current is None:
            raise KeyError('Key not found: {0}'.format(key))
        elif key == current.key:
            return current
        else:
            octant = octant_check(current, key)
            if current.child_nodes[octant].key == key:
                return current.child_nodes[octant]
            else:
                return self.get_tree_node_by_key_aux(current.child_nodes[octant], key)
            
    def __setitem__(self, key: Point, item: I) -> None:
        self.root=self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I):
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
        """
        if current is None:  # base case: at the leaf
            current = BeeNode(key, item)
            self.length += 1

        elif key != current.key:
            octant = octant_check(current, key)
            current.subtree_size += 1
            current.child_nodes[octant] = self.insert_aux(current.child_nodes[octant], key, item)

        elif key == current.key:  # key == current.key
            raise ValueError('Inserting duplicate item', key, item)
        return current
        
    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        raise NotImplementedError()

def octant_check (current: BeeNode, key: Point) -> int:
    if key[0] >= current.key[0] and key[1] >= current.key[1] and key[2] >= current.key[2]:
        return 7
    elif key[0] <= current.key[0] and key[1] >= current.key[1] and key[2] >= current.key[2]:
        return 6
    elif key[0] <= current.key[0] and key[1] <= current.key[1] and key[2] >= current.key[2]:
        return 5
    elif key[0] >= current.key[0] and key[1] <= current.key[1] and key[2] >= current.key[2]:
        return 4
    elif key[0] >= current.key[0] and key[1] >= current.key[1] and key[2] <= current.key[2]:
        return 3
    elif key[0] <= current.key[0] and key[1] >= current.key[1] and key[2] <= current.key[2]:
        return 2
    elif key[0] <= current.key[0] and key[1] <= current.key[1] and key[2] <= current.key[2]:
        return 1
    elif key[0] >= 0 and key[1] <= 0 and key[2] <= 0:
        return 0

if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2

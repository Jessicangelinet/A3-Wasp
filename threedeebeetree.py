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
    child_nodes = ArrayR(8)

    def set_subtree_size(self, subtree_size: int) -> None:
        self.subtree_size = subtree_size

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        raise NotImplementedError

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
        raise NotImplementedError()

    def __setitem__(self, key: Point, item: I) -> None:
        current = self.insert_aux(self.root, key, item)
        if self.root == None:
            self.root = current
        for i in range(len(self.root.child_nodes)):
            print(self.root.child_nodes[i] , i)
            
    def insert_aux(self, current: BeeNode, key: Point, item: I):
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
        """
        if current is None:  # base case: at the leaf
            current = BeeNode(key, item)
            self.length += 1
        elif key != current.key:
            octant = self.octant_check(current, key)
            print(octant)
            current.subtree_size += 1
            current.child_nodes[octant] = self.insert_aux(current.child_nodes[octant], key, item)
        elif key == current.key:  # key == current.key
            raise ValueError('Inserting duplicate item', key, item)
        return current
        
    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        raise NotImplementedError()

    def octant_check (self,current: BeeNode, key: Point) -> int:
        check_list = []
        for points in range(len(key)):
            if key[points] >= current.key[points]:
                check_list.append(True)
            else:
                check_list.append(False)

        if check_list == [False, False, False]:
            return 0
        elif check_list == [True, False, False]:
            return 1
        elif check_list == [False, True, False]:
            return 2
        elif check_list == [True, True, False]:
            return 3
        elif check_list == [False, False, True]:
            return 4
        elif check_list == [True, False, True]:
            return 5
        elif check_list == [False, True, True]:
            return 6
        elif check_list == [True, True, True]:
            return 7
        else:
            return KeyError(key)

if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2

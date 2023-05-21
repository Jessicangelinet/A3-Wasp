from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]

@dataclass
class BeeNode:

    key: Point
    item: I
    subtree_size: int = 1
    child_nodes = [None] * 8

    def set_subtree_size(self, subtree_size: int) -> None:
        self.subtree_size = subtree_size

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        raise NotImplementedError()

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
        self.root=self.insert_aux(self.root, key, item)
        print (self.root.child_nodes)
    def insert_aux(self, current: BeeNode, key: Point, item: I):
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
        """
        if current is None:  # base case: at the leaf
            current = BeeNode(key, item=item)
            self.length += 1
        elif key != current.key:
            octant = self.octant_check(key)
            if current.child_nodes[octant] == None:
                current.child_nodes[octant] = BeeNode(key, item=item)
            else:
                self.insert_aux(current.child_nodes[octant], key, item)
        else:  # key == current.key
            raise ValueError('Inserting duplicate item')
        return current
        
    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        raise NotImplementedError()

    def octant_check (self,key: Point) -> int:
        check_list = []
        for point in range(len(key)):
            if self.root.key[point] >= key[point]:
                check_list.append(True)
            else:
                check_list.append(False)

        if check_list == [False, False, False]:
            return 1
        elif check_list == [True, False, False]:
            return 2
        elif check_list == [False, True, False]:
            return 3
        elif check_list == [True, True, False]:
            return 4
        elif check_list == [False, False, True]:
            return 5
        elif check_list == [True, False, True]:
            return 6
        elif check_list == [False, True, True]:
            return 7
        elif check_list == [True, True, True]:
            return 8
 
 

        


if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2

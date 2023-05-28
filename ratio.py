from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.points_tree = BinarySearchTree()
    
    def add_point(self, item: T):
        """
        Attempts to insert an item into the tree, it uses the Key to insert it
            :complexity best: O(CompK) inserts the item at the root.
            :complexity worst: O(CompK * D) inserting at the bottom of the tree
            where D is the depth of the tree
            CompK is the complexity of comparing the keys
        """
        self.points_tree[item] = item
    
    def remove_point(self, item: T):
        """
        since we assume the depth of all BSTs are bounded by a factor of log(N) for the rest of the assessment, 
        we only assess the complexity when it is balanced
        :complexity best: O(CompK * logn) = worst: where there are 3 cases:
        - deleting the leaf node
        - deleting the node that has 1 children, then put the child in the deleted node's position
        - deleting the node that has 2 children, then find the successor node to be put in the deleted node's position, 
        then delete the duplicate node.

        where n is the number of nodes in the BST
        CompK is the complexity of comparing the keys
        """
        del self.points_tree[item]

    def ratio(self, x, y):
        percent_X = ceil(x/100 * len(self.points_tree)) + 1
        percent_Y = self.points_tree.root.subtree_size - ceil(y/100 * len(self.points_tree)) #index 2

        root = self.points_tree.root
        res = []

        smallest = self.points_tree.kth_smallest(percent_X, root) #returns a node class
        largest = self.points_tree.kth_smallest(percent_Y, root)

        if smallest and largest:
            return self.collect_node(self.points_tree.root, smallest.key, largest.key, [])
        else:
            return []

    def collect_node(self, current: TreeNode, lower: int, upper: int, collected_nodes: list = []) -> list[int]:
        """
        :Best and Worst Case: O(log(N) + O) where N is the total number of points within an instance of the Percentiles object
        and O is the number of items returned by the function.
        """
        if current != None:
            if current.key > lower:
                self.collect_node(current.left, lower, upper, collected_nodes)

            if lower <= current.key <= upper:
                collected_nodes.append(current.key)
            
            if current.key < upper:
                self.collect_node(current.right, lower, upper, collected_nodes)
            
        return collected_nodes

if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))

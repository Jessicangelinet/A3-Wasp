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
        percent_X = ceil(x/100 * len(self.points_tree))
        percent_Y = ceil(y/100 * len(self.points_tree)) #index 2

        print("p x", x, percent_X)
        print("p y", y, percent_Y)

        root = self.points_tree.root
        res = []


        """if root:
            smallest = self.points_tree.kth_smallest(percent_X, root) #returns a node class
            largest = self.points_tree.kth_smallest(percent_Y, root, is_smallest=False)

            print("smallest largest", smallest, largest)
            self.points_tree.inorder_limit(root, res, smallest.key, largest.key)
        result = [point.key for point in res]
        return result"""

        
        # 1st attempt pass
        self.points_tree.inorder_traversal(self.points_tree.root, res)
        # self.points_tree.inorder_traversal_limits_reversed(self.points_tree.root, res, percent_X, percent_Y) #dk if we can do dis tho lmao
        res = res[percent_X:-percent_Y] #logn * N , logn + xlogn + ylogn,   !(logn + O)!
        result = [point.key for point in res]
        return result
if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))

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
        self.points_tree[item] = item
    
    def remove_point(self, item: T):
        del self.points_tree[item]

    def ratio(self, x, y):
        percent_X = ceil(x/100 * len(self.points_tree))
        percent_Y = ceil(y/100 * len(self.points_tree))

        res = []
        self.points_tree.inorder_traversal_limits_reversed(self.points_tree.root, res, percent_X, percent_Y) #dk if we can do dis tho lmao
        # res = res[percent_X:-percent_Y]
        print(res)
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

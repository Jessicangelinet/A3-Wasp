""" Binary Search Tree ADT.
    Defines a Binary Search Tree with linked nodes.
    Each node contains a key and item as well as references to the children.
"""

from __future__ import annotations

__author__ = 'Brendon Taylor, modified by Alexey Ignatiev, further modified by Jackson Goerner'
__docformat__ = 'reStructuredText'

from typing import TypeVar, Generic
from node import TreeNode
import sys

from copy import copy

# generic types
K = TypeVar('K')
I = TypeVar('I')
T = TypeVar('T')


class BinarySearchTree(Generic[K, I]):
    """ Basic binary search tree. """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """

        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the bst is empty
            :complexity: O(1)
        """
        return self.root is None

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: K) -> bool:
        """
            Checks to see if the key is in the BST
            :complexity: see __getitem__(self, key: K) -> (K, I)
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: K) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
            :complexity best: O(CompK) finds the item in the root of the tree
            :complexity worst: O(CompK * D) item is not found, where D is the depth of the tree
            CompK is the complexity of comparing the keys
        """
        return self.get_tree_node_by_key(key).item

    def get_tree_node_by_key(self, key: K) -> TreeNode:
        return self.get_tree_node_by_key_aux(self.root, key)

    def get_tree_node_by_key_aux(self, current: TreeNode, key: K) -> TreeNode:
        if current is None:
            raise KeyError('Key not found: {0}'.format(key))
        elif key == current.key:
            return current
        elif key < current.key:
            return self.get_tree_node_by_key_aux(current.left, key)
        else:  # key > current.key
            return self.get_tree_node_by_key_aux(current.right, key)

    def __setitem__(self, key: K, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: TreeNode, key: K, item: I) -> TreeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
            :complexity best: O(CompK) inserts the item at the root.
            :complexity worst: O(CompK * D) inserting at the bottom of the tree
            where D is the depth of the tree
            CompK is the complexity of comparing the keys
        """
        if current is None:  # base case: at the leaf
            current = TreeNode(key, item=item)
            self.length += 1
        elif key < current.key:
            current.subtree_size += 1 # the part I modified so that at all times, for any node current, current.subtree_size represents the number of nodes within the subtree. 
            current.left = self.insert_aux(current.left, key, item)
        elif key > current.key:
            current.subtree_size += 1 # the part I modified so that at all times, for any node current, current.subtree_size represents the number of nodes within the subtree. 
            current.right = self.insert_aux(current.right, key, item)
        else:  # key == current.key
            raise ValueError('Inserting duplicate item')
        return current

    def __delitem__(self, key: K) -> None:
        self.root = self.delete_aux(self.root, key)

    def delete_aux(self, current: TreeNode, key: K) -> TreeNode:
        """
            Attempts to delete an item from the tree, it uses the Key to
            determine the node to delete.

            :complexity:
            In the best case, the node being deleted is a leaf node (i.e., it has no children) or has only one child. 
            In this case, the delete operation can be performed in O(h) time, where h is the height of the tree. 
            If the tree is balanced (i.e., the height is O(log n)), then the best-case time complexity of the delete method is O(log n).

            In the worst case, the node being deleted has two children and the tree is unbalanced (i.e., it has a height of n). 
            In this case, the delete operation involves finding the in-order predecessor or successor of the node, 
            which can take O(n) time in an unbalanced tree. 
            Therefore, the worst-case time complexity of the delete method is O(n).

            In summary, the best-case time complexity of the delete method for a BST is O(log n) for a balanced tree and O(h) for an unbalanced tree, 
            where h is the height of the tree. The worst-case time complexity is O(n) for an unbalanced tree.
        """
        if current is None:  # key not found
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current.subtree_size -= 1 # the part I modified so that at all times, for any node current, current.subtree_size represents the number of nodes within the subtree. 
            current.left  = self.delete_aux(current.left, key)
        elif key > current.key:
            current.subtree_size -= 1 # the part I modified so that at all times, for any node current, current.subtree_size represents the number of nodes within the subtree. 
            current.right = self.delete_aux(current.right, key)
        else:  # we found our key => do actual deletion
            if self.is_leaf(current):
                self.length -= 1 # the part I modified so that at all times, for any node current, current.subtree_size represents the number of nodes within the subtree. 
                return None
            elif current.left is None:
                self.length -= 1 # the part I modified so that at all times, for any node current, current.subtree_size represents the number of nodes within the subtree. 
                return current.right
            elif current.right is None:
                self.length -= 1 # the part I modified so that at all times, for any node current, current.subtree_size represents the number of nodes within the subtree. 
                return current.left

            # general case => find a successor
            succ = self.get_successor(current)
            current.key  = succ.key
            current.item = succ.item
            current.right = self.delete_aux(current.right, succ.key)

        return current

    def get_successor(self, current: TreeNode) -> TreeNode:
        """
            Get successor of the current node.
            It should be a child node having the smallest key among all the
            larger keys.

            :complexity: O(self.get_minimal())
            - balanced BST
            :best case == worst case: O(depth) = O(logn), where n is the number of nodes and depth is the depth levels the BST has

            - inbalanced BST
            :best case: O(1), when the BST is extremely inbalanced, and the left child from the root is only 1
            :worst case: O(n), when the BST is extremely inbalanced that the BST resemble a linked list and traversing through it takes O(N) time
            where n is the number of nodes
        """
        return self.get_minimal(current.right)

    def get_minimal(self, current: TreeNode) -> TreeNode:
        """
            Get a node having the smallest key in the current sub-tree.

            :complexity
            - balanced BST
            :best case == worst case: O(depth) = O(logn), where n is the number of nodes and depth is the depth levels the BST has

            - inbalanced BST
            :best case: O(1), when the BST is extremely inbalanced, and the left child from the root is only 1
            :worst case: O(n), when the BST is extremely inbalanced that the BST resemble a linked list and traversing through it takes O(N) time
            where n is the number of nodes
        """
        if current is None:
            return None
        elif current.left is None:
            return current
        else:
            return self.get_minimal(current.left)

    def is_leaf(self, current: TreeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """

        return current.left is None and current.right is None

    def draw(self, to=sys.stdout):
        """ Draw the tree in the terminal. """

        # get the nodes of the graph to draw recursively
        self.draw_aux(self.root, prefix='', final='', to=to)

    def draw_aux(self, current: TreeNode, prefix='', final='', to=sys.stdout) -> K:
        """ Draw a node and then its children. """

        if current is not None:
            real_prefix = prefix[:-2] + final
            print('{0}{1}'.format(real_prefix, str(current.key)), file=to)

            if current.left or current.right:
                self.draw_aux(current.left,  prefix=prefix + '\u2551 ', final='\u255f\u2500', to=to)
                self.draw_aux(current.right, prefix=prefix + '  ', final='\u2559\u2500', to=to)
        else:
            real_prefix = prefix[:-2] + final
            print('{0}'.format(real_prefix), file=to)

    def kth_smallest(self, k: int, current: TreeNode) -> TreeNode:
        """
        Finds the kth smallest value by key in the subtree rooted at current.
        """
        if k > current.subtree_size:
            raise ValueError("Out of Bounds")
        else:
            if k == 0:
                k = 1
            return self.inorder_traversal(k, current)
        
    def inorder_traversal(self, k: int, current: TreeNode): 

        node_index = current.subtree_size - (current.right.subtree_size if current.right else 0)

        if k == node_index:
            return current
        
        elif k < node_index:
            return self.inorder_traversal(k, current.left)

        elif k > node_index:
            return self.inorder_traversal(k-node_index, current.right)
    
    def inorder_limit(self, root, ordered_list, start, end):
        if root:
            if root.key > start:
                self.inorder_limit(root.left,ordered_list, start, end)

            if start < root.key <= end:
                ordered_list.append(root)

            if root.key < end:
                self.inorder_limit(root.right,ordered_list, start, end)
            

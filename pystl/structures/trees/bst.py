from error import EmptyTreeError
from models.abstract_tree import AbstractTree
from structures.node_structure.tree_node import TreeNode

class BinarySearchTree(AbstractTree):
    def __init__(self, lst=None):
        self.root = None
        self.size = 0
        if lst:
            for val in lst:
                self.push(val)

    def push(self, val):
        """Inserts a new element into the binary search tree."""

        new_node = TreeNode(val)
        if not self.root:
            self.root = new_node
        else:
            self._push_recursive(self.root, new_node)
        self.size += 1
    
    def _push_recursive(self, current, new_node):
        """Helper function for recursive insert."""

        if new_node.val < current.val:
            if current.left:
                self._push_recursive(current.left, new_node)
            else:
                current.left = new_node
        else:
            if current.right:
                self._push_recursive(current.right, new_node)
            else:
                current.right = new_node 
    
    def pop(self, val):
        """Removes an element from the binary tree."""

        if not self.root:
            raise EmptyTreeError

        self.root, removed = self._pop_recursive(self.root, val)
        if removed:
            self.size -= 1
    
    def _pop_recursive(self, current, val):
        """Helper function for recursive remove."""

        if not current:
            return None, None

        if val < current.val:
            current.left, removed = self._pop_recursive(current.left, val)
        elif val > current.val:
            current.right, removed = self._pop_recursive(current.right, val)
        else:
            # Node to be removed found
            removed = current
            if not current.left:
                return current.right, removed
            elif not current.right:
                return current.left, removed
            # Node has two children, find the inorder successor (smallest node in the right subtree)
            min_node = self._find_min(current.right)
            current.val = min_node.val
            current.right, _ = self._pop_recursive(current.right, min_node.val)

        return current, removed

    def _find_min(self, node):
        """Finds the smallest node in a subtree."""

        while node.left:
            node = node.left
        return node

    def empty(self):
        """Checks if the binary tree is empty."""

        return self.size == 0

    def __len__(self):
        return self.size

    def __iter__(self):
        self.inorder_list = []
        self._inorder_traversal(self.root)
        return iter(self.inorder_list)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            self.inorder_list.append(node.val)
            self._inorder_traversal(node.right)
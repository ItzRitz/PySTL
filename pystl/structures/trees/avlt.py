from error import EmptyTreeError
from models.abstract_tree import AbstractTree
from structures.node_structure.avl_node import AVLNode


class AVLTree(AbstractTree):
    def __init__(self, lst):
        self.root = None
        self.size = 0
        if lst is not None:
            for val in lst:
                self.push(val)

    def push(self, val):
        """Inserts a new element into the AVL tree."""
        new_node = AVLNode(val)
        if not self.root:
            # If the tree is empty, the new node becomes the root.
            self.root = new_node
        else:
            # Otherwise, perform a recursive insert and balance the tree.
            self.root = self._push_recursive(self.root, new_node)
        self.size += 1

    def _push_recursive(self, current, new_node):
        """Helper function for recursive insert and AVL balancing."""
        if not current:
            return new_node

        if new_node.val < current.val:
            current.left = self._push_recursive(current.left, new_node)
        else:
            current.right = self._push_recursive(current.right, new_node)

        # Update height of the current node.
        current.height = 1 + max(self._get_height(current.left), self._get_height(current.right))

        # Perform balancing.
        balance = self._get_balance(current)

        # Left Left Case
        if balance > 1 and new_node.val < current.left.val:
            return self._rotate_right(current)

        # Right Right Case
        if balance < -1 and new_node.val > current.right.val:
            return self._rotate_left(current)

        # Left Right Case
        if balance > 1 and new_node.val > current.left.val:
            current.left = self._rotate_left(current.left)
            return self._rotate_right(current)

        # Right Left Case
        if balance < -1 and new_node.val < current.right.val:
            current.right = self._rotate_right(current.right)
            return self._rotate_left(current)

        return current

    def pop(self, val):
        """Removes an element from the AVL tree."""
        if not self.root:
            raise EmptyTreeError

        # Perform a recursive remove and balance the tree.
        self.root = self._pop_recursive(self.root, val)
        if self.root:
            self.size -= 1

    def _pop_recursive(self, current, val):
        """Helper function for recursive remove and AVL balancing."""
        if not current:
            return None

        if val < current.val:
            current.left = self._pop_recursive(current.left, val)
        elif val > current.val:
            current.right = self._pop_recursive(current.right, val)
        else:
            # Node to be removed found.
            if not current.left:
                return current.right
            elif not current.right:
                return current.left

            # Node has two children, find the inorder successor (smallest node in the right subtree).
            min_node = self._find_min(current.right)
            current.val = min_node.val
            current.right = self._pop_recursive(current.right, min_node.val)

        # Update height of the current node.
        current.height = 1 + max(self._get_height(current.left), self._get_height(current.right))

        # Perform balancing.
        balance = self._get_balance(current)

        # Left Left Case
        if balance > 1 and self._get_balance(current.left) >= 0:
            return self._rotate_right(current)

        # Right Right Case
        if balance < -1 and self._get_balance(current.right) <= 0:
            return self._rotate_left(current)

        # Left Right Case
        if balance > 1 and self._get_balance(current.left) < 0:
            current.left = self._rotate_left(current.left)
            return self._rotate_right(current)

        # Right Left Case
        if balance < -1 and self._get_balance(current.right) > 0:
            current.right = self._rotate_right(current.right)
            return self._rotate_left(current)

        return current

    def _find_min(self, node):
        """Finds the smallest node in a subtree."""
        while node.left:
            node = node.left
        return node

    def empty(self):
        """Checks if the AVL tree is empty."""
        return self.size == 0

    def __len__(self):
        """Returns the size of the AVL tree."""
        return self.size

    def __iter__(self):
        """Iterates through the AVL tree using an inorder traversal."""
        self.inorder_list = []
        self._inorder_traversal(self.root)
        return iter(self.inorder_list)

    def _inorder_traversal(self, node):
        """Helper function for inorder traversal."""
        if node:
            self._inorder_traversal(node.left)
            self.inorder_list.append(node.val)
            self._inorder_traversal(node.right)

    def _get_height(self, node):
        """Gets the height of a node (returns 0 for None)."""
        return node.height if node else 0

    def _get_balance(self, node):
        """Calculates the balance factor of a node."""
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        """Performs a left rotation."""
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, y):
        """Performs a right rotation."""
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x
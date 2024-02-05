from error import ElementNotFoundError
from models.abstract_tree import AbstractTree
from structures.node_structure.rb_node import RBNode

class RedBlackTree(AbstractTree):
    def __init__(self, lst):
        self.NIL = RBNode(None, color="BLACK")  # Sentinel node with black color
        self.root = self.NIL
        self.size = 0
        if lst is not None:
            for val in lst:
                self.push(val)

    def push(self, val):
        """Inserts a new element into the Red-Black Tree."""
        new_node = RBNode(val)
        self._insert(new_node)
        self.size += 1

    def _insert(self, z):
        """Helper function for insert operation."""
        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right

        z.parent = y

        if y == self.NIL:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z

        z.left = self.NIL
        z.right = self.NIL
        z.color = "RED"
        self._insert_fixup(z)

    def _insert_fixup(self, z):
        """Fixes the Red-Black Tree properties after insert."""
        while z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self._left_rotate(z.parent.parent)

        self.root.color = "BLACK"

    def _left_rotate(self, x):
        """Performs a left rotation."""
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        """Performs a right rotation."""
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def pop(self, val):
        """Removes an element from the Red-Black Tree."""
        z = self._search(val)
        if z == self.NIL:
            raise ElementNotFoundError(f"Element {z} not found in the tree")
        
        self._delete(z)
        self.size -= 1

    def _search(self, val):
        """Searches for a node with the given data."""
        current = self.root
        while current != self.NIL and current.val != val:
            if val < current.val:
                current = current.left
            else:
                current = current.right
        return current

    def _delete(self, z):
        """Deletes a node from the Red-Black Tree."""
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == "BLACK":
            self._delete_fixup(x)

    def _delete_fixup(self, x):
        """Fixes the Red-Black Tree properties after delete."""
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self._right_rotate(x.parent)
                    x = self.root

        x.color = "BLACK"

    def _transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, x):
        while x.left != self.NIL:
            x = x.left
        return x

    def __len__(self):
        """Returns the size of the Red-Black Tree."""
        return self.size

    def __iter__(self):
        """Iterates through the Red-Black Tree using an inorder traversal."""
        self.inorder_list = []
        self._inorder_traversal(self.root)
        return iter(self.inorder_list)

    def _inorder_traversal(self, node):
        if node != self.NIL:
            self._inorder_traversal(node.left)
            self.inorder_list.append(node.data)
            self._inorder_traversal(node.right)

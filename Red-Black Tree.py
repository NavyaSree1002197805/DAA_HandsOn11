class Node:
    def __init__(self, value, color='RED'):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, 'BLACK')
        self.root = self.NIL

    def insert(self, value):
        new_node = Node(value)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'RED'
        self.balance_after_insertion(new_node)

    def balance_after_insertion(self, node):
        while node != self.root and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._left_rotate(node.parent.parent)
        self.root.color = 'BLACK'

    def delete(self, value):
        node = self.search(value)
        if node is None:
            return
        self._delete_node(node)

    def _delete_node(self, node):
        y = node
        y_original_color = y.color
        if node.left == self.NIL:
            x = node.right
            self.replace_node(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self.replace_node(node, node.left)
        else:
            y = self.minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.replace_node(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.replace_node(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_original_color == 'BLACK':
            self.balance_after_deletion(x)

    def balance_after_deletion(self, node):
        while node != self.root and node.color == 'BLACK':
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self._left_rotate(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == 'BLACK' and sibling.right.color == 'BLACK':
                    sibling.color = 'RED'
                    node = node.parent
                else:
                    if sibling.right.color == 'BLACK':
                        sibling.left.color = 'BLACK'
                        sibling.color = 'RED'
                        self._right_rotate(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    sibling.right.color = 'BLACK'
                    self._left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self._right_rotate(node.parent)
                    sibling = node.parent.left
                if sibling.right.color == 'BLACK' and sibling.left.color == 'BLACK':
                    sibling.color = 'RED'
                    node = node.parent
                else:
                    if sibling.left.color == 'BLACK':
                        sibling.right.color = 'BLACK'
                        sibling.color = 'RED'
                        self._left_rotate(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    sibling.left.color = 'BLACK'
                    self._right_rotate(node.parent)
                    node = self.root
        node.color = 'BLACK'

    def replace_node(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def search(self, value):
        current = self.root
        while current != self.NIL:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.NIL:
            node = node.right
        return node

    def inorder_traversal(self, node, result):
        if node != self.NIL:
            self.inorder_traversal(node.left, result)
            if node.color == 'RED':
                result.append(f"{node.value} (RED)")
            else:
                result.append(f"{node.value} (BLACK)")
            self.inorder_traversal(node.right, result)

    def contains_value(self, value):
        node = self.search(value)
        return node is not None

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

#Example
if __name__ == "__main__":
    RBtree = RedBlackTree()
    values = [17, 3, 28, 11, 25, 38, 14, 46]
    for value in values:
        RBtree.insert(value)

    print("Inorder traversal of the Red-Black Tree:")
    result = []
    RBtree.inorder_traversal(RBtree.root, result)
    print(result)

    print("Search for the Key 28")
    print(RBtree.contains_value(28))   # True

    print("Deleting 11 from the tree:")
    RBtree.delete(11)
    result = []
    RBtree.inorder_traversal(RBtree.root, result)
    print(result)

'''

Output:
Inorder traversal of the Red-Black Tree:
['3 (RED)', '11 (BLACK)', '14 (RED)', '17 (BLACK)', '25 (BLACK)', '28 (RED)', '38 (BLACK)', '46 (RED)']
Search for the Key 28
True
Deleting 11 from the tree:
['3 (RED)', '14 (BLACK)', '17 (BLACK)', '25 (BLACK)', '28 (RED)', '38 (BLACK)', '46 (RED)']

'''

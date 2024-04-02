class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.insert_key_recursive(self.root, key)

    def insert_key_recursive(self, node, key):
        if not node:
            return AVLTreeNode(key)
        elif key < node.key:
            node.left = self.insert_key_recursive(node.left, key)
        else:
            node.right = self.insert_key_recursive(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)

        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)

        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, key):
        self.root = self.delete_key_recursive(self.root, key)

    def delete_key_recursive(self, root, key):
        if not root:
            return root

        elif key < root.key:
            root.left = self.delete_key_recursive(root.left, key)

        elif key > root.key:
            root.right = self.delete_key_recursive(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete_key_recursive(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)

        if balance > 1 and self._get_balance(root.left) >= 0:
            return self._right_rotate(root)

        if balance < -1 and self._get_balance(root.right) <= 0:
            return self._left_rotate(root)

        if balance > 1 and self._get_balance(root.left) < 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        if balance < -1 and self._get_balance(root.right) > 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def search(self, key):
        return self.search_key_recursive(self.root, key)

    def search_key_recursive(self, root, key):
        if not root:
            return False
        elif root.key == key:
            return True
        elif key < root.key:
            return self.search_key_recursive(root.left, key)
        else:
            return self.search_key_recursive(root.right, key)

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def _min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, root):
        if root:
            self._inorder_traversal(root.left)
            print(root.key, end=" ")
            self._inorder_traversal(root.right)


#Example
if __name__ == "__main__":
    avlt = AVLTree()
    avlt.insert(12)
    avlt.insert(3)
    avlt.insert(35)
    avlt.insert(22)
    avlt.insert(61)
    avlt.insert(87)

    print("Inorder traversal of the AVL tree:", end=" ")
    avlt.inorder_traversal()
    print("\nSearch for the Key 22:", avlt.search(22))
    avlt.delete(35)
    print("Inorder traversal of the AVL tree after deletion 35:", end=" ")
    avlt.inorder_traversal()

'''
Output:

Inorder traversal of the AVL tree: 3 12 22 35 61 87 
Search for the Key 22: True
Inorder traversal of the AVL tree after deletion 35: 3 12 22 61 87

'''


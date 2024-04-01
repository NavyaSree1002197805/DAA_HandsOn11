class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySeachTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.val:
                root.left = self._insert_recursive(root.left, key)
            else:
                root.right = self._insert_recursive(root.right, key)
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.val:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.val = self._min_value_node(root.right)
            root.right = self._delete_recursive(root.right, root.val)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.val

# Example
binaryST = BinarySeachTree()
binaryST.insert(5)
binaryST.insert(3)
binaryST.insert(2)
binaryST.insert(4)
binaryST.insert(7)
binaryST.insert(6)
binaryST.insert(8)

print("Inorder traversal of the BST:", end=" ")
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)
inorder_traversal(binaryST.root)

result = binaryST.search(3)
print("\nSearching for the key 3:", result is not None)
print("Inorder traversal of the BST after deleting 3:", end=" ")
binaryST.delete(3)
inorder_traversal(binaryST.root)

'''
Output:
Inorder traversal of the BST: 2 3 4 5 6 7 8 
Searching for the key 3: True
Inorder traversal of the BST after deleting 3: 2 4 5 6 7 8
'''

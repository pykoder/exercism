class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, value):
        if value <= self.data:
            if not self.left:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def sort(self):
        sorted_tree = []
        if self.left:
            sorted_tree.extend(self.left.sort())
        sorted_tree.append(self.data)
        if self.right:
            sorted_tree.extend(self.right.sort())
        return sorted_tree
            

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self._data = None
        if len(tree_data) < 1:
            return
        self._data = TreeNode(tree_data[0])
        for value in tree_data[1:]:
            print(f"Inserting value {value}")
            self._data.insert(value)
        print(self._data)

    def data(self):
        return self._data

    def sorted_data(self):
        if not self.data:
            return []
        return self._data.sort()

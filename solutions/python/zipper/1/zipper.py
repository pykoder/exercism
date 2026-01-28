class Zipper:
    @staticmethod
    def from_tree(tree):
        zipper = Zipper()
        zipper.stack = []
        zipper.tree = tree
        zipper.focus = tree
        return zipper

    def __init__(self):
        pass
    
    def value(self):
        return self.focus.get('value')

    def set_value(self, value):
        self.focus['value'] = value
        return self

    def left(self):
        left = self.focus.get('left')
        if not left:
            return None
        new_zipper = Zipper()
        new_zipper.focus = left
        new_zipper.tree = self.tree
        new_zipper.stack = self.stack
        new_zipper.stack.append(self.focus)
        return new_zipper

    def set_left(self, left):
        self.focus['left'] = left
        return self

    def right(self):
        right = self.focus.get('right')
        if not right:
            return None
        new_zipper = Zipper()
        new_zipper.focus = right
        new_zipper.tree = self.tree
        new_zipper.stack = self.stack
        new_zipper.stack.append(self.focus)
        return new_zipper

    def set_right(self, right):
        self.focus['right'] = right
        return self

    def up(self):
        if self.stack:
            new_zipper = Zipper()
            new_zipper.tree = self.tree
            new_zipper.focus = self.stack[-1]
            new_zipper.stack = self.stack[:-1]
            return new_zipper
        return None

    def to_tree(self):
        return self.tree

from json import dumps
import os

class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def path(self, node):
        """Find path from root to provided node"""
        if node == self.label:
            return [self.label]
        if self.children:
            for subtree in self.children:
                subpath = subtree.path(node)
                if subpath:
                    return [self.label]+subpath
        return []


    def from_pov(self, from_node):
        if from_node == self.label:
            return self
        nodes_path = self.path(from_node)
        if not nodes_path:
            raise ValueError("Tree could not be reoriented")
        root, second, *rest = nodes_path

        new_children = []
        for x in self.children:
            if x.label == second:
                pov_tree = x
            else:
                new_children.append(x)
        old_root = Tree(root, new_children)
        pov_tree.children.append(old_root)

        if len(nodes_path) == 2:
            return pov_tree
        return pov_tree.from_pov(from_node)

    def path_to(self, from_node, to_node):
        part1 = self.path(from_node)
        if not part1:
            raise ValueError("Tree could not be reoriented")
        part2 = self.path(to_node)
        if not part2:
            raise ValueError("No path found")
        prefix = os.path.commonprefix([part1, part2])
        return part1[len(prefix):][::-1]+prefix[-1:]+part2[len(prefix):]

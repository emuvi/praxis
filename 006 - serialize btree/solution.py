# Given the root to a binary tree, implement serialize(root), 
# which serializes the tree into a string, and deserialize(s), 
# which deserializes the string back into the tree.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    if node is None:
        return "#"
    return "{} {} {}".format(node.val, serialize(node.left), serialize(node.right))


def deserialize(text):
    tokens = iter(text.split())
    def parse():
        token = next(tokens)
        if token == '#':
            return None
        node = Node(token)
        node.left = parse()
        node.right = parse()
        return node
    return parse()


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
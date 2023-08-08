import random
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val} {self.left if self.left else '#'} {self.right if self.right else '#'}"


def generate(size, count=0):
    if count > size:
        return None
    root = Node(random.randint(1, 999))
    way = random.randint(0, 2)
    if way == 0 or way == 2:
        root.left = generate(size, count + 1)
    if way == 1 or way == 2:
        root.right = generate(size, count + 1)
    return root


def parse(code):
    tokens = code.split()
    if not tokens:
        return None

    def walk(root):
        val = tokens.pop(0)
        if val != '#':
            root.left = Node(val)
            walk(root.left)
        val = tokens.pop(0)
        if val != '#':
            root.right = Node(val)
            walk(root.right)

    root = Node(tokens.pop(0))
    walk(root)
    return root


def test_parser():
    for i in range(10):
        tree = generate(i)
        code = str(tree)
        parsed = parse(code)
        tester = str(parsed)
        if code == tester:
            print('Test', i, 'success!')
        else:
            print('Test', i, 'fail!!!')


def count(node):
  return count(node.left) + count(node.right) + 1 if node else 0


def increment_depth(node_depth_tuple):
    node, depth = node_depth_tuple
    return (node, depth + 1)


def deepest(node):
    if node and not node.left and not node.right:
        return (node, 1)
    if not node.left:
        return increment_depth(deepest(node.right))
    elif not node.right:
        return increment_depth(deepest(node.left))
    return increment_depth(
            max(deepest(node.left), deepest(node.right),
                    key=lambda x: x[1]))


def breadth_first_recursive(levels):
    if not any(levels):
        return
    new_level = []
    for node in levels:
        if node:
            print(node.val, end = ' ')
            new_level.extend([node.left, node.right])
    breadth_first_recursive(new_level)


def breadth_first_iterative(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end = ' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def pre_order_recursive(node):
    if node is not None:
        print(node.val, end = ' ')
        pre_order_recursive(node.left)
        pre_order_recursive(node.right)


def in_order_recursive(node):
    if node is not None:
        in_order_recursive(node.left)
        print(node.val, end = ' ')
        in_order_recursive(node.right)


def post_order_recursive(node):
    if node is not None:
        post_order_recursive(node.left)
        post_order_recursive(node.right)
        print(node.val, end = ' ')


def pre_order_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end = ' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def in_order_iterative(root):
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.val, end = ' ')
            node = node.right


def post_order_iterative(root):
    stack = []
    result = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    result.reverse()
    for val in result:
        print(val, end = ' ')

        
tree = generate(3)
print(tree)
print('Printing in BreadthFirst')
breadth_first_recursive([tree])
print()
breadth_first_iterative(tree)
print()
print('Printing in DepthFirst PreOrder')
pre_order_recursive(tree)
print()
pre_order_iterative(tree)
print()
print('Printing in DepthFirst InOrder')
in_order_recursive(tree)
print()
in_order_iterative(tree)
print()
print('Printing in DepthFirst PostOrder')
post_order_recursive(tree)
print()
post_order_iterative(tree)
print()


'''
This problem was asked by Google.
A unival tree (which stands for "universal value") is a tree 
where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''


def solution_force(root):

    def is_unival(root):
        return unival_helper(root, root.value)

    def unival_helper(root, value):
        if root is None:
            return True
        if root.value == value:
            return unival_helper(root.left, value) and unival_helper(root.right, value)
        return False

    def count_unival_subtrees(root):
        if root is None:
            return 0
        left = count_unival_subtrees(root.left)
        right = count_unival_subtrees(root.right)
        return 1 + left + right if is_unival(root) else left + right
    
    count_unival_subtrees(root)

def solution_dynamic(root):

    def helper(root):
        if root is None:
            return 0, True
        left_count, is_left_unival = helper(root.left)
        right_count, is_right_unival = helper(root.right)
        total_count = left_count + right_count
        if is_left_unival and is_right_unival:
            if root.left is not None and root.value != root.left.value:
                return total_count, False
            if root.right is not None and root.value != root.right.value:
                return total_count, False
            return total_count + 1, True
        return total_count, False
    
    def count_unival_subtrees(root):
        count, _ = helper(root)
        return count
    
    count_unival_subtrees(root)
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_leaf(node):
    return not node.left and not node.right


def count_leaves(root: TreeNode) -> int:
    total = 0
    queue = deque([root])

    while queue:
        curr = queue.pop()
        if not curr:
            continue

        if is_leaf(curr):
            total += 1

        queue.appendleft(curr.left)
        queue.appendleft(curr.right)
    return total
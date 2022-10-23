from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs(root: TreeNode) -> None:

    stack = []
    curr = root

    while stack or curr:
        while curr:
            print(curr.val)
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        curr = curr.right
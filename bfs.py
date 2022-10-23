from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs(root: TreeNode) -> None:
    queue = deque([root])
    while queue:
        curr = queue.pop()
        if not curr:
            continue
        print(curr.val)
        queue.appendleft(curr.left)
        queue.appendleft(curr.right)
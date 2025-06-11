from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node({self.val})'


# BFS
# Time Complexity: O(n)
# Space Complexity:
#   - O(n) space for the queue
#   - O(h) space for the output array
# where:
#   - n is the number of nodes
#   - h is the height of the binary tree
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        nodes_queue = deque((root,))
        result = []

        while nodes_queue:
            result.append(nodes_queue[-1].val)
            for _ in range(len(nodes_queue)):
                current = nodes_queue.popleft()
                if current.left:
                    nodes_queue.append(current.left)
                if current.right:
                    nodes_queue.append(current.right)

        return result


# DFS
# Time Complexity: O(n)
# Space Complexity:
#   - O(h) space for the recursion stack
#   - O(h) space for the output array
# where:
#   - n is the number of nodes
#   - h is the height of the binary tree
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(root, level):
            if not root:
                return

            if level == len(result):
                result.append(root.val)

            dfs(root.right, level + 1)
            # process root
            dfs(root.left, level + 1)

        dfs(root, 0)
        return result

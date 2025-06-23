from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node({self.val})'


# Recursive DFS
# Time Complexity: O(n)
# Space Complexity: O(h)
# where:
#   - n is the number of nodes
#   - h is the height of the binary tree
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val

        if not root.left and not root.right:
            return targetSum == 0

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


# Iterative DFS I
# Time Complexity: O(n)
# Space Complexity: O(h)
# where:
#   - n is the number of nodes
#   - h is the height of the binary tree
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        nodes_stack = []
        node = root
        current_sum = 0

        while node or nodes_stack:
            while node:
                current_sum += node.val
                if not node.left and not node.right and current_sum == targetSum:
                    return True
                nodes_stack.append((node, current_sum))
                node = node.left

            node, current_sum = nodes_stack.pop()
            node = node.right

        return False


# Iterative DFS II
# Time Complexity: O(n)
# Space Complexity: O(h)
# where:
#   - n is the number of nodes
#   - h is the height of the binary tree
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        nodes_stack = [(root, root.val)]

        while nodes_stack:
            node, current_sum = nodes_stack.pop()
            if not node.left and not node.right and current_sum == targetSum:
                return True
            if node.right:
                nodes_stack.append((node.right, current_sum + node.right.val))
            if node.left:
                nodes_stack.append((node.left, current_sum + node.left.val))

        return False


# BFS
# Time Complexity: O(n)
# Space Complexity: O(n)
# where:
#   - n is the number of nodes
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        nodes_queue = deque(((root, root.val),))

        while nodes_queue:
            node, current_sum = nodes_queue.popleft()
            if not node.left and not node.right and current_sum == targetSum:
                return True
            if node.left:
                nodes_queue.append((node.left, current_sum + node.left.val))
            if node.right:
                nodes_queue.append((node.right, current_sum + node.right.val))

        return False

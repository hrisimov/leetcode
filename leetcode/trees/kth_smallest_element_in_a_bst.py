from typing import Optional, List


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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def inorder_dfs(root):
            if root is None:
                return None

            result = inorder_dfs(root.left)
            if result is not None:
                return result

            nonlocal count
            count += 1
            if count == k:
                return root.val

            return inorder_dfs(root.right)

        return inorder_dfs(root)


# Iterative DFS
# Time Complexity: O(n)
# Space Complexity: O(h)
# where:
#   - n is the number of nodes
#   - h is the height of the binary tree
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        nodes_stack = []
        current = root

        while current or nodes_stack:
            while current:
                nodes_stack.append(current)
                current = current.left

            current = nodes_stack.pop()

            count += 1
            if count == k:
                return current.val

            current = current.right

        return None


# Morris traversal
# Time Complexity: O(n)
# Space Complexity: O(1)
# where:
#   - n is the number of nodes
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None
        current = root

        while current:
            if current.left:
                previous = current.left

                while previous.right and previous.right != current:
                    previous = previous.right

                if not previous.right:
                    previous.right = current
                    current = current.left
                    continue

                previous.right = None

            count += 1
            if count == k:
                result = current.val

            current = current.right

        return result

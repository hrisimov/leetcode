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
# Space Complexity:
#   - O(h) space for the recursion stack
#   - O(n) space for the output array
# where:
#   - n is the number of nodes
#   - h is the height of the binary tree
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes_values = []
        self.__inorder_dfs(root, nodes_values)
        return nodes_values

    def __inorder_dfs(self, root, nodes_values):
        if not root:
            return

        self.__inorder_dfs(root.left, nodes_values)
        nodes_values.append(root.val)
        self.__inorder_dfs(root.right, nodes_values)


# Iterative DFS
# Time Complexity: O(n)
# Space Complexity:
#   - O(h) space for the stack
#   - O(n) space for the output array
# where:
#   - n is the number of nodes
#   - h is the height of the binary tree
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes_values = []
        nodes_stack = []
        current = root

        while current or nodes_stack:
            while current:
                nodes_stack.append(current)
                current = current.left

            current = nodes_stack.pop()
            nodes_values.append(current.val)
            current = current.right

        return nodes_values


# Morris traversal
# Time Complexity: O(n)
# Space Complexity:
#   - O(1) extra space
#   - O(n) space for the output array
# where:
#   - n is the number of nodes
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes_values = []
        current = root

        while current:
            if current.left:
                previous = current.left

                while previous.right and previous.right != current:
                    previous = previous.right

                if previous.right:
                    previous.right = None
                    nodes_values.append(current.val)
                    current = current.right
                else:
                    previous.right = current
                    current = current.left
            else:
                nodes_values.append(current.val)
                current = current.right

        return nodes_values

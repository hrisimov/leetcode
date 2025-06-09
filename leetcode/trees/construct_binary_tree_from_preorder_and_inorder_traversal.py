from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node({self.val})'


# DFS and dictionary I
# Time Complexity: O(n + n) => O(n)
# Space Complexity:
#   - O(n) space for the `inorder_indices` dict
#   - O(h) space for the recursion stack
# where:
#   - n is the number of nodes
#   - h is the height of the binary tree
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = {v: i for i, v in enumerate(inorder)}

        def dfs(p_start, p_end, i_start, i_end):
            if p_start > p_end or i_start > i_end:
                return None

            root = TreeNode(preorder[p_start])
            root_value_index = inorder_indices[preorder[p_start]]
            values_left = root_value_index - i_start

            root.left = dfs(p_start + 1, p_start + values_left, i_start, root_value_index - 1)
            root.right = dfs(p_start + values_left + 1, p_end, root_value_index + 1, i_end)

            return root

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)


# DFS and dictionary II
# Time Complexity: O(n + n) => O(n)
# Space Complexity:
#   - O(n) space for the `inorder_indices` dict
#   - O(h) space for the recursion stack
# where:
#   - n is the number of nodes
#   - h is the height of the binary tree
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = {v: i for i, v in enumerate(inorder)}
        p_index = 0

        def dfs(i_start, i_end):
            if i_start > i_end:
                return None

            nonlocal p_index
            root = TreeNode(preorder[p_index])
            root_value_index = inorder_indices[preorder[p_index]]
            p_index += 1

            root.left = dfs(i_start, root_value_index - 1)
            root.right = dfs(root_value_index + 1, i_end)

            return root

        return dfs(0, len(inorder) - 1)


# DFS with limit value
# Time Complexity: O(n)
# Space Complexity: O(h)
# where:
#   - n is the number of nodes
#   - h is the height of the binary tree
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        p_index = i_index = 0
        p_length = len(preorder)

        def dfs(limit_value):
            nonlocal p_index, i_index

            if p_index == p_length:
                return None

            if inorder[i_index] == limit_value:
                i_index += 1
                return None

            root = TreeNode(preorder[p_index])
            p_index += 1

            root.left = dfs(root.val)
            root.right = dfs(limit_value)

            return root

        return dfs(float('inf'))

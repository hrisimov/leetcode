from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node({self.val})'


# Recursive searching
# Time Complexity: O(h)
# Space Complexity: O(h)
# h - Height of the BST
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if val == root.val:
            return root
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)


# Iterative searching
# Time Complexity: O(h)
# Space Complexity: O(1)
# h - Height of the BST
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if val == root.val:
                break
            elif val > root.val:
                root = root.right
            else:
                root = root.left

        return root

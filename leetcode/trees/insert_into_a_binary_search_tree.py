from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node({self.val})'


# Recursive variant
# Time Complexity: O(h)
# Space Complexity: O(h)
# h - Height of the BST
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        return root


# Iterative variant
# Time Complexity: O(h)
# Space Complexity: O(1)
# h - Height of the BST
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        previous = None
        current = root

        while current:
            previous = current
            if val > current.val:
                current = current.right
            else:
                current = current.left

        if val > previous.val:
            previous.right = TreeNode(val)
        else:
            previous.left = TreeNode(val)

        return root

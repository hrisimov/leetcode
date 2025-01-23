from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node({self.val})'


def get_node_with_min_value(root):
    current = root

    while current.left:
        current = current.left

    return current


# Recursive variant 1
# Time Complexity: O(h)
# Space Complexity: O(h)
# h - Height of the BST
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left and root.right:
                min_node = get_node_with_min_value(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
            else:
                return root.left or root.right

        return root


# Recursive variant 2
# Time Complexity: O(h)
# Space Complexity: O(h)
# h - Height of the BST
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left and root.right:
                min_node = get_node_with_min_value(root.right)
                min_node.left = root.left
                return root.right
            else:
                return root.left or root.right

        return root


# Iterative variant
# Time Complexity: O(h)
# Space Complexity: O(1)
# h - Height of the BST
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        node_to_remove, parent = self.__find_node_and_its_parent(root, key)

        if not node_to_remove:
            return root

        if not parent:
            return self.__remove_root_node(node_to_remove)

        if parent.left == node_to_remove:
            parent.left = self.__remove_root_node(node_to_remove)
        else:
            parent.right = self.__remove_root_node(node_to_remove)

        return root

    def __remove_root_node(self, root):
        if root.left and root.right:
            max_node = self.__get_node_with_max_value(root.left)
            max_node.right = root.right
            return root.left
        else:
            return root.left or root.right

    @staticmethod
    def __get_node_with_max_value(root):
        current = root

        while current.right:
            current = current.right

        return current

    @staticmethod
    def __find_node_and_its_parent(root, key):
        parent = None
        current = root

        while current:
            if key > current.val:
                parent = current
                current = current.right
            elif key < current.val:
                parent = current
                current = current.left
            else:
                break

        return current, parent

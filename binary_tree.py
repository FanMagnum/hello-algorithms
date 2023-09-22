from typing import Optional


class TreeNode:
    def __init__(self, val=0):
        self.val: int = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

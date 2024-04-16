# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque()
        height = 0

        queue.append(root)

        while len(queue) > 0:
            height += 1
            for i in range(len(queue)):
                if queue:
                    currNode = queue.popleft()
                if currNode and currNode.left:
                    queue.append(currNode.left)
                if currNode and currNode.right:
                    queue.append(currNode.right)

        return height



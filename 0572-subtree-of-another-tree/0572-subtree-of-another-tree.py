
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p and q:
            return False
        
        if p and not q:
            return False

        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            for i in range(len(queue)):
                currentNode = queue.popleft()

                if self.isSameTree(currentNode, subRoot):
                    return True
                
                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)

        return False

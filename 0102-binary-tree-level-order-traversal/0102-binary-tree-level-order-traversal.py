# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        result = []

        result.append([root.val])
        queue.append(root)

        while len(queue):
            nodes = []
            for i in range(len(queue)):
                currentNode = queue.popleft()

                if currentNode.left:
                    queue.append(currentNode.left)
                    nodes.append(currentNode.left.val)
                    
                if currentNode.right:
                    queue.append(currentNode.right)
                    nodes.append(currentNode.right.val)

            if len(nodes) > 0:
                result.append(nodes)


        return result



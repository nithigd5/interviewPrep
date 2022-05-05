from collections import deque
import queue
from typing import Deque, List, Optional

from numpy import equal
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = deque()
        stack.append(root)
        while stack:
            c = stack.pop()
            res.append(c.val)
            if c.right:
                stack.append(c.right)
            if c.left:
                stack.append(c.left)
        return res
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = deque()
        cur = root
        while cur and stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = deque()
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                tmp = list(stack)[-1].right
                if not tmp:
                    tmp = stack.pop()
                    res.append(tmp.val)
                    while stack and tmp == list(stack)[-1].right:
                         tmp = stack.pop()
                         res.append(tmp.val)
                else:
                    cur = tmp
        return res
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root: return res
        q = deque()
        q.append(root)
        # visited = set()
        while q:
            size = len(list(q))
            l = []
            for _ in range(size):
                cur = q.popleft()
                # if cur not in visited:
                    # visited.add(cur)
                l.append(cur.val)   
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right) 
            res.append(l)
        return res
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l,r)+1
    depth = 0
    def maxDepthTD(self, root: Optional[TreeNode], depth = 1) -> int:
       if not root:
           return 
       if not root.left and not root.right:
           self.depth = max(self.depth, depth)
       self.maxDepthTD(root.left, depth+1)
       self.maxDepthTD(root.right, depth+1)
       
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q : Deque[TreeNode]= deque()
        q.append(root)
        while q:
            l = []
            size = len(q)
            for _ in range(size):
                c = q.popleft()
                if c.left:
                    q.append(c.left)
                    l.append(c.left.val)
                else:
                    l.append('x')
                if c.right:
                    l.append(c.right.val)
                    q.append(c.right)
                else:
                    l.append('x')
            if l != l[::-1]:
                return False
        return True
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # 遍历顺序：根节点 --> 按从左到右遍历N个子节点
        # 递归实现
        if not root:
            return []
        res = [root.val]
        for child in root.children:
            res+=self.preorder(child)
        return res        
        # 栈的迭代实现
        # 对子节点按从右到左的顺序存入栈，那么出栈的时候则正好是按从左到右的顺序。
        # 对每个节点：把要处理的节点pop出来，取值，再将其子节点按倒序入栈
        if not root:
            return []
        stack,res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for c in node.children[::-1]:
                stack.append(c)
        return res

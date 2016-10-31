# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(not root):
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while(stack):
            right = stack.pop()
            left = stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val == right.val:
                stack.append(left.left)
                stack.append(right.right)
                stack.append(right.left)
                stack.append(left.right)
            else:
                return False
        return True
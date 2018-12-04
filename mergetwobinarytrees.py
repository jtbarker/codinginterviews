class Solution(object):
    def mergeTrees(self, t1, t2):
        if t1 == None:
            return t2
        elif t2 == None:
            return t1
        
        rtn_val = TreeNode(t1.val + t2.val)
        
        if t1.left != None or t2.left != None:
            rtn_val.left = self.mergeTrees(t1.left, t2.left)
        if t1.right != None or t2.right != None:
            rtn_val.right = self.mergeTrees(t1.right, t2.right)
        
        return rtn_val


class Solution:
    def mergeTrees(self,t1,t2):
        if t1 == None:
            return t2
        elif t2 == None:
            return t1
        ans = TreeNode(t1.val + t2.val)
        if t1.left != None or t2.left != None:
            ans.left = self.mergeTrees(t1.left,t2,left)
        if t1.right != None or t2.right != None:
            ans.right = self.mergeTrees(t1.right,t2.right)
        return ans
        
        
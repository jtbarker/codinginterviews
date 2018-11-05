class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
    

        if root == None:
            return False
        self.trav = set()
        self.k = k
        self.found = False
        self.preorder(root)
        return self.found
    
    def preorder(self, node):
        if self.found:
            return
        comp = self.k - node.val
        if comp in self.trav:
            self.found = True
            return 
        else:
            self.trav.add(node.val)
        if self.found:
            return
        if node.left: self.preorder(node.left)
        if node.right: self.preorder(node.right)
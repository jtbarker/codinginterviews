class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums = set()
        def traverse(root):
            nums.add(root)
            if root-k in nums:
                return True
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            else:
                return root
        return False
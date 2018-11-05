class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        traversal = [root.val]
        for child in root.children:
            traversal.extend(self.preorder(child))
        return traversal
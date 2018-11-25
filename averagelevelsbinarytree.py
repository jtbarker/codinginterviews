class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        if not root:
            return result
        levels = [root]
        while levels:
            result.append(sum(node.val for node in levels)/float(len(levels)))
            levels = [child for node in levels for child in (node.left, node.right) if child]
        return result
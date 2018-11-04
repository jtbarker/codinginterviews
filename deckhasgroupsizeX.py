class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        sorteddeck = sorted(deck)
        sortedsetdeck = set(sorteddeck)
        counts = []
        for i in sortedsetdeck:
            counts.append(sorteddeck.count(i))
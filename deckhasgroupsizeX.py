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
        for i in counts:
            for j in (i,len(counts)):
                if i != j:
                    return False
                else:
                    return True
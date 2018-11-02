class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        evens = []
        odds = []
        for i in A:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)
        rslt = evens
        rslt.extend(odds)
        return rslt
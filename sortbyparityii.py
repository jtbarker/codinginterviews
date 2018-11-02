class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A.sort(key = lambda x: x%2) # how to use lambda expressions and keys to sort evens and odds, evens first, then odds
        even, odd = A[:len(A)//2], A[len(A)//2:]
        res = []
        for i in range(len(A)):
            if i%2==0:
                res.append(even.pop()) # pattern to use pop to add values one by one
            else:
                res.append(odd.pop())
        return res
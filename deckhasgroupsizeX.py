class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a,b):
            while b:
                a,b = b, a%b
            return a
        a = [v for k,v in collections.Counter(deck).items()]
        ans = a[0]
        for i in range(1,len(a)):
            ans = gcd(ans,a[i])
        return ans >= 2

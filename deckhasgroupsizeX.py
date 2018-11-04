class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a,b):
            while b:
                a,b = b, a%b #how to get the gcd using euclidean algo
            return a
        a = [v for k,v in collections.Counter(deck).items()] #get list of values for counts
        ans = a[0]
        for i in range(1,len(a)): #run through every count value and get the gcd for each pair of counts from beginning to end
            ans = gcd(ans,a[i])
        return ans >= 2 # if final value is not 1, true else false

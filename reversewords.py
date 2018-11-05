class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        listwords = s.split(" ")
        ans = []
        for i in listwords:
            ans.append(i[::-1]) #reverse individual words
        return " ".join(ans) #make a list into a string and add spaces between
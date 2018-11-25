class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split()
        newlist = []
        for i in reversed(lst):
            newlist.append(i)
        return ' '.join(newlist)
    
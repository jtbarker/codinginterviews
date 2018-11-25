class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        my_list = []
        
        
        while True:
          if n == 1:
            return True
          
          my_sum = 0
          
          num_str = str(n)
          
          for i in range(len(num_str)):
            my_sum += (int(num_str[i]))**2
            
          if my_sum not in my_list:
            my_list.append(my_sum)
            n = my_sum
          else:
            return False
          
class Solution:
    def isPalindrome(x):
        x_li = [i for i in str(x)]
        if not (x_li[0].isdigit()):
            return False
        x_re = []
        for n in range(len(x_li)-1,-1,-1):
            x_re.append(x_li[n])
    
        return x_li == x_re

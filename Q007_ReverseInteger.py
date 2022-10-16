class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            a = 1      
        else:
            a = -1

        xli = [int(i) for i in str(x*a)]
        res = xli[::-1]     

        num = int(''.join(map(str,res))) * a
        
        if num >= 2 ** 31 - 1 or num <= -2 ** 31:   #2的31次方是2**31， 不是2^31
            return 0

        return num 

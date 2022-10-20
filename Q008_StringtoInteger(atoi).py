class Solution:
    def myAtoi(self, s: str) -> int:
        # if s is None or len(s) <1:
        #     return 0
        # s = s.strip()
        # i = 0
        # sign = 1
        # if s[0] in ["-", "+"]:
        #     if s[0] == "-":
        #         sign = -1
        #     i+=1  

        # res = 0
        # while i < len(s) and s[i].isdigit():
        #     res = res*10 + ord(s[i]) - ord("0")
        #     i+=1
        # return max(min(res*sign, 2**32 -1), -2**31)   
        
        ls = list(s.strip())
        if not ls: return 0
        sign = 1
        if ls[0] in ['-', '+']:
            if ls[0] == '-':
                sign = -1 
            ls = ls[1:]
                    
        
        res, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            res = res*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * res, 2**31-1))

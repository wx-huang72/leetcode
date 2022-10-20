class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X":10,"L": 50, "C": 100, "D":500, "M":1000 }
        ls = [a for a in s]
        n = len(ls)
        res = roman[s[n-1]]
        for i in range(n-2, -1,-1):
            if  roman[s[i]]  >=  roman[s[i+1]]:
                res += roman[s[i]]
            else:
                res -= roman[s[i]]

        return res

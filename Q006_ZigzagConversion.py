class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        step = numRows*2 -2
        li = [w for w in s]  

        res = ""

        for i in range(numRows):
            for j in range(i, len(s), step):
                res+= s[j]
                if i != 0 and i != numRows-1 and (j+step -2*i) < len(s):
                    res+= s[j+step -2*i]

        return res       

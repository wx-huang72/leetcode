class Solution:
    def checkInclusion(s1, s2) :
        if len(s1) > len(s2): return False
        
        if len(s1) == len(s2): return sorted(s1) == sorted(s2)
        
        for i in range(len(s2)):
            if s2[i] in s1:
                s = s2[i:i + len(s1)]
                if sorted(s) == sorted(s1):
                    return True
        return False 

    checkInclusion("ab","eidbaooo")
    # Input: s1 = "ab", s2 = "eidbaooo"
    # Output: true    

    # Input: s1 = "ab", s2 = "eidboaoo"
    # Output: false
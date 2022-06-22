class Solution:
    def lengthOfLongestSubstring(s) :
#         if len(s) == 0:
#             return 0
        
#         subs = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
#         res = []
#         for sub in subs:
#             freq = Counter(sub)
#             if (len(freq) == len(sub)):
#                 res.append(sub)
#         res.sort(key=len,reverse = True)
#         # print(len(res[0]))
#         return len(res[0])

        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res    

    lengthOfLongestSubstring("abcabcbb")
    # Output: 3
       

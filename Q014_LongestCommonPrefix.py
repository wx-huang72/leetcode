"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs, key = len)
        # print(shortest_word)
  
        dic = {}
        for i in range(len(shortest_word)):
            # print(i)
            v = []
            for word in strs:
                # print(word)
                v.append(word[i])
                # print(values)
            dic[i] = v

        # print(dic)   
        ans = ""
        for value in dic.values():
            # print(value)
            if any(x != value[0] for x in value):
                break
            else:    
                ans += value[0]

        return ans    
    
            


        

from ast import List
from collections import defaultdict


class Solution:
    def groupAnagrams(strs):
        dic = defaultdict(list)
        for i in strs:
            dic["".join(sorted(i))].append(i)
        # print(dic)
        res = list(dic.values())
        print(res)
        return res

    groupAnagrams(["eat","tea","tan","ate","nat","bat"])    

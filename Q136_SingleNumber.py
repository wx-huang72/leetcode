import collections
class Solution:
    def singleNumber(self, nums):   #nums is a list of nums, and the return value is int
        counter = collections.Counter(nums)
        dic = dict(counter)
        print(dic)
        for k,v in dic.items():
            if v == 1:
                return k

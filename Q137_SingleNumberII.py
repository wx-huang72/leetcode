import collections
class Solution:
    def singleNumber(self, nums):
        counter = collections.Counter(nums)
        dic = dict(counter)
        print(dic)
        for k,v in dic.items():
            if v == 1:
                return k

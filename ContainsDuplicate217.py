class Solution(object):
    def containsDuplicate(nums):
        temp = []
        for i in nums:
            if i not in temp:
                temp.append(i)
            else:
                return True
        return False   
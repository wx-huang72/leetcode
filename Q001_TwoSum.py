class Solution:
    def twoSum(nums, target):
#         rlist = []
#         for i in range(len(nums)):
#             newlist = nums[:]
#             # print(type(newlist))
#             temp_num = nums[i]
#             newlist.pop(i)
#             for j in range(len(newlist)):
#                 if temp_num+newlist[j] == target:
#                     rlist.append(i)
#                     rlist.append(nums.index(newlist[j]))
#                     return rlist       
        prevmap = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in prevmap:
                return [prevmap[diff],i]
            prevmap[n] = i
        return

    twoSum([2,7,11,15],9)    

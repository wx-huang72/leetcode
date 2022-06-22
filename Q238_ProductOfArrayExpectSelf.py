import numpy
class Solution:
    def productExceptSelf(nums):
        # res = []
        # mul = 1
        # for i in range(len(nums)):
        #     temp = nums.copy()
        #     temp.pop(i)
        #     # print(temp)
        #     for j in temp:
        #         mul = mul * j
        #     res.append(mul) 
        #     mul = 1
        # # print(res)
        # return res
        

        res = [1] * (len(nums))
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

    productExceptSelf([1,2,3,4])
    # Output: [24,12,8,6]    

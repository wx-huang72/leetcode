class Solution:
    def longestConsecutive(nums):
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        print(longest)        
        return longest
                
    longestConsecutive([1,200,100,2,3,4])    

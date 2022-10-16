import statistics
#nums1 and nums2 are both list of ints and the return result should be float
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        #Method 1   Merge-sort
        # li = []
        # i = j = 0
        # while i<len(nums1) and j <len(nums2):
        #     if(nums1[i] > nums2[j]):
        #         li.append(nums2[j])
        #         j+=1
        #     else:
        #         li.append(nums1[i])
        #         i+=1
        # li = li+nums1[i:] + nums2[j:]
        
        # Method 2 
        li = sorted(nums1 + nums2) 
        
        
        return median(li)

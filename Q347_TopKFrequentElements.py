class Solution:
    def topKFrequent(nums, k) :
        #Approach 1
        count={}
        for i in nums:
            count[i] = nums.count(i)
        sorted_count ={k: v for k, v in sorted(count.items(), key=lambda item: item[1],reverse=True)}
        keys = list(sorted_count.keys())
        res = keys[:k]
        print(res)
        return res

        #Approach 2
        # count = {}
        # freq = [[] for i in range(len(nums)+1)]
        
        # for n in nums:
        #     count[n] = 1+count.get(n,0)
        # for n,c in count.items():
        #     freq[c].append(n)
            
        # res = []
        # for i in range(len(freq) - 1,0,-1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res


    topKFrequent([1,1,1,2,2,3],2)    
    # output: [1,2]

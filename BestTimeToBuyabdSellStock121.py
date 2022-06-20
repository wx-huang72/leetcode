class Solution:
    def maxProfit(prices):
        res = 0
        l = 0
        
        for i in range(1,len(prices)):
            if prices[i]<prices[l]:
                l = i
            res = max(prices[i]-prices[l],res)    
        return res 

    maxProfit([7,1,5,3,6,4])
    # Expected Output:5
        
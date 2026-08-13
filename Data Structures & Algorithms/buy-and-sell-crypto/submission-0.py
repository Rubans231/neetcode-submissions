class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxprof = 0

        for price in prices:

            if price < buy:    
                buy = price
            
            elif price - buy > maxprof:
                maxprof = price - buy
        return maxprof
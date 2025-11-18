class Solution(object):
    def maxProfit(self, prices):
        prefix = prices[0]     
        maxx = 0              

        for i in range(1, len(prices)):
            
            current_profit = prices[i] - prefix
            if current_profit > maxx:
                maxx = current_profit

            if prices[i] < prefix:
                prefix = prices[i]

        return maxx




        
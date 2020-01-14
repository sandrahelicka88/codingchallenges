import unittest
'''Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.'''

def maxProfit(prices):
    if len(prices) == 0:
        return 0
    minPrice = prices[0]
    maxProfit = 0
    for i in range(1, len(prices)):
        if prices[i]<minPrice:
            minPrice = prices[i]
        else:
            maxProfit = max(maxProfit, prices[i]-minPrice)
    return maxProfit


class Test(unittest.TestCase):
    def test_stock(self):
        output = maxProfit([])
        self.assertEqual(output,0)
        output2 = maxProfit([7,6,4,3,1])
        self.assertEqual(output2,0)
        output3 = maxProfit([7,1,5,3,6,4])
        self.assertEqual(output3,5)
    

if __name__ == '__main__':
    unittest.main()
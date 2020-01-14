import unittest
'''Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).'''

def maxProfit(prices):
    if len(prices) == 0:
        return 0
    result = 0
    for i in range(1, len(prices)):
        if prices[i]-prices[i-1]>0:
            result+=prices[i]-prices[i-1]
    return result

class Test(unittest.TestCase):
    def test_profit(self):
        output = maxProfit([])
        self.assertEqual(output,0)
        output2 = maxProfit([7,1,5,3,6,4])
        self.assertEqual(output2,7)
        output3 = maxProfit([1,2,3,4,5])
        self.assertEqual(output3,4)
        output4 = maxProfit([7,6,4,3,1])
        self.assertEqual(output4,0)

if __name__ == '__main__':
    unittest.main()
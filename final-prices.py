# Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

# Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.

# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation:
# For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
# For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
# For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
# For items 3 and 4 you will not receive any discount at all.

def finalPrices(prices):
    final_price = []

    for i in range(len(prices)):
        n = i+1
        count = 0
        while n < len(prices):
            if prices[i] >= prices[n]:
                final_price.append(prices[i]-prices[n])
                count += 1
                break
            n += 1
        if count == 0:
            final_price.append(prices[i])

    return final_price


print(finalPrices([8, 4, 6, 2, 3]))  # -> [4,2,4,2,3]
print(finalPrices([10, 1, 1, 6]))  # -> [9,0,1,6]
print(finalPrices([8, 7, 4, 2, 8, 1, 7, 7, 10, 1]))  # -> [1,3,2,1,7,0,0,6,9,1]

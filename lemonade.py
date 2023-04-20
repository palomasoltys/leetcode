# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# Note that you do not have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

def lemonadeChange(bills):
    if bills[0] > 5:
        return False
    # create a change array variable to store the change
    change = []
    # iterate through bills
    for bill in bills:
        # if bills equal to 5, add to the change array
        if bill == 5:
            change.append(bill)
        # if bills equal to 10, check if there is 5 in change array
        elif bill == 10:
            if 5 in change:
                # if yes, pop from change and add 10 to change
                change.remove(5)
                change.append(bill)
            # if not, return false
            else:
                return False
        # if bills equal to 20, check if there is 5 in change
        elif bill == 20:
            if 5 not in change:
                # if not, return false
                return False
            # if yes, check if there is a 10, if yes pop 10 and 5 and add 20 to change
            else:
                if 10 in change:
                    change.remove(10)
                    change.remove(5)
                    change.append(bill)
                # if yes, check to see if there is another 5, if yes pop both 5 and add 20
                elif change.count(5) > 2:
                    change.remove(5)
                    change.remove(5)
                    change.remove(5)
                    change.append(bill)
                else:
                    return False
    # return true
    return True


print(lemonadeChange([5, 5, 5, 10, 5, 5, 10, 20, 20, 20]))  # false
print(lemonadeChange([5, 5, 5, 5, 20, 20, 5, 5, 20, 5]))  # false
print(lemonadeChange([5, 5, 5, 20, 5, 5, 5, 20, 5, 5,
      5, 10, 5, 20, 10, 20, 10, 20, 5, 5]))  # false

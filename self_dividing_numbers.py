# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.

# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

def selfDividingNumbers(left, right):
    # create an empty list to store the result
    res = []
    # iterate through the range (left, right)
    for n in range(left, right+1):
        # separate the digits and check if curr number mod the separated dig equals to 0
        string = str(n)
        if "0" in string:
            continue
        self_dividing = True
        for s in string:
            if not (n % int(s) == 0):
                self_dividing = False
        if self_dividing:
            res.append(n)
    # return the result array
    return res


print(selfDividingNumbers(47, 85))  # [48,55,66,77]

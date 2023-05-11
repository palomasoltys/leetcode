# It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from  to . Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

# Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

# Example
# If person  bribes person , the queue will look like this: . Only  bribe is required. Print 1.
# Person  had to bribe  people to get to the current position. Print Too chaotic.
# q = [2, 1, 5, 3, 4] -> 3
# q = [2, 5, 1, 3, 4] -> Too chaotic

def minimumBribes(q):
    count = 0
    for i in range(1, len(q)):
        if q[i-1] < q[i]:
            if i == len(q) - 1:
                print(count)
            continue
        else:
            if q[i-1] - q[i] > 2:
                print("Too chaotic")
                break
            else:
                count += q[i-1] - q[i]
        if i == len(q) - 1:
            print(count)


minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])  # 7
minimumBribes([2, 1, 5, 3, 4])
minimumBribes([2, 5, 1, 3, 4])

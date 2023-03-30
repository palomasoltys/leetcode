# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

def asteroidCollision(asteroids):
    s = []
    for a in asteroids:
        while s and s[-1] > 0 and a < 0:
            if s[-1] + a < 0:
                s.pop()
            elif s[-1] + a > 0:
                break
            else:
                s.pop()
                break
        else:
            s.append(a)
    return s


print(asteroidCollision([5, 10, -5]))  # [5,10]
print(asteroidCollision([8, -8]))  # []
print(asteroidCollision([10, 2, -5]))  # 10
print(asteroidCollision([-2, -1, 1, 2]))  # [-2, -1, 1, 2]

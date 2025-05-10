# 5. Maximum of Three Numbers
# Write a function max_of_three(a, b, c) that returns the largest of the three.
def max_of_three(a, b, c):
    return max(a, b, c)     
# Test the function 
result = max_of_three(3, 7, 5)
print("The maximum of 3, 7, and 5 is:", result)  # Output: The maximum of 3, 7, and 5 is: 7

# Write a function max_of_three(a, b, c) that returns the largest of the three without using max() function.
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
result = max_of_three(8, 8, 5)
print("The maximum of 3, 7, and 5 is:", result)
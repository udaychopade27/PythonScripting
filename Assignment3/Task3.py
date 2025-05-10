# 3. Add Two Numbers
# Write a function add(a, b) that returns the sum.

def sum(num1, num2):
    return num1 + num2

# Test the function
result = sum(5, 7)
print("The sum is:", result)  # Output: The sum is: 12
# 4. Factorial Function
# Write a function factorial(n) that returns the factorial of n.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Test the function
result = factorial(5)
print("The factorial is:", result)  # Output: The factorial is: 120

# 5. Fibonacci Sequence
# Write a function fibonacci(n) that returns the Fibonacci sequence.
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence 
# Test the function
result = fibonacci(10)  
print("The Fibonacci sequence is:", result)  # Output: The Fibonacci sequence is: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 6. Palindrome Checker
# Write a function is_palindrome(s) that checks if a string is a palindrome.        
def is_palindrome(s):
    return s == s[::-1] 
# Test the function
result = is_palindrome("racecar")
print("Is 'racecar' a palindrome?", result)  # Output: Is 'racecar' a palindrome? True  

# 7. Prime Number Checker       
# Write a function is_prime(n) that checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Test the function        
result = is_prime(7)
print("Is 7 a prime number?", result)  # Output: Is 7 a prime number? True

# 8. Count Vowels in a String
# Write a function count_vowels(s) that counts the number of vowels in a string.    
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
# Test the function         
result = count_vowels("Hello, World!")  
print("Number of vowels:", result)  # Output: Number of vowels: 3     

  
# 9. Reverse a String
# Write a function reverse_string(s) that reverses a string.        
def reverse_string(s):
    return s[::-1]  
# Test the function 

result = reverse_string("Hello, World!")
print("Reversed string:", result)  # Output: Reversed string: !dlroW ,olleH


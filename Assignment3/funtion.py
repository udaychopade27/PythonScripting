# 🔵 1. Defining a Function
def greet():
    print("Hello!")
greet()

# 🔵 2. Function with Parameters
def greet(name):
    print("Hello, " + name + "!")
greet("Alice")
greet("Bob")

# 🔵 3. Function with Return Value
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # Output: 7

# 🔵 4. Function with Default Parameter
def greet(name="World"):
    print("Hello, " + name + "!")
greet()  # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice!
# 🐍 Python Beginner Lesson 4 – Functions

In Lesson 3, we learned how to write and use **functions** to make our code more organized and reusable.

---

## 📘 What is a Function?

A **function** is a reusable block of code that performs a specific task.

---

## ✅ 1. Defining a Function

```python
def greet():
    print("Hello!")
```

Call it like this:

```python
greet()
```

---

## ✅ 2. Function with Parameters

```python
def greet(name):
    print("Hello, " + name + "!")
```

```python
greet("Alice")
greet("Bob")
```

---

## ✅ 3. Function with Return Value

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # Output: 7
```

---

## 🧠 Why Use Functions?

- Makes code reusable
- Easier to organize and maintain
- Improves readability and testing

---

## ✏️ Assignment

### 1. Simple Greeter Function
Write a function that prints "Hello, world!" and call it.

### 2. Personalized Greeter
Write a function `greet(name)` that prints `"Hello, [name]!"`

### 3. Add Two Numbers
Write a function `add(a, b)` that returns the sum.

### 4. Check Even or Odd
Write a function `is_even(n)` that returns `True` if even, otherwise `False`.

### 5. Maximum of Three Numbers (without using `max()`)

```python
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
```

---

## 💡 Tip
Functions help break down problems into smaller pieces. Use them as building blocks in your code! 🧱

Happy coding! 🧑‍💻

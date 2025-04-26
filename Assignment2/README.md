# 🐍 Python Beginner Lesson 3 – Loops

Welcome back!  
In Lesson 3, we learned how to use **loops** in Python to repeat actions automatically.

---

## 📘 Lesson 3: Loops Basics

### ✅ 1. For Loop
Use a `for` loop when you know how many times to repeat.

```python
for number in range(5):
    print(number)
```

- `range(5)` gives numbers 0, 1, 2, 3, 4.

### ✅ 2. While Loop
Use a `while` loop when you want to repeat **until a condition is false**.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

- It prints numbers 0 to 4.

### ✅ 3. Loop Control (break and continue)
- `break` → Stops the loop early
- `continue` → Skips one loop step and continues

Example:

```python
for num in range(10):
    if num == 5:
        break
    print(num)
```

```python
for num in range(5):
    if num == 2:
        continue
    print(num)
```

---

## 🧠 Assignment

Practice using loops with these tasks:

### 1. Print numbers 1 to 10 using a for loop.

### 2. Print "Hello" 5 times using a while loop.

### 3. Number Guessing Game
Ask the user to guess a number between 1 and 10. Keep asking until they guess correctly.

### 4. Print only even numbers from 1 to 20
Use a `for` loop and `continue` to skip odd numbers.

---

## 💡 Tip
Test your programs often!  
Break big problems into small steps. 🧩

Happy coding! 🚀

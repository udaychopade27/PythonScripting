# Print only even numbers from 1 to 20 using a for loop and continue statement.
for number in range(1, 21):
    if number % 2 != 0:
        continue
    print(number)   
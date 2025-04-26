# for loop
for number in range(5):
    print(number)
    
# while loop
count = 0
while count < 5:
    print(count)
    count += 1  

# break → Stop the loop immediately
for num in range(10):
    if num == 5:
        break
    # This will print 0–4 and stop when 5 is reached.
    print(num)

# continue → Skip the current step and continue with the next one
for num in range(5):
    if num == 2:
        continue
    #  This prints 0, 1, skips 2, then 3, 4.
    print(num)



# For-Lop in Python:~
# In For Loop we do.
# 1)to print number with help of 'for-loop'
# 2)to print string
# 3)to print Arrays

#Print 0 to 10 numbers:
for i in range(1,11):
    print(i)

# Example2:
for i in range(1,21,2):      # (start, stop, increment)
    print(i)

# ro print Array:     (Contain same data type values)
name = ['ashfaq', 'safdar', 'irfan']
for i in name:
    print(i)

# to print string:
name = 'Ashfaq'
for i in name:
    print(i)

# while-Loop in Python:
# In while loop its runt but even a specify condition is false/wrong it will stop there.
steps = 1
while steps < 21:
    print(steps)
    steps = steps + 1

# Example2:
steps = 1
while steps < 21:
    print(steps)
    steps = steps + 2

# Break, Continue in Python:
# Break Statement:
i = 1
while i <10:
    print(i)
    i = i + 1
    if i == 5:
         break

# Continue Statement:
name = ['ashfaq', 'irfan', 'safdar']
for i in name:
    if i == 'irfan':
        continue
        print(i)

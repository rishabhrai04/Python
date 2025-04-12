# Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter a number: "))
# 5! = 5 * 4 * 3 * 2 * 1 = 120
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}")
# Write a python function to print multipplication table of a given number.

def multiply(n):
    for i in range(1, 11):
        print(f"{n}*{i} = {n*i}")

multiply(5)
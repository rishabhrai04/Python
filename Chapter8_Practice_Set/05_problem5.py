# Write a python function which converts inches to cms.
# ***
# **
# *     for n=3

def pattern(n):
    if (n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(5)

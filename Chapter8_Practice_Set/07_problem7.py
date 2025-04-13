# Write a python function to remove a given word from a list ad strip it at the same time.
def rem(i,word):
    n=[]
    for item in l:
        n.append(item.strip(word))
    return n


l = ["Harry","Rohan","Shubham","an"]

print(rem(1,"an"))
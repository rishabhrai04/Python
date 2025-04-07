s = { 1, 5, 32, 54, 5, 5, 5, "Rahul" }

print(s,type(s))  # {32, 1, 5, 54, 'Rahul'}

s.add(566)
print(s,type(s))  # {32, 1, 5, 54, 'Rahul', 566}
s.remove(1)
print(s,type(s))  # {32, 5, 54, 'Rahul', 566}
s.discard(32)
print(s,type(s))  # {5, 54, 'Rahul', 566}
s.discard(100) # No error if the element is not present
print(s,type(s))  # {5, 54, 'Rahul', 566}
s.pop() # Removes the last element
print(s,type(s))  # {54, 'Rahul', 566}
s.clear() # Removes all elements from the set
print(s,type(s))  # set()
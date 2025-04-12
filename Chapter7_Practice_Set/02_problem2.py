# Write a program to greet all the person names stored in a list 'l' and which starts with S.
# l =["Harry", "Sandy", "John", "Samantha", "Michael"]

l = ["Harry", "Sandy", "John", "Samantha", "Michael"]

for name in l:
    if name.startswith("S"):
        print(f"Hello {name}, welcome!")  # Greet the person
    else:
        print(f"Hi {name}, welcome!")  # Greet the person with a different message
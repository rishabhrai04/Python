class Employee:
    
    language = "Py"  # This is class attribute 
    salary = 1200000

harry = Employee()
harry.name = "Harry"  # This is an instance attribute
print(harry.name,harry.salary,harry.language)

rohan = Employee()
rohan.name = "Rohan"
print(rohan.name,rohan.salary,rohan.language)

#Here name is instance attribute and salary and language are class attributes as they directly belong to the class.
class Employee:
    language = "Python"  # This is a class attribute.
    salary = 1200000

    def __init__(self):  # Dunder method which is automatically called.
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

harry = Employee()
harry.name = "Harry"
print(harry.name,harry.salary)
    
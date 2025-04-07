d = {} # Empty dictionary
marks ={
    "Rohan": 100,
    "Shubham": 90,
    "Amit": 95,
    0: "Rohan",
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# print(marks.get("Rohan"))
# print(marks.get("Shuhel" )) #Prints None
# print(marks.get["Rohan1"])  #Returns an error
# marks.update({"Rohan": 99,"Rahul": 100})
# print(marks)
# marks.pop("Key","Default_Value")
# print(marks)
# dict.clear(marks)
# print(marks)
# dict.copy(marks)
# print(marks)
# marks.popitem()
# print(marks)
# marks.setdefault("Rohan", 100)
# print(marks)
# marks.setdefault("Rohan", 1000)
# print(marks)
new_dict = dict.fromkeys(marks,0)
print(new_dict)

# Write a python program using function to convert Celsius to Fahrenheit.
# The formula for conversion is: F = C * (9/5) + 32

#def celsius_to_fahrenheit(celsius):
def f_to_c(f):
    return 5*(f-32)/9
    #return celsius * (9/5) + 32
#f = int(input("Enter temperature in Celsius: "))
f = int(input("Enter temperature in F:"))
c = f_to_c(f)
print(f"{round(c,2)}  °C")
#print(f"{f} Celsius is equal to {celsius_to_fahrenheit(f)} Fahrenheit")

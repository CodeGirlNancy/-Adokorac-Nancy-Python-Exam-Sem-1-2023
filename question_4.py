#Write a Python program that prints the following pattern;
#1
#12
#123
#1234
#12345
#Soln
rows = 5  # Define the number of rows for the pattern

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


#Writing a recursive function to calculate the factorialof a given number n.
#Test the function with n=5.
#Soln
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Testing the function with n = 5
n = 5
result = factorial(n)
print(f"The factorial of {n} is: {result}")


#Writing a python function that takes two parameters (a and b) and returns their sum.
#Test the function with values a=3 and b=4.
#Soln
def sum_values(a, b):
    return a + b

# Testing the function with values a = 3 and b = 4
a = 3
b = 4
result = sum_values(a, b)
print(f"The sum of {a} and {b} is: {result}")

#Defining a python class named "Car" with attributes: brand and year.
#Providing a method in the class to display information about the car.
#Soln
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")

# Creating an instance of the Car class
car_instance = Car("BMW", 2020)

# Displaying information about the car using the method
car_instance.display_info()


#Creating an instance of the class and display the information.
#Soln
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")

# Creating an instance of the Car class
car_instance = Car("FERRARI", 2023)

# Displaying information about the car using the method
car_instance.display_info()
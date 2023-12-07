#writing a pytgon program named calculate_area that takes
#the radius of a circle as a parameter and returns the area of the circle.
#Use the formula: area = π*r^2.(Assume π=3.14).
#Test the function with a radius of 5.
#Soln
def calculate_area(radius):
    p = 3.14
    area = p * radius**2
    return area

# Testing the function with a radius of 5
radius = 5
result = calculate_area(radius)
print(f"The area of a circle with radius {radius} is: {result}")
#Write a recursive function to calculate the sum of natural numbers up to n.
#test the function with n=4
#Soln
def sum_of_naturals(n):
    if n <= 1:
        return n
    else:
        return n + sum_of_naturals(n - 1)

# Testing the function with n = 4
n = 4
result = sum_of_naturals(n)
print(f"The sum of natural numbers up to {n} is: {result}")

#Given the list below, remove the element at index 2 and insert the value 10at the end.
#numbers= [1,3,5,7,9]
#Soln
numbers = [1, 3, 5, 7, 9]

# Remove the element at index 2
del numbers[2]

# Insert the value 10 at the end
numbers.append(10)

print(numbers)

#Using list comprehension,create a new list that contains only the even numbers from the original list.
#even_numbers=[2,4,6,8,10]
#Soln
even_numbers = [2, 4, 6, 8, 10]

# List comprehension to extract even numbers
new_list = [num for num in even_numbers if num % 2 == 0]

print(new_list)


#Given the dictionary below,update the value of 'age' to 25 and
#add a new key-value pair ('city','New York').
#student_info={'name':'Alice','age',:20,'grade':'A'}
#Soln
student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}

# Update the value of 'age' to 25
student_info['age'] = 25

# Add a new key-value pair ('city', 'New York')
student_info['city'] = 'New York'

print(student_info)

#Using dictionary comprehension,create a new dictionary with only key_value pairs
#where the value is greater than 5. oringinal_dict={'a':3,'b':8,'c':2,'d':7}
#Son
original_dict = {'a': 3, 'b': 8, 'c': 2, 'd': 7}

# Dictionary comprehension to filter key-value pairs
new_dict = {key: value for key, value in original_dict.items() if value > 5}

print(new_dict)
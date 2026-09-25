# Small practice examples for Module 2 concepts

numbers = [1, 2, 3, 4, 5, 6]

# Lambda function
square = lambda x: x * x
print("Square of 5:", square(5))

# List comprehension
even_numbers = [number for number in numbers if number % 2 == 0]
squares = [number * number for number in numbers]

print("Even numbers:", even_numbers)
print("Squares:", squares)

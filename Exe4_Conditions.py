# 4.) Conditions

# 1. Check whether a number is positive, negative, or zero.

num = float(input("Enter a number: "))

if num > 0:
    print("The number is POSITIVE.")
elif num < 0:
    print("The number is NEGATIVE.")
else:
    print("The number is ZERO.")

# 2. Check whether a person is eligible to vote.

age = int(input("\nEnter your age: "))

if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote yet.")

# 3. Find the largest of three numbers.

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("The largest number is:", largest)


# 4. Check whether a year is a leap year.

import calendar

user_input = input("\nEnter a year: ")

if user_input.isdigit():
    year = int(user_input)
    
    if calendar.isleap(year):
        print(f"\n{year} is a leap year.")
    else:
        print(f"\n{year} is not a leap year.")
else:
    print("Please enter a valid number only!")

# 5. Create a grade system based on marks.

user_input = input("\nEnter your marks (0 to 100): ")

if user_input.isdigit():
    marks = int(user_input)
    
    if 0 <= marks <= 100:
        # Grading Logic
        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        elif marks >= 35:
            grade = "E"
        else:
            grade = "F (Fail)"
            
        print(f"\nMarks: {marks} | Grade: {grade}")
    else:
        print("Out of range! Please enter marks between 0 and 100.")
else:
    print("Please enter a valid number only!")

# 6. Check whether a number is divisible by 5 and 11.

user_input = input("\nEnter a number: ")

if user_input.isdigit():
    number = int(user_input)
    
    if number % 5 == 0 and number % 11 == 0:
        print(f"{number} is divisible by both 5 and 11.")
    else:
        print(f"{number} is not divisible by both 5 and 11.")
else:
    print("Please enter a valid number only!")

# 7. Create a simple calculator using if-elif-else.

num1 = float(input("\nEnter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    print(f"Result: {num1 + num2}")
elif operator == '-':
    print(f"Result: {num1 - num2}")
elif operator == '*':
    print(f"Result: {num1 * num2}")
elif operator == '/':
    
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        print(f"Result: {num1 / num2}")
else:
    print("Invalid operator!")





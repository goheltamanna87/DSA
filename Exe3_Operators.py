# 3.) Operators

# 1. Perform addition, subtraction, multiplication, and division.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (Cannot divide by zero)"

print(f"\n--- Results for {num1} and {num2} ---")
print(f"Addition (+):       {addition}")
print(f"Subtraction (-):    {subtraction}")
print(f"Multiplication (*): {multiplication}")
print(f"Division (/):       {division}")

# 2. Find the remainder and quotient of two numbers.

num1 = int(input("\nEnter the dividend (first number): "))
num2 = int(input("Enter the divisor (second number): "))

if num2 != 0:
    quotient = num1 // num2
    remainder = num1 % num2

    print(f"\n--- Results ---")
    print(f"Quotient :  {quotient}")
    print(f"Remainder: {remainder}")
else:
    print("\nError: Cannot divide by zero!")

# 3. Check whether a number is even or odd.

num = int(input("\nEnter a number to check odd or even: "))

if num % 2 == 0:
    print(f"\n{num} is an EVEN number.")
else:
    print(f"\n{num} is an ODD number.")

# 4. Compare two numbers using relational operators.

num1 = float(input("\nEnter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"\n--- Comparison Results for {num1} and {num2} ---")

if num1 == num2:
    print(f"Both numbers are equal ({num1} == {num2})")
else:
    print(f"Numbers are not equal ({num1} != {num2})")
    
    if num1 > num2:
        print(f"First number is greater than the second ({num1} > {num2})")
    else:
        print(f"First number is less than the second ({num1} < {num2})")

print(f"Greater than or equal to (>=): {num1 >= num2}")
print(f"Less than or equal to (<=):    {num1 <= num2}")


# 5. Demonstrate logical operators (and, or, not).

x = eval(input("\nEnter True or False for X: "))
y = eval(input("Enter True or False for Y: "))

print("\n--- Results ---")

print("X and Y is:", x and y)
print("X or Y is :", x or y)
print("not X is   :", not x)

# 6. Demonstrate assignment operators (+=, -=, *=, /=).

x = 10
print("\nStart: ", x)

x += 5
print("After +=" , x)

x -= 3
print("After -=" , x)

x *= 2
print("After *=" , x)

x /= 4
print("After /=" , x)

# 7. Find the largest of two numbers using comparison operators.

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- comparison operators Results ---")
if num1 > num2:
    print("The largest number is:", num1)

if num2 > num1:
    print("The largest number is:", num2)

if num1 == num2:
    print("Both numbers are equal.")
    

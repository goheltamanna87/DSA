# 5.) Loops

# 1. Print numbers from 1 to 10 using a for loop.

print("--- Numbers 1 to 10 ---")
for i in range(1, 11):
    print(i)

# 2. Print numbers from 10 to 1 using a while loop.

print("\n--- Numbers 10 to 1 ---")
i = 10
while i > 0:
    print(i)
    i = i - 1

# 3. Print the multiplication table of a number.

print("\n--- Multiplication Table ---")
num = int(input("Enter a number to generate its table: "))

print(f"\nMultiplication Table of {num}:")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 4. Find the sum of numbers from 1 to n.

print("\n--- Sum of Numbers (1 to n) ---")
n = int(input("Enter the value of 'n' to calculate sum: "))
total_sum = 0

for i in range(1, n + 1):
    total_sum = total_sum + i

print("The sum of numbers from 1 to", n, "is:", total_sum)

# 5. Find the factorial of a number.

print("\n--- Factorial Calculator ---")
import math

num = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {num} is:", math.factorial(num))

# 6. Print all even numbers between 1 and 100.

print("\n--- Even Numbers between 1 and 100 ---")
for i in range(2, 101, 2):
    print(i, end=" ")
print()

# 7. Reverse a number using a loop.
print("\n--- Number Reversal ---")
num = int(input("Enter a number to reverse: "))
temp = num
reverse = 0

while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10

print(f"The reverse of {num} is:", reverse)


# 8. Count the digits of a number.
print("\n--- Digit Counter ---")
num = int(input("Enter a number to count its digits: "))
temp = abs(num)
count = 0

if temp == 0:
    count = 1
else:
    while temp > 0:
        count = count + 1
        temp = temp // 10

print(f"Total number of digits in {num} is:", count)


# 9. Check whether a number is prime.
print("\n--- Prime Number Checker ---")
num = int(input("Enter a number to check if it's prime: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"Yes, {num} is a Prime Number.")
else:
    print(f"No, {num} is NOT a Prime Number.")


# 10. Print Fibonacci series up to n terms.
print("\n--- Fibonacci Series Generator ---")
n = int(input("Enter how many terms (n) you want: "))

n1, n2 = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer greater than 0.")
elif n == 1:
    print(f"Fibonacci series up to {n} term:")
    print(n1)
else:
    print(f"Fibonacci series up to {n} terms:")
    while count < n:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count = count + 1
    print()

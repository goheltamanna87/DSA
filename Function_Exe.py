# 1. Write a function to print "Hello, World!".
def hello():
    print("Hello, World!")
hello()


# 2. Write a function that takes a name and prints a greeting.
def greeting(name):
    print(f"Hello, {name}!")
greeting("abc")


# 3. Write a function to add two numbers.
def add_number(a, b):
    return a + b

res = add_number(10, 20)
print(f"Addition result: {res}")


# 4. Write a function to find the square of a number.
def square_number(num):
    return num ** 2

res = square_number(4)
print(f"Square result: {res}")


# 5. Write a function to check whether a number is even or odd.
def odd_even(num):
    return "Even" if num % 2 == 0 else "Odd"

result = odd_even(4)
print(f"The number is: {result}")


# 6. Write a function to find the maximum of two numbers.
def max_of_two(a, b):
    return max(a, b)

max_num = max_of_two(40, 20)
print(f"Maximum number is: {max_num}")

# 7. Write a function to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

fahrenheit = celsius_to_fahrenheit(25)
print(f"25°C in Fahrenheit is: {fahrenheit}°F")

# 8. Write a function to calculate the area of a circle.

import math

def circle_area(radius):
    return math.pi * (radius ** 2)

area = circle_area(5)
print(f"Area of circle with radius 5: {area:.2f}")

# 9. Write a function to calculate the factorial of a number.
def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"Factorial of 5 is: {factorial(5)}")

#10. Write a function to check whether a number is positive, negative, or zero.
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    return "Zero"

print(f"Number -7 is: {check_number(-7)}")

#11. Write a function to find the maximum of three numbers.

def max_of_three(a, b, c):
    return max(a, b, c)

max_num = max_of_three(10, 45, 23)
print(f"Maximum of three numbers is: {max_num}")

#12. Write a function to count vowels in a string.

def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    
    for char in s:
        if char in vowels:
            count = count + 1
            
    return count

vowel_count = count_vowels("Hello World")
print(f"Vowel count: {vowel_count}")

#13. Write a function to reverse a string.
def reverse_string(s):
    return s[::-1]

reversed_str = reverse_string("Python")
print(f"Reversed string: {reversed_str}")

#14. Write a function to check whether a string is a palindrome.

def is_palindrome(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
        
    if s == reversed_s:
        return True
    else:
        return False

print(f"Is 'radar' a palindrome?: {is_palindrome('radar')}")

#15. Write a function to find the sum of all elements in a list.

def sum_of_list(lst):
    return sum(lst)

total_sum = sum_of_list([1, 2, 3, 4, 5])
print(f"Sum of list elements: {total_sum}")

#16. Write a function to find the largest element in a list.

def largest_element(lst):
    return max(lst) if lst else None

largest = largest_element([12, 67, 34, 89, 54])
print(f"Largest element is: {largest}")

#17. Write a function to remove duplicate elements from a list.

def remove_duplicates(lst):
    return list(set(lst))

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(f"List after removing duplicates: {result}")

#18. Write a function to count how many times an element appears in a list.

def count_occurrence(lst, element):
    return lst.count(element)

count = count_occurrence([1, 4, 2, 4, 3, 4, 5], 4)
print(f"Element 4 appears: {count} times")

#19. Write a function to check whether a number is prime.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Is 17 prime?: {is_prime(17)}")

#20. Write a function to return all prime numbers between two numbers.

def primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

prime_list = primes_in_range(10, 30)
print(f"Prime numbers between 10 and 30: {prime_list}")


#21. Write a function to calculate Fibonacci numbers.

def fibonacci(n):
    sequence = []
    a = 0
    b = 1
    
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
        
    return sequence

print(f"First 7 Fibonacci numbers: {fibonacci(7)}")

#22. Write a function to find the second-largest number in a list.

def second_largest(lst):
    unique_nums = list(set(lst))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[-2]

sec_largest = second_largest([10, 45, 46, 23, 9, 34])
print(f"Second largest number is: {sec_largest}")

#23. Write a function to sort a list without using sort().

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print("Sorted list:", sorted_numbers)

#24. Write a function to merge two lists and remove duplicates.

def merge_and_remove_duplicates(list1, list2):
    return list(set(list1 + list2))

merged_res = merge_and_remove_duplicates([1, 2, 3], [3, 4, 5])
print(f"Merged unique list: {merged_res}")









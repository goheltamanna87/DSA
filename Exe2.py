# 2.) Data Types

# 1. Demonstrate int, float, str, bool, and complex.

my_int = 42
print(f"Value: {my_int}, Type: {type(my_int)}")

my_float = 3.14
print(f"Value: {my_float}, Type: {type(my_float)}")

my_str = "Hello, Python!"
print(f"Value: '{my_str}', Type: {type(my_str)}")

my_bool = True
print(f"Value: {my_bool}, Type: {type(my_bool)}")

my_complex = 2 + 3j
print(f"Value: {my_complex}, Type: {type(my_complex)}")

# 2. Accept two numbers and display their data types.

num1 = eval(input("\nEnter the first number: "))
num2 = eval(input("Enter the second number: "))

print(f"\nThe data type of {num1} is: {type(num1).__name__}")
print(f"The data type of {num2} is: {type(num2).__name__}")

# 3. Convert a string number into an integer and float.

string_num = "42"

integer_version = int(string_num)
float_version = float(string_num)

print(f"\nInteger value: {integer_version} | Type: {type(integer_version).__name__}")
print(f"Float value: {float_version} | Type: {type(float_version).__name__}")

# 4.Find the length of a string.

text = input("\nEnter String values: ")
print("\n String length of: ",len(text))

# 5.Create a list, tuple, set, and dictionary and display their types.

my_list = ["apple", "banana", "cherry"]
my_tuple = ("apple", "banana", "cherry")
my_set = {"apple", "banana", "cherry"}
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

print("\n",type(my_list)) 
print(type(my_tuple)) 
print(type(my_set))
print(type(my_dict))


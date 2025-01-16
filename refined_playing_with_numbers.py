# Function to perform arithmetic operations and display results
def arithmetic_operations(a, b):
    print(f"Values: a = {a}, b = {b}")
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b if b != 0 else "Undefined (division by zero)")
    print("Floor Division:", a // b if b != 0 else "Undefined (division by zero)")
    print("Modulus:", a % b if b != 0 else "Undefined (modulus by zero)")
    print()

# Integer cases
print("CASE 1: Both Positive")
arithmetic_operations(50, 33)

print("CASE 2: Both Negative")
arithmetic_operations(-22, -10)

print("CASE 3: Positive a, Negative b")
arithmetic_operations(29, -20)

print("CASE 4: Negative a, Positive b")
arithmetic_operations(-29, 20)

# Float cases
print("FLOAT CASES")

print("CASE 1: Both Positive Floats")
arithmetic_operations(5.3, 3.3)

print("CASE 2: Both Negative Floats")
arithmetic_operations(-5.3, -8.7)

print("CASE 3: Positive a, Negative b (Float)")
arithmetic_operations(12, -3.3)

# Using round function
a = 12
b = -3.3
print("Using round function for division result:")
print("Division rounded:", round(a / b, 2))

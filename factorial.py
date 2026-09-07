# ============================================================
# Q2. ONE-SHOT PROMPTING - FACTORIAL CALCULATION
# ============================================================

# Question:
# Write a one-shot prompt by providing one input-output example
# and ask the AI to generate a Python function to compute
# the factorial of a given number.

# Example:
# Input: 5
# Output: 120

# Prompt:
# Write a Python function to calculate the factorial of a given
# non-negative integer.
#
# Example:
# Input: 5 -> Output: 120
#
# Handle invalid negative inputs appropriately.


# Python Code:

def factorial(n):
    if n < 0:
        return "Invalid Input"

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


n = int(input("Enter a number: "))
print(factorial(n))


# ============================================================
# Question -> Input -> Output
# ============================================================

# Question: Find the factorial of the given number.
# Input: 5
# Output: 120

# Question: Find the factorial of the given number.
# Input: 0
# Output: 1

# Question: Find the factorial of the given number.
# Input: -4
# Output: Invalid Input
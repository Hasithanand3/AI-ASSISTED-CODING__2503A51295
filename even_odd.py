# ============================================================
# Q6. FEW-SHOT PROMPTING - EVEN OR ODD WITH VALIDATION
# ============================================================

# Question:
# Write a few-shot prompt by providing multiple input-output
# examples to guide the AI to generate a Python program that
# determines whether a given number is even or odd, including
# proper input validation.

# Examples:
# Input: 8 -> Output: Even
# Input: 15 -> Output: Odd
# Input: 0 -> Output: Even

# Prompt:
# Write a Python program that determines whether an integer
# is Even or Odd.
#
# Use these examples:
# 8 -> Even
# 15 -> Odd
# 0 -> Even
#
# The program must validate that the input is an integer
# and handle negative integers correctly.


# Python Code:

def even_or_odd(n):
    if n % 2 == 0:
        return "Even"

    return "Odd"


try:
    n = int(input("Enter an integer: "))
    print(even_or_odd(n))

except ValueError:
    print("Invalid Input")


# ============================================================
# Question -> Input -> Output
# ============================================================

# Question: Determine whether the given number is even or odd.
# Input: 8
# Output: Even

# Question: Determine whether the given number is even or odd.
# Input: 15
# Output: Odd

# Question: Determine whether the given number is even or odd.
# Input: 0
# Output: Even

# Question: Determine whether the given number is even or odd.
# Input: -6
# Output: Even

# Question: Determine whether the given number is even or odd.
# Input: -7
# Output: Odd

# Question: Determine whether the given number is even or odd.
# Input: abc
# Output: Invalid Input
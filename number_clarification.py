# ============================================================
# Q4. CONTEXT-MANAGED PROMPTING
# PRIME, COMPOSITE OR NEITHER
# ============================================================

# Question:
# Design a context-managed prompt with clear instructions
# and constraints to generate an optimized Python program
# that classifies a number as prime, composite, or neither.

# Prompt:
# Write an optimized Python program that classifies an integer
# as Prime, Composite, or Neither.
#
# Requirements:
# 1. Numbers less than 2 must be classified as Neither.
# 2. Check divisibility only up to the square root of the number.
# 3. Validate that the input is an integer.
# 4. Clearly display the result as Prime, Composite, or Neither.


# Python Code:

def classify_number(n):
    if n < 2:
        return "Neither"

    i = 2

    while i * i <= n:
        if n % i == 0:
            return "Composite"

        i += 1

    return "Prime"


try:
    n = int(input("Enter an integer: "))
    print(classify_number(n))

except ValueError:
    print("Invalid Input")


# ============================================================
# Question -> Input -> Output
# ============================================================

# Question: Classify the given number as Prime, Composite,
# or Neither.
# Input: 7
# Output: Prime

# Question: Classify the given number as Prime, Composite,
# or Neither.
# Input: 12
# Output: Composite

# Question: Classify the given number as Prime, Composite,
# or Neither.
# Input: 1
# Output: Neither

# Question: Classify the given number as Prime, Composite,
# or Neither.
# Input: -5
# Output: Neither

# Question: Classify the given number as Prime, Composite,
# or Neither.
# Input: abc
# Output: Invalid Input
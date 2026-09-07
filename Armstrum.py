# ============================================================
# Q3. FEW-SHOT PROMPTING - ARMSTRONG NUMBER
# ============================================================

# Question:
# Write a few-shot prompt by providing multiple input-output
# examples to guide the AI in generating a Python function
# to check whether a given number is an Armstrong number.

# Examples:
# Input: 153 -> Output: Armstrong Number
# Input: 370 -> Output: Armstrong Number
# Input: 123 -> Output: Not an Armstrong Number

# Prompt:
# Write a Python function to check whether a number is an
# Armstrong number.
#
# Use these examples to understand the expected output:
# 153 -> Armstrong Number
# 370 -> Armstrong Number
# 123 -> Not an Armstrong Number
#
# Handle zero and negative numbers appropriately.


# Python Code:

def armstrong(n):
    if n < 0:
        return "Not an Armstrong Number"

    digits = str(n)
    power = len(digits)

    total = sum(int(digit) ** power for digit in digits)

    if total == n:
        return "Armstrong Number"

    return "Not an Armstrong Number"


n = int(input("Enter a number: "))
print(armstrong(n))


# ============================================================
# Question -> Input -> Output
# ============================================================

# Question: Check whether the given number is an Armstrong number.
# Input: 153
# Output: Armstrong Number

# Question: Check whether the given number is an Armstrong number.
# Input: 370
# Output: Armstrong Number

# Question: Check whether the given number is an Armstrong number.
# Input: 123
# Output: Not an Armstrong Number

# Question: Check whether the given number is an Armstrong number.
# Input: 0
# Output: Armstrong Number

# Question: Check whether the given number is an Armstrong number.
# Input: -153
# Output: Not an Armstrong Number
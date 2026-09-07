# ============================================================
# Q1. ZERO-SHOT PROMPTING - PALINDROME NUMBER
# ============================================================

# Question:
# Write a zero-shot prompt to generate a Python function that
# checks whether a given number is a palindrome.

# Prompt:
# Write a Python function that checks whether a given number
# is a palindrome. Return "Palindrome" if the number reads
# the same forward and backward, otherwise return
# "Not a Palindrome".


# Python Code:

def palindrome(n):
    if n < 0:
        return "Not a Palindrome"

    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    if original == reverse:
        return "Palindrome"

    return "Not a Palindrome"


n = int(input("Enter a number: "))
print(palindrome(n))


# ============================================================
# Question -> Input -> Output
# ============================================================

# Question: Check whether the given number is a palindrome.
# Input: 121
# Output: Palindrome

# Question: Check whether the given number is a palindrome.
# Input: 123
# Output: Not a Palindrome

# Question: Check whether the given number is a palindrome.
# Input: -121
# Output: Not a Palindrome
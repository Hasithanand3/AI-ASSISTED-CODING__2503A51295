# ============================================================
# Q5. ZERO-SHOT PROMPTING - PERFECT NUMBER
# ============================================================

# Question:
# Write a zero-shot prompt without providing any examples
# to generate a Python function that checks whether a number
# is a perfect number.

# Prompt:
# Write a Python function that checks whether a given positive
# integer is a perfect number.
#
# A perfect number is equal to the sum of its proper positive
# divisors.
#
# Return "Perfect Number" or "Not a Perfect Number".


# Python Code:

def perfect_number(n):
    if n <= 1:
        return "Not a Perfect Number"

    total = 1

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            total += i

            if i != n // i:
                total += n // i

    if total == n:
        return "Perfect Number"

    return "Not a Perfect Number"


n = int(input("Enter a number: "))
print(perfect_number(n))


# ============================================================
# Question -> Input -> Output
# ============================================================

# Question: Check whether the given number is a perfect number.
# Input: 6
# Output: Perfect Number

# Question: Check whether the given number is a perfect number.
# Input: 28
# Output: Perfect Number

# Question: Check whether the given number is a perfect number.
# Input: 12
# Output: Not a Perfect Number

# Question: Check whether the given number is a perfect number.
# Input: 1
# Output: Not a Perfect Number
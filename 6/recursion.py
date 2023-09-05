""" Recursion error
def error_function(i = 0):
    print(i)
    return error_function(i + 1)

try:
    error_function()
except RecursionError as e:
    print(e)
"""


def integral(n):
    if n < 0:
        raise ValueError("N must be bigger that 0")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    return integral(n - 1) * n

print(integral(5))
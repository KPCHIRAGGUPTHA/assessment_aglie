def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


number = 5

print("Factorial of", number, "=", factorial(number))
print("Factorial of 0 =", factorial(0))

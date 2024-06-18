#Write a python program that calculates the factorial of a given number.


n=int(input("Enter no."))
def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(n))
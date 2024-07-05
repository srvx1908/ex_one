import math
n=int(input("Enter your number-->"))
def factorial(num):
    if num>0:
        print("factorial of", num,"=",math.factorial(num))
    else:
        print("given number is negative")
factorial(n)
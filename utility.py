import math
def factorial():
    number = int(input("Enter a number:"))
    result = math.factorial(number)
    print("Factorial of", number, "is: ", result)
def squareroot():
    number = float(input("Enter a number"))
    result = math.sqrt(number)
    print("Squareroot of", number, "is", result)
def prime():
    n = int(input("Enter a number"))
    if n <= 1:
        return  (n, "is not a Prime number")   
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return (n, "is not a Prime number")        
    return (n, "is a Prime number")

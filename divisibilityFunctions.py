def tableOfPrimeAndComposites(n: int):
    """Gives a Table of numbers that are prime or composite from 1 to n"""

    print("Prime      Composite")
    print("____________________")
    
    i = 2
    for i in range(i, n+1):
        j = 2
        while (j*j <= i):
            if ((i % j) == 0):
                break
            j += 1
        if (j * j > i):
            print(i)
        else:
            print(f"\t\t{i}")



def eucledianAlgorithmExplained(a: int, b: int):
    """Explains the Eucledian Algorithm between two integers a and b step by step"""

    aInitial = a
    bInitial = b

    while b > 0:
        r = a % b
        q = a//b

        print(f"{a :>5} = {b :>5} * {q :>5} + {r :>5}")

        a = b
        b = r
    
    print(f"The greatest common factor of {aInitial} and {bInitial} is {a}")



def gcd(a: int, b: int):
        """Greatest Common Divisor of two integers a and b"""
        while b > 0:
            r = a % b
            a = b
            b = r

        return a

def lcm(a: int, b: int):
    """Least Common Multiple of two integers a and b"""
    return int(a * (b/(gcd(a, b))))



# Applications of these functions
# ---------- Fraction Calculator ----------
#
# We know that multiplying and dividing fractions are pretty straight forward.
# However, we now know that addind and subtracting fractions requires the denomimator to be a common form for both fractions.
# As such, the lcm can help us determine a common number for both denomimators and do calculators for the numerators and final result.

def fractionOperation(x, y, a, b, operation):
    d = lcm(y, b)

    if operation == "+":
        # x/y + a/b = n/d
        n = int(((d/y)*x) + ((d/b)*a))

        print(f"{x}/{y} + {a}/{b} = {n}/{d}")

    elif operation == "-":
        # x/y - a/b = n/d
        n = int(((d/y)*x) - ((d/b)*a))

        print(f"{x}/{y} - {a}/{b} = {n}/{d}")

    elif operation == "*":
        # x/y * a/b = x*a/y*b
        print(f"{x}/{y} * {a}/{b} = {x*a}/{y*b}")
    
    elif operation == "/":
        # x/y / a/b = x*b/y*a
        print(f"{x}/{y} / {a}/{b} = {x*b}/{y*a}")












# A Table of all possible combiantions of two numbers and the GCD

# def gcdTable(n: int):
#     print("     Num 1        Num 2        GCD")
#     print("----------------------------------")

#     for i in range(1, n):
#         for j in range(1, n):
#             print(f"   {i:>4}           {j:>4}        {gcd(i, j):>4}")

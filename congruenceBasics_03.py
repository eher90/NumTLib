# Table of Congruence Addition and Multiplication
# (Note: Prototype version only handle up to n = 10)

from divisibilityFunctions_01 import gcd

def additionCongruenceTable(n: int):
    print(f"Addition Table in Mod {n}")

    header = ""
    for i in range(n):
        header += f"___{i}"
    
    print(header)

    for j in range(n):
        rows = ""
        for k in range(n):
            l = (j+k) % n
            rows += f" {l}  "
        print(f"{j}|{rows}")

def multiplicationCongruenceTable(n: int):
    print(f"Multiplication Table in Mod {n}")

    header = ""
    for i in range(n):
        header += f"___{i}"
    
    print(header)

    for j in range(n):
        rows = ""
        for k in range(n):
            l = (j*k) % n
            rows += f" {l}  "
        print(f"{j}|{rows}")


# The Reduced Residue Class is all the elements in the modulus n such that the gcd(a, n) = 1
# This is important as Euler Phi (n) = # Elements in Reduced Residue Class
        
def reducedResidueClass(n: int):
    elements = []
    for i in range(n):
        if gcd(i, n) == 1:
            elements.append(i)
    
    return elements


# Since we are in congruences, there are basic properties of congruences that is important to know. Mostly modular arithmetic.
# - Modular Addition:
#       * a + b mod(n) = a mod(n) + b mod(n)
#       * c(a+b) mod(n) = ac mod(n) + bc mod(n)
#
# - Modular Subtraction:
#       * a-b mod(n) = a mod(n) - b mod(n)
#       * c(a-b) mod(n) = ac mod(n) - bc mod(n)
#
# - Modular Multiplication:
#       * a*b mod(n) = a mod(n) * b mod(n)
#       * k(ab) mod(n) = ka mod(n) * kb mod(n)

# In programs such as C++ or C, there would be an issue of overflow getting the wrong answer for large amounts of numbers.
# In Python, the issue is resolved and as such, the calculations can be done under the hood.



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
#

# We can do modular exponeniation as well. 
def mod_exp(base: int, exponent: int, modulus: int):

    # Check if exponent is 0 as n**0 = 1
    if exponent == 0:
        return 1

    result = 1
    base = base % modulus # Check if base >= modulus for overcounting

    while exponent > 0: 
        if exponent % 2 == 1: # Accounting the number of times of base ^ 1
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus

    return result




# This is extremely useful as we can find the order of a congruence class [n] if
# - a^n === b mod(m) satisfies gcd(a, m) = 1
# - Order of a is the smallest possible integer n such that a^n === 1 

# Ex: Order of 5 in congruence class 9 is 6 as 5^6 === 1 mod 9

# We can do his by using the mod_exp and gcd()


def orderOfEachElementInClass(n: int):
    orders = {}

    for i in range(1, n):
        if gcd(i, n) == 1:
            for j in range(1, n):
                if mod_exp(i, j, n) == 1:
                    orders[i] = j
                    break
    
    return orders # In form of a: b where a is element of element class and b is a^b === 1 mod n


# We can also find the primitive root. This is when the order of an element of congruence class = phi(n)

# Another interesting thing is that there are exactly phi(phi(n)) primitive roots mod n.





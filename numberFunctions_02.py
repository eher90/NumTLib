from divisibilityFunctions_01 import gcd

# Euler Phi Function is a funciton that counts the number of elements in Zx n. 
# Or mostly the number of positive integers less than an integer n that is coprime to n.
# One method would be to iteratively count from 1 to n and determine if the gcd(a, n) = 1.

def naiveEulerPhiFunction(n: int):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    
    return count

# We can do better than that. We can use trial division to get a list of factors that divides n.
# Basically, the method is that we know any factor is less than or equal to the square root of an integer n. 
# We only check until from 1 to sqrt(n).

# For this example, (and later, this is the prime factorization). You can reuse this code to find all factors but this
# method will be useful for other number functions.

def trialDivision(n: int):
    x = n
    primeFactorization = []

    # All even factors (2 * 2 * ...):
    while (n % 2 == 0):
        n = int(n/2)
        primeFactorization.append(2)
    
    # n would either be itself or changed as a factor of that even number
    # This means n needs to be factored as well just in case we msis any prime factors
    
    for i in range(3, n + 2):
        while n % i == 0:
            primeFactorization.append(i)
            n /= i
    

    return primeFactorization


# Now why did we return a list for the trial division? 
# We have a list of prime factors that is easily computable and a property of Eulper Phi Function is that
# 
# phi(p) = p-1 and
# phi(p^n) = (p^n-1) * (p-1)
#
# So this means we just multiply all the primes in the array to minus one of all of them. 
# Ex: Phi(280) = [2, 2, 2, 5, 7] => 1 * 1 * 1 * 4 * 6 = 24

def eulerPhi(n: int):
    nums = trialDivision(n)
    placeholder = 1

    # This takes all the values and stores it into a hashset based on how many of each number in there
    # Iterate through the hashset and follow the guide for Phi(n) and you should end up with the correct number

    values = {}

    for i in nums:
        if i not in values:
            values[i] = 0
        values[i] += 1
    
    for key, value in values.items():
        if value > 1:
            placeholder = placeholder * (key ** (value - 1)) * (key - 1)
        else:
            placeholder *= (key - 1)
    
    return placeholder







def tableOfPrimeAndComposites(n: int):
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
    aInitial = a
    bInitial = b

    while b > 0:
        r = a % b
        q = a//b

        print(f"{a :>5} = {b :>5} * {q :>5} + {r :>5}")

        a = b
        b = r
    
    print(f"The greatest common factor of {aInitial} and {bInitial} is {a}")

def eucledianAlgorithm(a: int, b: int):
        while b > 0:
            r = a % b
            a = b
            b = r

        return a


eucledianAlgorithmExplained(5797, 13020)
print(eucledianAlgorithm(5797, 13020))
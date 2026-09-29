def checkprime(prime):
    if prime < 2:
        return False

    for divisor in range(2, int(prime ** 0.5) + 1):
        if prime % divisor == 0:
            return False

    return True


prime = int(input("Enter a whole number: "))
if checkprime(prime):
    print("This is a prime number")
else:
    print("This is not a prime number")
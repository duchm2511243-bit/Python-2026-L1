def isperfectN(n):
    if n <= 1:
        return False

    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n


num = int(input("Enter a number: "))
if isperfectN(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
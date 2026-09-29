def pydivisorNum(n):
    divisors = [i for i in range(1, abs(n) + 1) if n % i == 0]
    return divisors


num = 12
result = pydivisorNum(num)

print(f"Divisors is {num}: ", result)
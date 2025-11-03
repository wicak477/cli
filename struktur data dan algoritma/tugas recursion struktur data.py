def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = 8
hasil = factorial(n)
print(f"{n}! = {hasil}")

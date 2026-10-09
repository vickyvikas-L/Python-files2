def perfect_number(n):
    total = 0

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i

    if total == n:
        print(f"{n} is a Perfect Number")
    else:
        print(f"{n} is Not a Perfect Number")


num = int(input("Enter a number: "))
perfect_number(num)
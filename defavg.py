def average_digits(n):
    total = 0
    count = 0

    while n > 0:
        digit = n % 10
        total += digit
        count += 1
        n //= 10

    return total / count


num = int(input("Enter a number: "))
avg = average_digits(num)

print("Average of digits =", avg)
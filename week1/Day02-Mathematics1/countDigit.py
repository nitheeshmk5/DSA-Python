def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
        #print(n)
    return count

print(count_digits(1234567))


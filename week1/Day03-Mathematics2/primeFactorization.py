def prime(n):
    if n == 1:
        return False
    if n == 3 or n == 2:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while(i*i <= n):
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True


def prime_fac(n):
    for i in range(2,n+1):
        if prime(i):
            x = i
            while n % x == 0:
                print(i , end=" ")
                x = x * i

n = 100
prime_fac(n)
            
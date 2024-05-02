#Naive approach
#O(n)

def prime_naive(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

n = 20
if prime_naive(n):
    print("It is prime number")
else:
    print("It is not a prime number")


#Efficient
#O(sqrt(n))

def prime_sq(n):
    if n == 1:
        return False
    if n == 2:
        return True
    i = 3
    while (i * i <= n):
        if n % i == 0:
            return False
        i += 1
    return True


#Super Efficient

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
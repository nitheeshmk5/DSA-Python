'''
Given a positive integer value N. The task is to find how many numbers less than or equal to N have numbers of divisors exactly equal to 3.

*Expected Time Complexity : O(N1/2 * N1/4)
'''

'''
it 25 is n
4,9 has exactly 3 divisors
also for 100
4,9,25,49

*clearly that is square of prime numbers
'''

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

def divisor3(n):
    count = 0
    # Iterate over numbers from 1 to sqrt(N)
    for i in range(1,int(n**2)+1):
        if prime(i):
            sq = i * i
            if sq <= n:
                count += 1
    print(count)


divisor3(100)       


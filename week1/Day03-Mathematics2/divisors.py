#Naive
#O(n)
def print_divisors(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end=" ")

#print_divisors(100)


"""
Eg: 30
Divisors always appear in pairs
(1,30),(2,15),(3,10),(5,6) = 30
(x,y) = n
x <= y
x * x = n
x = sqrt(n)
"""

def divisors(n):
    i = 1
    count = 0
    while i * i <= n:
        if n % i == 0:
            print(i)
            count += 1
            if i != n//i:
                print(n//i)
        i += 1

divisors(100)

#iterative way
#O(n) O(1)->space

def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact = fact * i
    print(fact)

def factorial_while(n):
    fact = 1
    while n > 0:
        fact = fact * n
        n -= 1  
    print(fact)

factorial_while(4)
        
#Recursive way
#O(n) theta(n) -> space
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))
        

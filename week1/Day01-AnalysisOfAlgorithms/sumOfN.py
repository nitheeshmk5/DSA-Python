# O(1) (No grow)

def sumOfN(n):
    return n(n+1)/2

# O(n) (Linear grow)

def sumOfN(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

# O(n**2) (Quadratically grow)

def sumOfN(n):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum += j
    
    return sum
        


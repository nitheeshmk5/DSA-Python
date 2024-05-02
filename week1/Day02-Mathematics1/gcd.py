#Euclidean Algorithm HCF

def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

#Optimised Euclidean

def gcd(a,b):  # 12,15
    if b == 0:
        return a
    else:
        return gcd(b, a % b)   # 15,3
    
'''
Modular multiplicative inverse - 
In mathematics, particularly in the area of arithmetic, a modular multiplicative inverse of an integer a is an integer x such that the product ax is congruent to 1 with respect to the modulus m

ax _= 1 (mod m)
'''


def modu(a,m):
    for i in range(1,m):
        if ((a % m) * (i % m)) % m == 1:
            return i
    return -1 

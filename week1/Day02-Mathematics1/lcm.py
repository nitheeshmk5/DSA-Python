def lcm(a,b):
    res = max(a,b)
    while True:
        if res % a == 0 and res % b == 0:
            return res
        else:
            res += 1

print(lcm(12,15))
    
    

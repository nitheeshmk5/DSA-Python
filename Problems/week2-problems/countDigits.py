def countDigits(num):
    temp = num
    if temp == 0:
        return 0 
    else:
        return 1 + countDigits(temp // 10)
        

print(countDigits(999))



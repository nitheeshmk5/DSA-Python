def greaterX(arr,x):
    great = []
    for i in arr:
        if i > x:
            great.append(i)
    return len(great)

print(greaterX([10,20,30,40,50],10))
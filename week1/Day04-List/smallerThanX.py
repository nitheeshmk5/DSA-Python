def smallerX(arr,x):
    small = []
    for i in arr:
        if i < x:
            small.append(i)
    print(small)

smallerX([20,30,25,100],x=31)
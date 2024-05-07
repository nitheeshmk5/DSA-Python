def smallerX(arr,x):
    
    # for i in arr:
    #     if x > i:
    #         small.append(i)
    # print(max(small))

    small = -1  #Default
    for i in arr:
        if i < x and i > small:
            small = i
    return small

smallerX([20,10,19],20)
def countF(arr,n):
    di = dict()
    for i in range(n):
        if arr[i] in di.keys():
            di[arr[i]] += 1
        else:
            di[arr[i]] = 1
    print(di)

countF([1,1,2,2,3,3,4],7)
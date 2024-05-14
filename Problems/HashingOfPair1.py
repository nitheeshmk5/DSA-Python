def sumExist(arr,n,sums):
    li = set()
    for i in arr:
        x = sums - i
        if x in li:
            return 1
        li.add(i)
    return 0

print(sumExist([1, 2, 3],10,14))

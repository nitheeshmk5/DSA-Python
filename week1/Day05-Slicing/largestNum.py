def largerstNum(arr):
    great = arr[0]
    for i in arr:
        if i > great:
            great = i
    return great 
    # return max(arr)


def isSorted(arr):  # *Assending order
    i = 1
    while i < len(arr):
        if arr[i] < arr[i-1]:   # arr[1] < arr[0] 
            return False
        i += 1
    return True

                

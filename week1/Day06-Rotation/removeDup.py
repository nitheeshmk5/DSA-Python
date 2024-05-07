# For sorted array
# Auxilary space O(n)

def removeDup(arr):
    n = len(arr)
    res = 1
    for i in range(1,n): # [1,1,2,2,3]
        if arr[res - 1] != arr[i]:   
            arr[res] = arr[i]  # 1st iter -> [1,2,2,2,3] -> [1,2,3,3,3] -> [1,2,3]
        res += 1
    return arr
    

def removeDuplicates(arr, n):
    if n == 0 or n == 1:
        return n
    j = 0
    for i in range(0, n-1):
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j += 1

    arr[j] = arr[n-1]
    j += 1
    return j

print(removeDup([1,1,1,2,2,3,3,3,3,3]))


#From gpt ->
def removeDup(arr):
    n = len(arr)
    if n == 0:
        return arr 
    res = 0  
    for i in range(1, n):
        if arr[res] != arr[i]:   
            res += 1
            arr[res] = arr[i]
    return arr[:res + 1]


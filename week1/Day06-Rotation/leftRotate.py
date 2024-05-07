'''
l = [10, 20, 30, 40]
l = l[1:] + l[0:1]
print(l)

l = [10, 20, 30, 40]
l.append(l.pop(0))

print(l)
'''

def rotateByOne(arr):
    first = arr[0]
    n = len(arr)

    for i in range(1,n):
        arr[i-1] = arr[i]
    
    arr[n - 1] = first  # to add at last

    return arr

print(rotateByOne([10,20,30,40]))

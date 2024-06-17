# Print elements in an array using recursion

def printElements(arr):
    if len(arr) == 0:
        return
    else:
        print(arr[0])
        printElements(arr[1 : ])


printElements([1,2,3,4,5])
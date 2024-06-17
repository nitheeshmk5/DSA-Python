# Print elements in an array using recursion

def printElements(arr):
    if len(arr) == 0:
        return
    else:
        print(arr[0])              # (1) -> (2) -> so on
        printElements(arr[1 : ])   # (2 3 4 5) -> (3 4 5) -> (4 5) -> (5) -> ()

printElements([1,2,3,4,5])
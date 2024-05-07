'''
Given an array arr[] of size N and two elements x and y, use counter variables to find which element appears most in the array. If both elements have the same frequency, then return the smaller element.
Note:  We need to return the element, not its count
'''

def majority(arr,x,y):
    x_count = 0
    y_count = 0

    for i in arr:
        if i == x:
            x_count += 1
        elif i == y:
            y_count += 1
    
    if x_count < y_count:
        return y
    else:
        return x
    
print(majority([10,10,1,1,1,1,1,1,1,1,1,11,1,1,2,2,2,2,2,2,2,2,2],1,2))

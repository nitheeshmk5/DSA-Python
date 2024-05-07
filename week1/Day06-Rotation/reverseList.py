def reverseList(arr):
    first = 0
    last = len(arr) - 1

    while first < last:
        arr[first],arr[last] = arr[last],arr[first]
        first += 1
        last -= 1

    return arr

print(reverseList([5,4,3,2,1]))


'''
l = [10,20,30]
l.reverse()     # reverse given list
print(l)

l = [10,20,30]
new_l = list(reversed(l))   # return new reversed list
print(new_l)

l = [10,20,30]
new_l = l[::-1]             # return new reversed list
print(new_l)

'''
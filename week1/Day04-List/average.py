def average(arr):
    total = 0
    for i in arr:        # O(n)
        total += i
    print(f'The avg is {total/len(arr)}')


def avg(arr):
    return sum(arr)/len(arr)

average([8,9,10])

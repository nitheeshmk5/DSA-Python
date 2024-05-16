# def fre_idx(arr):
#     counts = {}

#     for element in arr:
#         if element in counts:
#             counts[element] += 1
#         else:
#             counts[element] = 1
    
    
#     repeated_elements = [num for num,value in counts.items() if value > 1]

#     return arr.index(repeated_elements[0])

# print(fre_idx([1, 5, 3, 4, 3, 5, 6]))

def firstRepeated(arr, n):

    first_occurrence = {}
    min_index = float('inf')

    for i in range(n):
        if arr[i] in first_occurrence:
            if first_occurrence[arr[i]] < min_index:
                min_index = first_occurrence[arr[i]]
        else:
            first_occurrence[arr[i]] = i + 1  

    if min_index == float('inf'):
        return -1  
    else:
        return min_index  

arr1 = [1, 5, 3, 4, 3, 5, 6]
n1 = len(arr1)
print(firstRepeated(arr1, n1))  

a = float('inf')
print(10 < a)



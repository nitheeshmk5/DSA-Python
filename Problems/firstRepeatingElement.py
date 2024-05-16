def fre_idx(arr):
    counts = {}

    for element in arr:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    
    
    repeated_elements = [num for num,value in counts.items() if value > 1]

    return arr.index(repeated_elements[0])

print(fre_idx([1, 5, 3, 4, 3, 5, 6]))
    
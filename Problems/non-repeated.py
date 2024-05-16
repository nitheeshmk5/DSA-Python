# def nonRep(arr):
#     counts = {}

#     for element in arr:
#         if element in counts:
#             counts[element] += 1
#         else:
#             counts[element] = 1
#     print(counts)
#     nonRepeated_elements = [key for key,value in counts.items() if value == 1]
#     return nonRepeated_elements

# print(nonRep([1,1,2,2,3,3,4,5,6,7]))

# def printNonRepeated(arr):
#     #Your code here
#     counts = {}
#     order =[]
    
#     for element in arr:
#         if element in counts:
#             counts[element] += 1
#         else:
#             counts[element] = 1
#             order.append(element)
            
#     nonRepeated = [elem for elem in order if counts[elem] == 1]
    
#     return nonRepeated

def nonRepChar(string):
    counts = {}
    order = []

    for letter in string:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
            order.append(letter)

    nonRep = [element for element in order if counts[element] == 1]
    if len(nonRep) == 0:
        return '$'
    else:
        return nonRep[0]

print(nonRepChar('aabbc'))
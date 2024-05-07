'''
Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) using sequences which have been already defined. Python supports the following 4 types of comprehensions:

-> List Comprehensions : output_list = [output_exp for var in input_list if (var satisfies this condition)]

-> Dictionary Comprehensions : output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}

-> Set Comprehensions
-> Generator Comprehensions
'''


def smallX(arr,x):
    small = [i for i in arr if i < x]
    print(small)

smallX([1,2,3,4,5],4)


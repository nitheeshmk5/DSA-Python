def evenOdd(arr):
    even = []
    odd = []
    for i in arr:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    
    print(f'Even : {even}\nOdd : {odd}')

evenOdd([1,2,3,4,5,6.6,7.7,8,9,10])
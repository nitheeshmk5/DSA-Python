def rotateList(arr,pos): # arr-> [1,2,3,4,5] pos->2 
    n = len(arr)
    '''
        For example, if n = 5 (array length) and pos = 7, rotating by 7 positions is the same as rotating by 7 % 5 = 2 positions (pos % n). 
    '''
    pos = pos % n 
    arr[:] = arr[pos:] + arr[0:pos]
    return arr

print(rotateList([1,2,3,4,5],2))



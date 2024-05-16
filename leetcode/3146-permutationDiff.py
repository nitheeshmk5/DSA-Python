# link -> https://leetcode.com/problems/permutation-difference-between-two-strings/

def perDiff(s,t):
    di = {}
    for idx,char in enumerate(s):
        '''
        0 a
        1 b
        2 c
        '''
        di[char] = idx
    diff = 0
    for idx,char in enumerate(t):
        #print(idx,char)
        '''
        0 b
        1 a
        2 c
        '''
        diff += abs(idx - di[char])  # (0 - 1) | (1 - 0) | (2 - 2) -> 1+1 = 2 
    print(diff)
perDiff('abc','bac')
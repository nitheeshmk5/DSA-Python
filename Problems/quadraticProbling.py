def QuadraticProbing(hash, hashSize, arr, n):
    for num in arr:
        original_position = num % hashSize
        hash_position = original_position
        i = 0
        
        while hash[hash_position] != -1:
            if hash[hash_position] == num:
                break
    
            i += 1
            hash_position = (original_position + i * i) % hashSize
            
        hash[hash_position] = num
        
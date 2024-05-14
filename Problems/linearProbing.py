def linearProb(m,arr,n):
    hash_table = [-1] * m
    for i in arr:
        idx = i % m
        orginal_idx = idx
        inserted = True

        while hash_table[orginal_idx] != -1:
            if hash_table[orginal_idx] == i:
                inserted = False
                break
            orginal_idx = (orginal_idx + 1) % m

            if orginal_idx == idx:
                inserted = False
                break
        if inserted:
            hash_table[orginal_idx] = i
    return hash_table
print(linearProb(10,[4,14,24,34],4))


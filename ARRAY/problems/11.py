# Find duplicates.

arr = [1,2,3,2,4,4,4]
size = 7 
duplicate = [None] * size
k = 0 

for i in range(size):
    for j in range(i+1,size):
        if arr[i] in duplicate:
            continue
        if arr[i] == arr[j]:
            duplicate[k] = arr[i]
            k += 1 

print(duplicate)
            
            

    




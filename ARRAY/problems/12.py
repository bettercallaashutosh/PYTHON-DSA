# Move zeros to end

arr = [1,0,2,0,0,3]
size = 6

new_arr = [None]*size

j = size-1
k = 0

for i in range(size):
    if arr[i] == 0:
        new_arr[j] = arr[i]
        j = j - 1
        
    else:
        new_arr[k] = arr[i]
        k = k + 1
    

print(new_arr)


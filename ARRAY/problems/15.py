#  Two sum (hash map approach)

arr = [1,3,5,2]
size = 4 

target = 6 

answer = [None]*size

k = 0 

for i in range(size):
    for j in range(i+1,size):
        if arr[i] + arr[j] == target:
            answer[k] = arr[i]
            answer[k+1] = arr[j] 
            break

print(answer)



# HASHMAP APPROACH 

hashmap = {}

for i in range(size):
    needed = target - arr[i]

    if needed in hashmap:
        print(needed,arr[i])
        break

    hashmap[arr[i]] = i 

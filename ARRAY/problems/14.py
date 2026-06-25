# Kadane's algorithm (max subarray sum)

arr = [-2,5,-3,8,-1,2]

size = 6

max_sum = 0 

def addition(array):
    total = 0
    for i in range(len(array)):
        total += array[i]

    return total

for i in range(size):
    for j in range(i+1,size+1):
        if  (addition(arr[i:j])) > max_sum:
            max_sum = addition(arr[i:j])


print(max_sum)




# Kadane's algorithm (max subarray sum)

arr = [-2,5,-3,8,-1,2]

size = 6

current_sum = 0
max_sum = 0 

for i in range(size):
    current_sum = current_sum + arr[i]
    if current_sum > max_sum :
        max_sum = current_sum
    if current_sum < 0:
        current_sum = 0

print(max_sum)


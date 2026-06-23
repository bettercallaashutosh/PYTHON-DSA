# Find second largest element

arr = [34, 30, 20, 10, 5]

size = 5

def find_second_max():
    if arr[0] > arr[1]:
        maximum = arr[0]
        second_max = arr[1]
    else:
        maximum = arr[1]
        second_max = arr[0]
    
    for i in range(2, size):
        if arr[i] > maximum:
            second_max = maximum
            maximum = arr[i]
        elif arr[i] > second_max and arr[i] != maximum:
            second_max = arr[i]
    
    return second_max

print(find_second_max())
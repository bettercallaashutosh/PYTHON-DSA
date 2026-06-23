# Reverse the array without creating a new array. Swap first and last, second and second-last, etc.

arr = [2,4,6,8,10]

size = 5 

def rev():
    global size
    
    i = 0 
    j = size - 1

    while i < j :
        arr[i], arr[j] = arr[j], arr[i]
        i += 1 
        j -= 1
    
    print(arr)

rev()
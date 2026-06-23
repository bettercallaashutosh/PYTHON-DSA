# Rotate array left by 1

arr = [1,2,3,4,5]

size = 5 

def rotate():
    global size 

    temp = arr[0]

    for i in range(size-1):
        arr[i] = arr[i+1]
        

   
    arr[size-1] = temp 

    return arr

print(rotate())
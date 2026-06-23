# Rotate array left by k

arr = [1,2,3,4,5]

k = 2 

size = 5 

def rotate():
    global size 

    temp = arr[0]

    for i in range(size-1):
        arr[i] = arr[i+1]
        

   
    arr[size-1] = temp 

    return arr


def rotate_by_k():

    for i in range(k):
        rotate()

    print(arr)


rotate_by_k()
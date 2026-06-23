# Check if array is sorted

arr = [1,2,3,4,6,5]
size = 6

def sorted():

    for  i in range(0,size-1):
        if arr[i] > arr[i+1]:
            print('Not sorted')
            return
    
    print('Sorted')


sorted()
    

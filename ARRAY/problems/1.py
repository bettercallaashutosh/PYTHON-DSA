# Add elements to the end of the array, one by one.

capacity = 5 

arr = [None] * capacity

size = 0 

def insert(value):
    global size
    
    if size == capacity:
       print('array is full')
       return
    
    arr[size] = value
    size += 1
    print(arr)


insert(10)
insert(100)
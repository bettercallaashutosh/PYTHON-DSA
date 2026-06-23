 # Delete element at index 2 from array [5, 20, 10, 15]. Result: [5, 20, 15].

capacity = 5 

arr = [None] * capacity

size = 0 

def insert_specific(index,value):
    global size 

    if index < 0 or index > size :
        print('invalid index')
        return 
    if size == capacity:
        print('array is full')
        return
    
    for i in range(size-1,index-1,-1):
        arr[i+1] = arr[i]

    arr[index] = value
    size += 1 

    
def delete(index):
    global size
    if index < 0 or index >= size:
        print('invalid index')
        return
    for i in range(index,size-1):
        arr[i] = arr[i+1]
        
    
    size -= 1
    print(arr)

insert_specific(0,5)
insert_specific(1,10)
insert_specific(2,15)
delete(1)



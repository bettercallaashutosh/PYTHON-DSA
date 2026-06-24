# Fixed-size array operations

capacity = 5
arr = [None] * capacity  # [None, None, None, None, None]
size = 0

def insert(index, value):
    global size
    if size == capacity:
        print('array is full')
        return
    if 0 > index or index > size :
        print('invalid index') 
        return
    
    for i in range(size-1,index-1,-1):
        arr[i+1] = arr[i]

    arr[index] = value
    size += 1 
    print(arr)


def delete(index):
    global size
    if index < 0 or index >= size:
        print('invalid index')
        return
    for i in range(index,size-1):
        arr[i] = arr[i+1]

    size -= 1
    print(arr)


def display():
    for i in range(size):
        print(arr[i], end=" ")
    print()

insert(0, 10)
insert(1, 20)
insert(2, 30)
display() 
delete(1)
display() 
delete(0)
display()
delete(0)
display()

    
   

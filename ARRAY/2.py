# Fixed-size array operations

capacity = 5
arr = [None] * capacity  # [None, None, None, None, None]
size = 0

def insert(index, value):
    global size
    if size == capacity :
        print('array is full')
        return
    if index < 0  or index > size :
        print('invalid index')
        return

    for i in range(size-1,index-1,-1):
        arr[i+1] = arr[i]

    arr[index] = value
    size +=1
    
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

def get(index):
    if index < 0 or index >= size:
        print('invalid index')
        return

    print(arr[index])

def search(value):
    for i in range(size):
        if arr[i] == value :
            return i
        
    return -1

insert(0,10)
insert(1,20)
insert(2,30)
get(0)
get(10)
print(search(20))
print(search(200))

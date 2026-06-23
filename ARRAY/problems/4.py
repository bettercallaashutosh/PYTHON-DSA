 # Write a function find_max() that returns the largest element in the array.
arr = [10,20,30,34,5]

size = 5

def find_max():
    maximum = arr[0]

    for i in range(1,size):
        if arr[i] > maximum:
            maximum = arr[i]

    print(maximum)

find_max()
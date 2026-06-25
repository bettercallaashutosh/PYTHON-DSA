 # Find intersection of two arrays

arr1 = [1,3,5,7,9,11]
size1 = 6

arr2 = [2,3,5,7,11]
size2 = 5

intersection = [None]*(size1 if size1 < size2 else size2)
k = 0 

for i in range(size1):
    for j in range(size2):
        if arr1[i] == arr2[j]:
            intersection[k] = arr1[i]
            k = k+1
            arr2[j] = None 
            break


print(intersection[:k])
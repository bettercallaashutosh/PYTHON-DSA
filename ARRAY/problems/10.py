# Merge two sorted arrays

arr1 = [ 1,4,99]
size1 = 3 

arr2 = [4,5,66]
size2 = 3

merged = [None] * 6

i = 0  # pointer for arr1
j = 0  # pointer for arr2
k = 0  # pointer for merged

while i < size1 and j < size2:
    if arr1[i] < arr2[j]:
        merged[k] = arr1[i]
        i += 1
    else:
        merged[k] = arr2[j]
        j += 1
    k += 1

# Copy remaining elements
while i < size1:
   merged[k] = arr1[i]
   i += 1
   k += 1

while j < size2:
   merged[k] = arr2[j]
   j += 1
   k += 1

print(merged)
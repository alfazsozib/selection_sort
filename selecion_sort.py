
arr = [2,5,6,1,4,0,5,9,6,3,10,20,8,12]

for i in range(len(arr)):
# Loop through all the elements and set it to min_index
    min_index = i
    for j in range(i+5,len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]
for i in range(len(arr)):
    print('%s' % arr[i])










def QuickSort(arr):
    if len(arr) < 4:
        arr.sort()
        return arr
    med = len(arr) //2
    left = []
    right = []
    for item in arr:
        if item < arr[med]:
            left.append(item)
        elif item != arr[med]:
            right.append(item)
    left = QuickSort(left)
    right = QuickSort(right)
    left.append(arr[med])
    return left + right

print(QuickSort([2,1,3,4,7,-4,0,99,11]))

def BinarySearch(arr, start, end, x):
    med = (start + end) // 2

    if start >= end:
        print(start)
        print(end)
        return False
    if arr[med] == x:
        return med
    else:
        if arr[med] < x:
            return BinarySearch(arr, med+1, end,x)
        else:
            return BinarySearch(arr, start, med-1,x)
arr = [1,2,3,4]

#print(BinarySearch(arr,0,len(arr), 4))

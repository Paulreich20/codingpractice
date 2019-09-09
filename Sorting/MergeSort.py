def Merge(left, right):
    sorted = []
    leftmark = 0
    rightmark = 0
    while len(sorted) != (len(left)+len(right)):
        if leftmark == len(left):
            sorted.append(right[rightmark])
            rightmark += 1
        elif rightmark == len(right) or left[leftmark] <= right[rightmark]:
            sorted.append(left[leftmark])
            leftmark +=1
        else:
            sorted.append(right[rightmark])
            rightmark += 1
    return sorted

def MergeSort(arr):
    if len(arr) < 4:
        arr.sort()
        return arr
    med = len(arr) // 2
    left = MergeSort(arr[0:med])
    right = MergeSort(arr[med:])
    return Merge(left,right)


print(MergeSort([3,2,1,4,0,-5,4,77,100,99999,-45,6,7,8]))

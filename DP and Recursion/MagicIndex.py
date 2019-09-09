def Mag(arr, start, end):
    med = (start+ end) // 2
    if arr[med] == med:
        return True
    if start == end:
        return False
    else:
        if arr[med] > med:
            return Mag(arr,start, med -1)
        else:
            return Mag(arr, med+1, end)

    Mag(arr, 0, len(arr)-1)

myArray = [-10,-5,2,2,2,3,4,7,9,12,13]
print(Mag(myArray, 0, len(myArray)-1))

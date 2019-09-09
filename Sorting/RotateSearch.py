import BinarySearch

def Rotate(arr, query, start, end):
    med = start + end // 2
    if arr[med] == query:
        return med
    if start >= end:
        return false
    if arr[med] < query:
        if arr[med] < arr[end]:  # the rotation is in the first half
            if query == arr[end]:
                return end
            if query < arr[end]:
                print('he')
                BinarySearch(arr, query, med+1, end-1)
            else:
                Rotate(arr, query, start, med-1)
        else:
            if query == arr[end]:
                return end
            if query < arr[end]:
                Rotate(arr, query, med+1, end-1)
            else:
                print("today")
                BinarySearch(arr,query, start, med-1)
    else:
        if arr[med] < arr[end]:  # the rotation is in the firsthalf
            if query == arr[end]:
                return end
            if query > arr[end]:
                Rotate(arr, query, start, med-1)
            else:
                print("hel")
                BinarySearch(arr, query, med+1, end-1)

        else:
            if query == arr[end]:
                return end
            if query > arr[end]:
                print('here')
                BinarySearch(arr, query, start, med-1)                                                                                                                                                           
            else:
                Rotate(arr, query, med+1, end)

arr =[4,1,2,3]
Rotate( arr, 3, 0, len(arr))

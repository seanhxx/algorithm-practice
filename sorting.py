def quickSort(A):
    if len(A) <= 1:
        return A
    last = 0
    for i in range(1, len(A)):
        if A[i] < A[0]:
            last += 1
            A[i], A[last] = A[last], A[i]
    A[0], A[last] = A[last], A[0]
    left = quickSort(A[:last+1])
    right = quickSort(A[last+1:])
    return left + right


def mergeSort(a):
    if len(a) == 1:
        return a
    else:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        sortedleft = mergeSort(left)
        sortedright = mergeSort(right)
        i = 0
        j = 0
        sorted_a = []
        while i < len(left) and j < len(right):
            if sortedleft[i] <= sortedright[j]:
                sorted_a.append(sortedleft[i])
                i += 1
            else:
                sorted_a.append(sortedright[j])
                j += 1
        while i < len(left):
            sorted_a.append(sortedleft[i])
            i += 1
        while j < len(right):
            sorted_a.append(sortedright[j])
            j += 1
        return sorted_a


array = [6,5,4,3,2,1]
# new_array = quickSort(array)
new_array = mergeSort(array)
print("new array is {}".format(new_array))

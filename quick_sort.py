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


array = [6,5,4,3,2,1]
new_array = quickSort(array)
print("new array is {}".format(new_array))

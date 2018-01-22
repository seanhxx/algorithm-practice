a = [0,4,7,3,3,5]
b = [0,3,3,7,5,3,11,6,2]
c = [5,4,3,2,1]
d = [0,1,1,1,2]
def mergesort(a):
    if len(a) == 1:
        return a
    else:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        sortedleft = mergesort(left)
        sortedright = mergesort(right)
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

def dict_generator(a):
    dict_a = {}
    for i in range(len(a)):
        dict_a[i] = a[i]
    return dict_a

e = dict_generator(a)

f = sorted(enumerate(d), key=lambda x:x[1])
print(f)
def findmax(t):
    i = 0
    j = 0
    next_low_index = 0
    low = 0
    high = 0
    maxvalue = -1
    while next_low_index < len(a) - 1:
        if t[i][1] == t[j][1]:
            j = j + 1
            next_low_index = j
        else:
            while j < len(a) - 2 and t[j][1] == t[j+1][1]:
                j = j + 1
            if maxvalue < abs(t[j][0] - t[i][0]):
                maxvalue = abs(t[j][0] - t[i][0])
                low = min(t[i][0],t[j][0])
                high = max(t[i][0],t[j][0])
            if j == len(a) - 1 and t[j-1][1] == t[j][1]:
                break
            i = next_low_index
            j = i
    return low, high, maxvalue

low, high, maxvalue = findmax(f)
print('({}, {}), {}'.format(low, high, maxvalue))

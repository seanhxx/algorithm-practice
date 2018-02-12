A1 = [0,6,5,1,2,3,4]
A2 = [1,2,3,4,0]

def check_duplicates(A):
    flag_duplicate = 0
    for index in range(len(A)):
        temp = -1
        if A[index] == index:
            pass
        else:
            a = A[index]
            A[index] = temp
            temp = a
            while temp != -1:
                if A[temp] == temp:
                    flag_duplicate = 1
                    break
                else:
                    a = A[temp]
                    A[temp] = temp
                    temp = a
            if flag_duplicate == 1:
                break

    if flag_duplicate == 0:
        print("No duplicates")
    else:
        print("Has duplicates")

check_duplicates(A1)


pos = -1
def search(list,n):
    lowerbound = 0
    upperbound = len(list)-1

    while lowerbound <= upperbound:
        mid = (lowerbound+upperbound)//2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid]<n:
                lowerbound = mid + 1
            else:
                upperbound = mid - 1
    return False

list = [4,7,8,12,45,99]
n = 8

if search(list,n):
    print("found at",pos+1)
else:
    print("not found")
def binarysearch(A,key):
    A.sort()
    low=0
    high=len(A)-1
    while low<=high:
        mid=(low+high)//2
        if key==A[mid]:
            return True
        elif key<A[mid]:
            high=mid-1
        else:
            low=mid+1
    return False

A=[90,56,12,34,13,83,78]
found=binarysearch(A,83)
print('The element 83 is:',found)
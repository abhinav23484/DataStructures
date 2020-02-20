def binarysearch(a,key,low,high):
    if low>high:
        return False
    else:
        mid=(low+high)//2
        if key==A[mid]:
            return True
        elif key<A[mid]:
            return binarysearch(A,key,low,mid-1)
        else:
            return binarysearch(A,key,mid+1,high)

A=[1,2,3,9,7,4,22]
A.sort()
found=binarysearch(A,4,0,7)
print('The element 4 is:',found)
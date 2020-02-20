def linearsearch(A,key):
    position=0
    flag=False
    while position<len(A) and not flag:
        if A[position]==key:
            flag=True
        else:
            position=position+1
    return flag
A=[15,78,90,45,66,36]
found=linearsearch(A,66)
print('Element 66 is present:',found)
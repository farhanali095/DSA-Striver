def merge(arr,l,m,r):
    n1=m-l+1
    n2=r-m
    L=[0]*n1
    R=[0]*n2
    for i in range(n1):
        L[i]=arr[l+i]
    for i in range(n2):
        R[i]=arr[m+1+i]

    i=0
    j=0
    k=l
    while i<n1 and j<n2:
        if L[i]<R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1
def mergeSort(arr,l,r):
    if l<r:
        m=(l+r)//2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)
arr=[4,2,1,6,7]
mergeSort(arr,0,len(arr)-1)
print(*arr)
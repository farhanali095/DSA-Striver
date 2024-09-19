def solve(arr):
    n=len(arr)
    x=0
    for i in range(1,n):
        if arr[i]!=arr[x]:
            x+=1
            arr[x]=arr[i]
    return x+1
arr=[1,1,1,2,2,3,3,3,3,4,4]
print(solve(arr))
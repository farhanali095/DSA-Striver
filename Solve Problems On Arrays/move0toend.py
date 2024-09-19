def solve(arr):
    ans=[]
    n=len(arr)
    for i in range(n):
        if arr[i]!=0:
            ans.append(arr[i])
    n1=len(ans)
    for i in range(n1):
        arr[i]=ans[i]
    for i in range(n1,n):
        arr[i]=0
    return arr
arr=[1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
print(*solve(arr))
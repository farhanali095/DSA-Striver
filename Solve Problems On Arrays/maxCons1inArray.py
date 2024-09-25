def solve(arr):
    count=0
    maxi=float('-inf')
    for i in range(n):
        if arr[i]==1:
            count+=1
        else:
            count=0
        maxi=max(maxi,count)
    return maxi
n=6
arr=[1,1,1,0,1,1]
print(solve(arr))
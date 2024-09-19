def solve(arr):
    temp=arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]
    arr[-1]=temp
    return arr
n=5
arr=[1,2,3,4,5]
print(*solve(arr))
def solve(arr,n):
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
    return True
n=5
arr=[1,2,3,4,5]
print(solve(arr,n))
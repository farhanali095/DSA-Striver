def solve(arr):
    maxi=float('-inf')
    for i in range(len(arr)):
        if arr[i]>maxi:
            maxi=arr[i]
    return maxi
arr=[2,5,1,3,0]
print(solve(arr))
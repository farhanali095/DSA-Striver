def solve(arr,n,target):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return "Yes"
    return "No"
n=5
arr=[2,6,5,8,11]
target=14
print(solve(arr,n,target))

def index(arr,n,target):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return [i,j]
    return [-1,-1]
n=5
arr=[2,6,5,8,11]
target=14
print(index(arr,n,target))
def solve(arr,num):
    for i in range(len(arr)):
        if arr[i]==num:
            return i
    return -1
arr=[5,4,3,2,1]
num=5
print(solve(arr,num))
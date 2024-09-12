def solve(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[mini]>arr[j]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]

arr=[13,46,24,52,20,9]
print(*solve(arr))
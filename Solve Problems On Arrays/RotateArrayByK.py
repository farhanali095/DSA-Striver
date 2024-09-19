def solve(arr,n,k):
    if n==0:
        return
    
    # Ensure k is within the array size
    k=k%n
    if k>n:
        return
    
    # Create a temporary array to store the rotated elements
    ans=[0]*k
    x=0

    # Store the last k elements in temp array
    for i in range(n-k,n):
        ans[x]=arr[i]
        x+=1

    # Shift the first n-k elements to the right
    for i in range(n-k-1,-1,-1):
        arr[i+k]=arr[i]

    # Copy the temp array back to the first k elements
    for i in range(k):
        arr[i]=ans[i]
    return arr
n=7
arr=[1,2,3,4,5,6,7]
k=2
print(*solve(arr,n,k))
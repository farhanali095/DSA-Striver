# def solve(arr):
#     n=len(arr)
#     maxi=float('-inf')
#     for i in range(n):
#         sumi=0
#         for j in range(i,n):
#             sumi+=arr[j]
#             maxi=max(maxi,sumi)
#     return maxi
# arr=[-2,1,-3,4,-1,2,1,-5,4]
# print(solve(arr))

def solve(arr):
    n=len(arr)
    maxi=float('-inf')
    curr=0
    for i in range(n):
        curr+=arr[i]
        if curr>maxi:
            maxi=curr
        if curr<0:
            curr=0
    return maxi
arr=[-2,1,-3,4,-1,2,1,-5,4]
print(solve(arr))
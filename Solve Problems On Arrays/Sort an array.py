# def solve(arr):
#     for i in range(len(arr)-1):
#         for j in range(i+1,len(arr)):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
#     return arr
# arr=[2,0,2,1,1,0]
# print(solve(arr))

def solve(arr):
    l,m,h=0,0,len(arr)-1
    while m<=h:
        if arr[m]==0:
            arr[l],arr[m]=arr[m],arr[l]
            l+=1
            m+=1
        elif arr[m]==1:
            m+=1
        else:
            arr[m],arr[h]=arr[h],arr[m]
            h-=1
    return arr
arr=[2,0,2,1,1,0]
print(solve(arr))
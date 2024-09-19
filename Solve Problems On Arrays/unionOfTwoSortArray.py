def solve(n,m,arr1,arr2):
    d={}
    ans=[]
    for i in arr1:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in arr2:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        ans.append(i)
    return ans
n=5
m=5
arr1=[1,2,3,4,5]
arr2=[2,3,4,4,5]
print(solve(n,m,arr1,arr2))

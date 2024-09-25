def solve(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i,j in d.items():
        if j==1:
            print(i)
arr=[4,1,2,1,2]
solve(arr)
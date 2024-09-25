def solve(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i,j in d.items():
        if j>len(arr)/2:
            print(i)
arr=[4,4,2,4,3,4,4,3,2,4]
solve(arr)
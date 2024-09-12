def solve(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for key,value in d.items():
        print(key,value)
arr=[10,5,10,15,10,5]
solve(arr)
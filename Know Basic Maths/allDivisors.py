def solve(n):
    ans=[]
    for i in range(1,n+1):
        if n%i==0:
            ans.append(i)
    return ans
n=36
print(solve(n))
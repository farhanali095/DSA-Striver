def solve(n):
    y=n
    x=0
    z=len(str(n))
    while n!=0:
        rem=n%10
        x+=(rem**z)
        n//=10
    return y==x
n=153
print(solve(n))
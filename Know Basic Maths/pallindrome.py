def solve(n):
    ans=0
    N=n
    while n!=0:
        rem=n%10
        ans=(ans*10)+rem
        n//=10
    return N==ans
n=4554
print(solve(n))
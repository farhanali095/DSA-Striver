def solve(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=10
print(solve(n))
# def solve(n):
#     ans=""
#     for i in reversed(str(n)):
#         ans+=i
#     return ans
# n=12345
# print(solve(n))

def solve(n):
    ans=0
    while n!=0:
        rem=n%10
        ans=(ans*10)+rem
        n//=10
    return ans
n=10300
print(solve(n))
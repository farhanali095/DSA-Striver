# import math
# def solve(n1,n2):
#     return math.gcd(n1,n2)
# n1,n2=9,12
# print(solve(n1,n2))
def solve(n1,n2):
    while n2!=0:
        n1,n2=n2,n1%n2
    return n1
n1,n2=9,12
print(solve(n1,n2))
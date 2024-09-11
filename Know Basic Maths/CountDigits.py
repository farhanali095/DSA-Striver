# def solve(n):
#     count=0
#     for i in str(n):
#         count+=1
#     return count
# n=12345
# print(solve(n))

def solve(n):
    count=0
    while n!=0:
        count+=1 
        n//=10
    return count
n=12345
print(solve(n))
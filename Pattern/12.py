# def solve(n):
#     spa=2*(n-1)
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end="")
#         for k in range(1,spa+1):
#             print(" ",end="")
#         for l in range(i,0,-1):
#             print(l,end="")
#         print()
#         spa-=2
# n=4
# solve(n)
def dualTriangle(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if j <= i:
                print(j, end="")
            else:
                print(" ", end="")
        for k in range(num, 0, -1):
            if k <= i:
                print(j, end="")
            else:
                print(" ", end="")
        print()
num = 4
dualTriangle(num)
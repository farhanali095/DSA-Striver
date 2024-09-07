def solve():
    for i in range(1,6):
        for j in range(5,i,-1):
            print(" ",end="")
        for k in range((2*i)-1):
            print("*",end="")
        print()
    for i in range(5,0,-1):
        for j in range(5,i,-1):
            print(" ",end="")
        for k in range((2*i)-1):
            print("*",end="")
        print()
solve()
# def diamond(num):
#     for i in range(1, num + 1):
#         for j in range(num, i, -1):
#             print(" ", end="")
#         for k in range(0, (2 * i) - 1):
#             print("*", end="")
#         print()
    
#     for i in range(num , 0, -1):
#         for j in range(num, i, -1):
#             print(" ", end="")
#         for k in range(0, (2 * i) - 1):
#             print("*", end="")
#         print()

# num =5
# diamond(num)
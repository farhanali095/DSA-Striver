def solve():
    for i in range(1,5):
        for j in range(4,i,-1):
            print(" ",end="")
        for k in range((2*i)-1):
            print(chr(64+k),end="")
        print()
solve()
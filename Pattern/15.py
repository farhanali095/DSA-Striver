def solve():
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(chr(64+j),end="")
        print()
n=5
solve()
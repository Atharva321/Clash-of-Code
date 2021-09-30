n,r=map(int,input().split())
#using lambda to take to print
print(*map(lambda x:r**x,range(n)),sep=" ")

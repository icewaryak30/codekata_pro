n,p,q,r=map(int,input().split())
l=[int(i) for i in input().split()]
y=[]
x=[p*l[i]+q*l[j]+r*l[k] for i in range(len(l)) for j in range(len(l)) for k in range(len(l)) if i<=j<=k]
print(max(x))

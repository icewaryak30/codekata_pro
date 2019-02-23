n,w=map(int,input().split())
W=[int(i) for i in input().split()]
V=[int(i) for i in input().split()]
d={}
for i in range(len(W)):
    d.update({W[i]:V[i]})
x=sorted(V,reverse=True)
print(x)
wei=0
l=[]
for i in x:
    for k,v in d.items():
        if v==i:
            wei+=k
            print(wei,k)
            if wei<=w:
                l.append(v)
            else:
                wei-=k
            break
print(l)

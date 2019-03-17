n=input()
if int(n)%8==0:
	p="yes"
else:
	for i in range(1,len(n)):
		if int(n[:i])%8==0 or int(n[i])%8==0:
			p="yes"
			break
		else:
			p="no"
print(p)

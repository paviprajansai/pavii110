p1,p2=map(str,input().split())
c1=max(len(p1),len(p2))
p=0
for i in range(c1):
	if p1[i]!=p2[i]:
		p=p+1
if p==1:
	print("yes")
else:
	print("no")

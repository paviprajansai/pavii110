l,r1=map(int,input().split())
for i1 in range(2,10000):
	if i1%l==0 and i1%r1==0:
		print(i1)
		break

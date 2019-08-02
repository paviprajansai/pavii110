n11,k11=map(int,input().split())
p11=[]
s11=""
l=list(map(int,input().split()))
for i in range(0,k11):
	l.append(l[0])
	l.remove(l[0])
for i in l:
   
        s11=s11+str(i)+" "
print(s11.strip())



def a(x):
	b=0
	c= 0
	d =0
	for i in range(1,x+1):
		b = b+i**2
		c=c+i;
	d = c**2
	print('resulttt',d-b)
	

n = int(input('Enter no of rows: '))
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j,end=' ')
	for k in range(i-1,0,-1):
		print(k,end=" ")
	print('\n')
	
	

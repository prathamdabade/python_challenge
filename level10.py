from itertools import groupby
def lookandsay(n):
    return ''.join( str(len(list(g))) + k for k, g in groupby(n))

num = "1"
for i in range(30):
	num = lookandsay(num)
	
print(len(num))
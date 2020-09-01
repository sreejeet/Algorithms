import time

def mergesorted(a):
	if len(a) <= 1:
		return a

	mid = len(a)//2
	L = mergesorted(a[:mid])
	R = mergesorted(a[mid:])
	a = []
	x = y = 0

	while True:
		Lx = L[x] if x < len(L) else None
		Ry = R[y] if y < len(R) else None
		if Lx == None and Ry == None:
			break
		if Lx == None:
			a.extend(R[y:])
			break
		if Ry == None:
			a.extend(L[x:])
			break
		if len(Lx) < len(Ry):
			a.append(Lx)
			x+=1
		else:
			a.append(Ry)
			y+=1

	return a

if __name__ == '__main__':
	a = [
		"#####",
		"######",
		"#",
		"#########",
		"##########",
		"########",
		"####",
		"###",
		"#######",
		"##",
	]

	print(mergesorted(a))


""" Output
['#', '##', '###', '####', '#####', '######', '#######', '########', '#########', '##########']
"""
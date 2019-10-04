import time

def mergesorted(a):
	if len(a) > 1:
		m = len(a)//2
		L = mergesorted(a[:m])
		R = mergesorted(a[m:])
		a = []
		x = y = 0
		while True:
			Lx = L[x] if x < len(L) else None
			Ry = R[y] if y < len(R) else None
			if Lx == None and Ry == None:
				break
			if Lx == None:
				a.append(Ry)
				y+=1
			elif Ry == None:
				a.append(Lx)
				x+=1
			else:
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
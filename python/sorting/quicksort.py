def quicksorted(a):
	if len(a) > 1:
		# selecting pivot using
		# median of 3 method
		mid = len(a) // 2
		if a[mid] < a[0]:
			a[0], a[mid] = a[mid], a[0]
		if a[-1] < a[0]:
			a[-1], a[0] = a[0], a[-1]
		if a[mid] < a[-1]:
			a[-1], a[mid] = a[mid], a[-1]

		pivot = a[-1]
		L = []
		R = []
		M = []
		for x in a:
			if x < pivot:
				L += [x]
			elif x == pivot:
				M += [x]
			else:
				R += [x]
		return \
			(quicksorted(L)) +\
			M +\
			(quicksorted(R))
	else:
		return a


if __name__ == '__main__':
	a = [
		55555,
		666666,
		1,
		999999999,
		1010101010,
		88888888,
		4444,
		333,
		7777777,
		22,
	]

	for x in a:
		print(x)

	print("\nPerforming Quicksort\n")
	a = quicksorted(a)

	for x in a:
		print(x)


""" Output
55555
666666
1
999999999
1010101010
88888888
4444
333
7777777
22

Sorting

1
22
333
4444
55555
666666
7777777
88888888
999999999
1010101010
"""

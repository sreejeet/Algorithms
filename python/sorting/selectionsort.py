import time

def selectionsorted(a):
	length = len(a)

	for i in range(length-1):
		smallest = i

		for x in range(i+1, length):
			if len(a[x]) < len(a[smallest]):
				smallest = x

		if smallest != i:
			a[smallest], a[i] = a[i], a[smallest]
			print(f"\r{a}")
			time.sleep(0.5)

	return a


if __name__ == '__main__':
	a = [
		"#####",
		"######",
		"#",
		"#########",
		"########",
		"####",
		"###",
		"#######",
		"##",
	]

	selectionsorted(a)

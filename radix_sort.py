def radix_sort(ints):
	mod = 10
	denom = 1
	lens = len(ints)

	while True:
		bins = [[] for i in range(10)]
		for i in ints:
			least = (i / denom) % mod
			bins[least].append(i)

		if len(bins[0]) == lens:
			return bins[0]

		mod *= 10
		denom *= 10
		ints = [item for sublist in bins for item in sublist]
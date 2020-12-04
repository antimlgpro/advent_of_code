inp = []
with open("1.txt", "r") as f:
	inp = f.read().splitlines()


def solution_1(_inp):
	frequency = 0
	seen = []
	for s in range(0, 1):
		print(f"Repeat {s}")
		for freq in _inp:
			if "+" in freq:
				frequency += int(freq[1:])
				seen.append(frequency)
			elif "-" in freq:
				frequency -= int(freq[1:])
				seen.append(frequency)
			if frequency in seen:
				print(f"{frequency} has been seen twice")
solution_1(inp)
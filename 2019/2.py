import sys

def add(data, code):
	cmd = data[0]
	pos1, pos2, pos3 = data[1:4]
	num1 = code[pos1]
	num2 = code[pos2]
	code[pos3] = num1 + num2
	return code[pos3]

def multi(data, code):
	cmd = data[0]
	pos1, pos2, pos3 = data[1:4]

	num1 = code[pos1]
	num2 = code[pos2]
	code[pos3] = num1 * num2
	return code[pos3]

def halt(data, *args):
	return 0

opcodes = {
	1: add, 
	2: multi,
	99: halt,
}


with open("2.txt", "r") as f:
	code_orig = f.read().split(",")

code_orig = list(map(int, code_orig))


def solution_1():
	ln = 0
	code = code_orig.copy()
	for idx,c in enumerate(code_orig):
		if idx % 4 == 0:
			ln += 1
			if c == 99:
				ret = opcodes.get(c)(code_orig[idx], code)
				#print(f"line {ln}: {code_orig[idx]} returned {ret}")
				break

			ret = opcodes.get(c)(code_orig[idx:idx+4], code)
			print(f"line {ln}: {code_orig[idx:idx+4]} returned {ret}")
	
	#print("COMPLETE",code_orig)
	return code_orig


def solution_2():
	ln = 0
	tri = 0
	code = []
	code = code_orig
	for n in range(0,100):
		ln = 0
		code = code_orig.copy()
		for v in range(0,100):
			ln = 0
			tri += 1
			code = code_orig.copy()
			code[1] = n
			code[2] = v
			#print(f"\rTrying noun {n}, verb {v}", end="")
			for idx,c in enumerate(code):
				if idx % 4 == 0:
					ln += 1
					if c == 99:
						ret = opcodes.get(c)(code[idx], code)
						break
					ret = opcodes.get(c)(code[idx:idx+4], code)
				if code[0] == 19690720:
					print(f"Correct 100 * {n} + {v} = {100 * n + v}")
					return 100 * n + v
	
	print("NO SOLUTION FOUND",code[0])

print(solution_1()) ## solution [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 10, 19, 1, 19, 5, 23, 2, 23, 6, 27, 1, 27, 5, 31, 2, 6, 31, 35, 1, 5, 35, 39, 2, 39, 9, 43, 1, 43, 5, 47, 1, 10, 47, 51, 1, 51, 6, 55, 1, 55, 10, 59, 1, 59, 6, 63, 2, 13, 63, 67, 1, 9, 67, 71, 2, 6, 71, 75, 1, 5, 75, 79, 1, 9, 79, 83, 2, 6, 83, 87, 1, 5, 87, 91, 2, 6, 91, 95, 2, 95, 9, 99, 1, 99, 6, 103, 1, 103, 13, 107, 2, 13, 107, 111, 2, 111, 10, 115, 1, 115, 6, 119, 1, 6, 119, 123, 2, 6, 123, 127, 1, 127, 5, 131, 2, 131, 6, 135, 1, 135, 2, 139, 1, 139, 9, 0, 99, 2, 14, 0, 0]
print(solution_2()) ## solution 42, 59 4259 
import string
from itertools import groupby

with open("4.txt", "r") as f:
	inp = f.read().split("\n")

idx = 0
passports = []
for e in inp:
	if e == '':
		idx += 1
	else:
		try:
			passports[idx] += e + " "
		except:
			passports.insert(idx, e + " ")


def valid_check(ps):
	matches = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
	if all(x in ps for x in matches):
		if 'cid' not in ps:
			#print(f"{idx} - no cid, valid - {ps}")
			return True
		#print(f"{idx} - no missing, valid - {ps}")
		return True
	else:
		#print(f"{idx} - missing, not valid - {ps}")
		return False

def solution_1(_inp):
	valid = 0
	for idx,ps in enumerate(_inp):
		if valid_check(ps):
			valid += 1
		
	return valid

def solution_2(_inp, output):
	valid = 0
	for ps in _inp:
		passpr = ps.split(" ")
		
		if valid_check(ps):
			params = {}
			del passpr[-1]
			passed = 0
			for pr in passpr:
				pr = pr.split(":")
				params[pr[0]] = pr[1]
			for param, value in params.items():
				if param == "byr":
					if len(value) == 4 and 1920 <= int(value) <= 2002:
						#print("byr valid")
						passed += 1
					else:
						if output: print(f"byr invalid {value}")
				if param == "iyr":
					if len(value) == 4 and 2010 <= int(value) <= 2020:
						if output: print("iyr valid")
						passed += 1
					else:
						if output: print(f"iyr invalid {value}")
				if param == "eyr":
					if len(value) == 4 and 2020 <= int(value) <= 2030:
						if output: print("eyr valid")
						passed += 1
					else:
						if output: print(f"eyr invalid {value}")
				if param == "hgt":
					hgt = [''.join(g) for _, g in groupby(value, str.isalpha)]
					if len(hgt) == 2:
						if hgt[1] == "in" and 59 <= int(hgt[0]) <= 76:
							if output: ("hgt valid")
							passed += 1
						elif hgt[1] == "cm" and 150 <= int(hgt[0]) <= 193:
							if output: print("hgt valid")
							passed += 1
						else:
							if output: print(f"hgt invalid {value}")
					else:
						if output: print(f"hgt invalid {value}")
				if param == "hcl":
					if value[0] == "#" and len(value) == 7:
						if all(c in "0123456789abcdef" for c in value[1:]):
							if output: print("hcl valid")
							passed += 1
						else:
							if output: print(f"hcl invalid {value}")
				if param == "ecl":
					matches = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
					if any(x in value for x in matches):
						if output: print(f"ecl valid")
						passed += 1
					else:
						if output: print(f"ecl invalid {value}")
				if param == "pid":
					if len(value) == 9:
						if output: print("pid valid")
						passed += 1
					else:
						if output: print(f"pid invalid {value}")
			if passed == 7:
				valid += 1
			
					
				
		
	return valid
		
valid1 = solution_1(passports)
valid2 = solution_2(passports, False)
print(f"Valid: {valid1}\nValid: {valid2}")  ## 170, 103
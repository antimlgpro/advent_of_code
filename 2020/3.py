import math
import time
from typing import List, Union, Tuple
inputtxt = []

with open("3.txt", "r") as f:
	inputtxt = f.read().splitlines()

def gen_coordinates(data: List) -> Union[int, int,dict]:
	coordinates = {}
	width = 0
	height = 0

	y = None
	for y,line in enumerate(data):
		width = len(line)
		for x,char in enumerate(line):
			coordinates[(x,y)] = char
	
	height = y
	return width, height, coordinates

def find_trees(data: List) -> dict:
	tree_coords = {}

	for y,line in enumerate(data):
		for x,char in enumerate(line):
			if "#" in char:
				tree_coords[(x,y)] = char

	return tree_coords

def calculate_slope(coords: dict, trees: dict, angle: List, width: int, height: int) -> Union[dict, int]:
	slope_coord = {}

	stx, sty = next(iter(coords.keys()))
	coords[(stx,sty)] = "S"

	bottom = False
	tree_count = 0

	while not bottom:
		stx += angle[0]
		sty += angle[1]
		if stx >= width:
			stx -= width
		key = (stx, sty)
		if sty > height:
			bottom = True
			break
		if key in trees:
			tree_count += 1
			coords[key] = "X"
		else:
			coords[key] = "O"
	slope_coord = coords
	print(f"Angle {', '.join(map(str, angle))} reached bottom {stx}, {sty} with tree count {tree_count}")
	return slope_coord, tree_count

def solution_1(coords,trees,width,height):
	angle = [3,1]
	s_coords, trees_count = calculate_slope(coords, trees, angle, width, height)
	return trees_count, s_coords

def solution_2(coords,trees,width,height):
	trarr = []
	angle = [[1,1],[3,1],[5,1],[7,1],[1,2]]

	s_coords = None
	for a, ang in enumerate(angle):
		s_coords, trees_count = calculate_slope(coords, trees, ang, width, height, str(a))
		trarr.append(trees_count)
	return math.prod(trarr), s_coords

width, height, coords = gen_coordinates(inputtxt)
trees = find_trees(inputtxt)


sol, s_coords = solution_1(coords, trees, width, height)
#sol, s_coords = solution_2(coords,trees, width, height)
print(sol)

## Prints map of S P A C E T R E E S

for i, (k,v) in enumerate(s_coords.items()):
	if v == "#":
		s_coords[k] = "\u001b[32;1m#\u001b[0m"
	if v == ".":
		s_coords[k] = " "
	if v == "X":
		s_coords[k] = "\u001b[31;1mX\u001b[0m"
	if v == "O":
		s_coords[k] = "\u001b[34;1mO\u001b[0m"

enable = True
if enable == True:
	for i,(k,v) in enumerate(s_coords.items()):
		if i % width == 0:
			print("\n",end="")
		print(v, end="")
		time.sleep(3 / 1000)

	print("")

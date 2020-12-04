from itertools import combinations
inp = []
with open("1.txt", "r") as f:
    inp = f.read().splitlines()

def solution_1(_inp):
    _inp = list(map(int, _inp))
    out = combinations(_inp, 2)
    for o in out:
        if o[0] + o[1] == 2020:
            print(f"success, {o[0]}  {o[1]}, {o[0]*o[1]}")
            return

def solution_2(_inp):
    _inp = list(map(int, _inp))
    out = combinations(_inp, 3)
    for o in out:
        if o[0] + o[1] + o[2] == 2020:
            print(f"success, {o[0]}  {o[1]}, {o[2]}, {o[0]*o[1]*o[2]}")
            return


solution_2(inp)
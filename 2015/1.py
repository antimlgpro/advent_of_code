inp = ""
with open("1.txt", "r") as f:
    inp = f.read()

def solution_1(_inp):
    floor = 0
    for i,inst in enumerate(_inp):
        if inst == "(":
            floor += 1
        elif inst == ")":
            #print(f"Going down from {floor}")
            if floor == 0:
                print(f"Basement time {i+1}")
            floor -= 1
    print(floor)

solution_1(inp)
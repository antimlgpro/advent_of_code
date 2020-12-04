inps = []
with open("2.txt", "r") as f:
    inps = f.read().splitlines()


## part 1
## solution 634

def solution_1():
    cor = 0
    for i in inps:
        current_rule, passw = i.split(":")
        minn, maxx = current_rule.split("-")
        maxx, lett = maxx.split(" ")
        minn, maxx = (int(minn),int(maxx))
        passw = passw.strip()
        
        charray = list(passw)
        letcount = charray.count(lett)
        
        if letcount in range(minn,maxx+1):
            cor += 1
    return cor


## part 2
## solution 634

def solution_2():
    cor = 0
    for index,i in enumerate(inps):
        #if index > 100:
        #    break
        current_rule, passw = i.split(":")
        has, bad = current_rule.split("-")
        bad, lett = bad.split(" ")

        has, bad = (int(has),int(bad))
        passw = passw.strip()
        
        password_pos = [passw[int(has)-1], passw[int(bad)-1]]

        if password_pos.count(lett) == 1:
            #print(f"{password_pos} has 1 ocurrence of {lett}")
            cor += 1

    return cor


print("solution_1:", solution_1())
#print("solution_2:", solution_2())
lines = open("nr2list","r")
lijst= []
for line in lines:
    stripped_line = line.strip()
    lijst.append(stripped_line)



def nr2():
    y = 0
    x = 0
    aim = 0
    for each in lijst:
        if "forward" in each:
            x += int(each.strip("forwardnup"))
            y += (int(each.strip("forwardnup")) * aim)
        elif "up" in each:
            aim -= int(each.strip("forwardnup"))
        elif "down" in each:
            aim += int(each.strip("forwardnup"))
        print("x: " + str(x))
        print("y: " + str(y))
        print("aim: " + str(aim))
        print(x * y)

nr2()
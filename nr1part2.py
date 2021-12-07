lines = open("depths.txt","r")
lijst= []
for line in lines:
    stripped_line = line.strip()
    lijst.append(int(stripped_line))

newlist = []
def make_new_list():
    for (ix, value) in enumerate(lijst):
        if ix == 1998:
            break
        newvalue = lijst[ix] + lijst[ix + 1] + lijst[ix + 2]
        newlist.append(newvalue)
    print(newlist)
    check_new_list()


def check_new_list():
    answer = 0
    for (ix, value) in enumerate(newlist):
        if value > newlist[ix -1]:
            answer += 1
    print(answer)

make_new_list()
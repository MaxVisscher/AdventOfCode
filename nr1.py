lines = open("depths.txt","r")
lijst= []
for line in lines:
    stripped_line = line.strip()
    lijst.append(int(stripped_line))


print(len(lijst))
answer = 0
for (ix, value) in enumerate(lijst):
    if value > lijst[ix -1]:
        answer += 1
print(answer)

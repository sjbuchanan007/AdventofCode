directions = open("aoc212a.txt","r").read().split('\n')
print (directions)

c = 0
i = 0
d = 0
h = 0
l = len(directions)

print (l)

for i in range (0, l):
    if directions[i][0] == "f":
        h += int(directions[i][-1])
    elif directions[i][0] == "d":
        d += int(directions[i][-1])
    elif directions[i][0] == "u":
        d -= int(directions[i][-1])
        
        

print (h)
print (d)
print (d*h)
        
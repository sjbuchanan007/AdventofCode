power = open("aoc213a.txt","r").read().split('\n')
print (power)

pl = len(power)
l = len(power[1])
pos = 0
ind = 0
countone = 0
countzero = 0
g = ""
e = ""

print (pl)
print (l)

for i in range (0,12):
    for x in range(0, pl-1):
        if power[ind][pos] == "1":
            countone += 1
            ind += 1
        else:
            countzero += 1
            ind += 1
    if int(countone) > int (countzero):
        g = g + "1"
        e = e + "0"
    else:
        g = g + "0"
        e = e + "1"
    ind = 0
    pos += 1
    countone = 0
    countzero = 0
    
print (g)
print (e)

gpos = 0
epos = 0
bin = 2048
ebin = 2048
gd = 0
ed = 0

for a in range (0,12):
    if g[gpos] == "1":
        gd += bin
        gpos += 1
        bin /= 2
    else:
        gpos += 1
        bin /= 2
        
print (gd)

for b in range (0,12):
    if e[epos] == "1":
        ed += ebin
        epos += 1
        ebin /= 2
    else:
        epos += 1
        ebin /= 2
        
print (ed)

print (ed * gd)

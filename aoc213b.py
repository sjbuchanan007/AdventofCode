lsro2 = open("aoc213a.txt","r").read().split('\n')
# print (lsro2)
lsrco2 = open("aoc213a.txt","r").read().split('\n')
# print (lsrco2)

plo = len(lsro2)
plc = len(lsrco2)
o2rem = []
o2one = []
o2zero = []
co2rem = []
co2one = []
co2zero = []

ind = 0
ind2 = 0
pos = 0
pos2 = 0
cpos = 0
cpos2 = 0
countone = 0
countzero = 0
cind = 0
cind2 = 0
ccountone = 0
ccountzero = 0


while plo >= 2:
    for x in range(0, plo):
        if lsro2[ind][pos] == "1":
            o2one.append(ind)
            countone += 1
            ind += 1
        else:
            o2zero.append(ind)
            countzero += 1
            ind += 1
    if int(countone) >= int (countzero):
        for a in reversed(o2zero):
            del lsro2[a]
    else:
        for a in reversed(o2one):
            del lsro2[a]
    ind = 0
    ind2 = 0
    pos += 1
    pos2 += 1
    countone = 0
    countzero = 0
    plo = len(lsro2)
    o2one = []
    o2zero = []

while plc >= 2:
    for y in range(0, plc):
        if lsrco2[cind][cpos] == "1":
            co2one.append(cind)
            ccountone += 1
            cind += 1
        else:
            co2zero.append(cind)
            ccountzero += 1
            cind += 1
    if int(ccountzero) <= int (ccountone):
        for a in reversed(co2one):
            del lsrco2[a]
    else:
        for a in reversed(co2zero):
            del lsrco2[a]
    cind = 0
    cind2 = 0
    cpos += 1
    cpos2 += 1
    ccountone = 0
    ccountzero = 0
    plc = len(lsrco2)
    co2one = []
    co2zero = []

print (lsro2)
print (lsrco2)

opos = 0
cpos = 0
bin = 2048
ebin = 2048
gd = 0
ed = 0

for c in range (0,12):
    if lsro2[0][opos] == "1":
        gd += bin
        opos += 1
        bin /= 2
    else:
        opos += 1
        bin /= 2
        
print (gd)

for d in range (0,12):
    if lsrco2[0][cpos] == "1":
        ed += ebin
        cpos += 1
        ebin /= 2
    else:
        cpos += 1
        ebin /= 2
        
print (ed)

print (ed * gd)

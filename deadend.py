#doodlopende paden bepalen
doodlopend = []
doodlopend_2 = []
j = 0
while j < level_breedte:
    doodlopend.append([])
    k = 0
    while k < level_hoogte:
        doodlopend[j].append(0)
        k += 1
    j += 1
    
def doodloopcheck(j,k):
    if doodlopend[j][k] == 0 and level[k][j] != '#':
        omgeving = [level[(k+1) % level_hoogte][j] , level[(k-1) % level_hoogte][j] , level[k][(j+1) % level_breedte] , level[k][(j-1) % level_breedte]]
        aantalhekjes = 0
        l=0
        while l < 4:
            if omgeving[l] == "#":
                aantalhekjes += 1
            l += 1
        if doodlopend[j-1][k] == [j-1,k]:
            aantalhekjes += 1
        if doodlopend[j][k-1] == [j,k-1]:
            aantalhekjes += 1
        if aantalhekjes >= 3:
            doodlopend[j][k] = [j,k]
            doodlopend_2.append([j,k])
            doodloopcheck(j-1,k)
            doodloopcheck(j,k-1)

j = 0
while j < level_breedte:
    k = 0
    while k < level_hoogte:
        doodloopcheck(j,k)
        k += 1
    j += 1
#doodlopende paden bepalen            
        
f.write("\n" )
f.write("Doodlopende vakjes:" + str(doodlopend_2))
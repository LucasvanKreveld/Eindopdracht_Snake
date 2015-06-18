#from anno import *

#simpele permanente doodlopende paden bepalen
doodlopend = []
doodlopend_permanent = []

def permanent_doodloopcheck_veld(j, k, level_breedte, level_hoogte, level, f):
    j = 0
    while j < level_breedte:
        doodlopend.append([])
        k = 0
        while k < level_hoogte:
            doodlopend[j].append(0)
            k += 1
        j += 1

    j = 0
    while j < level_breedte:
        k = 0
        while k < level_hoogte:
            permanent_doodloopcheck(j, k, level_breedte, level_hoogte, level)
            k += 1
        j += 1
          
    f.write("\n" )
    f.write("Permanent doodlopende vakjes:" + str(doodlopend_permanent))

def permanent_doodloopcheck(j, k, level_breedte, level_hoogte, level):
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
            doodlopend_permanent.append([j,k])
            permanent_doodloopcheck(j-1, k, level_breedte, level_hoogte, level)
            permanent_doodloopcheck(j, k-1, level_breedte, level_hoogte, level)



#simpele permanente doodlopende paden bepalen  




# momenteel doodlopende paden bepalen
doodlopend_momenteel_lijst = []
doodlopend_momenteel_weergave = []

def momenteel_doodloopcheck_veld(level_breedte, level_hoogte, level, positie, f): 
    j = 0
    while j < level_breedte:
        doodlopend_momenteel_lijst.append([])
        k = 0
        while k < level_hoogte:
            doodlopend_momenteel_lijst[j].append(0)
            k += 1
        j += 1
    
    j = 0
    while j < level_breedte:
        k = 0
        while k < level_hoogte:
            momenteel_doodloopcheck(j, k, level_hoogte, level_breedte, level, positie)
            k += 1
        j += 1
    
    f.write("\n" )
    f.write("Momenteel doodlopende vakjes:" + str(doodlopend_momenteel_weergave))
    

def momenteel_doodloopcheck(j, k, level_hoogte, level_breedte, level, positie):
    if doodlopend_momenteel_lijst[j][k] == 0 and (level[k][j] == "." or level[k][j] == "x"):
        omgeving_symbool = [level[(k+1) % level_hoogte][j] , level[(k-1) % level_hoogte][j] , level[k][(j+1) % level_breedte] , level[k][(j-1) % level_breedte]]
        omgeving_coordinaten = [[j,(k+1) % level_hoogte] , [j,(k-1) % level_hoogte] , [(j+1) % level_breedte,k] , [(j-1) % level_breedte,k]]
        aantal_obstakels = 0
        l=0
        while l < 4:
            if omgeving_symbool[l] != "." and omgeving_symbool[l] != "x" and omgeving_coordinaten[l] != str(positie):
                aantal_obstakels += 1
            l += 1
        if doodlopend_momenteel_lijst[(j-1) % level_breedte][k] == [j-1,k]:
            aantal_obstakels += 1
        if doodlopend_momenteel_lijst[j][(k-1) % level_hoogte] == [j,k-1]:
            aantal_obstakels += 1
        if doodlopend_momenteel_lijst[(j+1) % level_breedte][k] == [j+1,k]:
            aantal_obstakels += 1
        if doodlopend_momenteel_lijst[j][(k+1) % level_hoogte] == [j,k+1]:
            aantal_obstakels += 1
        if aantal_obstakels >= 3:
            doodlopend_momenteel_lijst[j][k] = [j,k]
            doodlopend_momenteel_weergave.append([j,k])
            momenteel_doodloopcheck(j-1, k, level_hoogte, level_breedte, level, positie)
            momenteel_doodloopcheck(j, k-1, level_hoogte, level_breedte, level, positie)
#momenteel doodlopende paden bepalen            



#lastige doodlopende paden bepalen

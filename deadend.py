#Code voor het bepalen van permanent doodlopende paden

doodlopend = []
doodlopend_permanent = []


def permanent_doodloopcheck_veld(j, k, level_breedte, level_hoogte, level, f):
    j = 0
    while j < level_breedte:
        doodlopend.append([])
        k = 0
        while k < level_hoogte:
            doodlopend[j].append(0)     #maak een lijst met nullen
            k += 1
        j += 1

    j = 0
    while j < level_breedte:
        k = 0
        while k < level_hoogte:
            permanent_doodloopcheck(j, k, level_breedte, level_hoogte, level) #check voor elk vakje of het doodloopt
            k += 1
        j += 1
          
    f.write("\n" )
    f.write("Permanent doodlopende vakjes:" + str(doodlopend_permanent)) #geef de permanent doodlopende vakjes weer in anno.txt

def permanent_doodloopcheck(j, k, level_breedte, level_hoogte, level): #check voor een vakje of het doodloopt
    if doodlopend[j][k] == 0 and level[k][j] != '#':
        omgeving = [level[(k+1) % level_hoogte][j] , level[(k-1) % level_hoogte][j] , level[k][(j+1) % level_breedte] , level[k][(j-1) % level_breedte]] #de vier vakjes eromheen
        aantalhekjes = 0
        l=0
        while l < 4:
            if omgeving[l] == "#":
                aantalhekjes += 1
            l += 1
        if doodlopend[(j-1) % level_breedte][k] == [(j-1) % level_breedte,k]:
            aantalhekjes += 1
        if doodlopend[j][(k-1) % level_hoogte] == [j,(k-1) % level_hoogte]:
            aantalhekjes += 1
        if doodlopend[(j+1) % level_breedte][k] == [(j+1) % level_breedte,k]:
            aantalhekjes += 1
        if doodlopend[j][(k+1) % level_hoogte] == [j,(k+1) % level_hoogte]:
            aantalhekjes += 1
        if aantalhekjes >= 3: #als er 3 of 4 hekjes of vakjes die doodlopend zijn omheen staan:
            doodlopend[j][k] = [j,k]
            doodlopend_permanent.append([j,k])
            permanent_doodloopcheck((j-1) % level_breedte, k, level_breedte, level_hoogte, level)
            permanent_doodloopcheck(j, (k-1) % level_hoogte, level_breedte, level_hoogte, level)
            permanent_doodloopcheck((j+1) % level_breedte, k, level_breedte, level_hoogte, level)
            permanent_doodloopcheck(j, (k+1) % level_hoogte, level_breedte, level_hoogte, level)
            

#simpele permanente doodlopende paden bepalen  






#momenteel doodlopende paden bepalen

doodlopend_momenteel_lijst = []
doodlopend_momenteel_weergave = []

def momenteel_doodloopcheck_veld(level_breedte, level_hoogte, level, positie, f): 
    doodlopend_momenteel_lijst = []
    doodlopend_momenteel_weergave = []
    j = 0
    while j < level_breedte:
        doodlopend_momenteel_lijst.append([])
        k = 0
        while k < level_hoogte:
            doodlopend_momenteel_lijst[j].append(0)     #maak een lijst met nullen
            k += 1
        j += 1
    
    j = 0
    while j < level_breedte:
        k = 0
        while k < level_hoogte:
            momenteel_doodloopcheck(j, k, level_hoogte, level_breedte, level, positie, f, doodlopend_momenteel_weergave, doodlopend_momenteel_lijst)    #check elk vakje op doodlopendheid
            k += 1
        j += 1
    
    f.write("\n" )
    f.write("Momenteel doodlopende vakjes:" + str(doodlopend_momenteel_weergave))   #geef de momenteel doodlopende vakjes weer in anno.txt
    

def momenteel_doodloopcheck(j, k, level_hoogte, level_breedte, level, positie, f, doodlopend_momenteel_weergave, doodlopend_momenteel_lijst):   #check voor elk vakje of het dood loopt
    a = doodlopend_momenteel_lijst
    b = doodlopend_momenteel_weergave
    
    if a[j][k] == 0 and (level[k][j] == "." or level[k][j] == "x"):
        
        omgeving_symbool = [level[(k+1) % level_hoogte][j] , level[(k-1) % level_hoogte][j] , level[k][(j+1) % level_breedte] , level[k][(j-1) % level_breedte]]    #de vier vakjes eromheen
        
        omgeving_coordinaten = [[j,(k+1) % level_hoogte] , [j,(k-1) % level_hoogte] , [(j+1) % level_breedte,k] , [(j-1) % level_breedte,k]]    #de coordinaten van die vakjes
        
        aantal_obstakels = 0
        l=0
        while l < 4:
            if omgeving_symbool[l] != "." and omgeving_symbool[l] != "x" and str(omgeving_coordinaten[l]) != str(positie):
                aantal_obstakels += 1
            l += 1
        if a[(j-1) % level_breedte][k] == [(j-1) % level_breedte,k]:
            aantal_obstakels += 1
        if a[j][(k-1) % level_hoogte] == [j,(k-1) % level_hoogte]:
            aantal_obstakels += 1
        if a[(j+1) % level_breedte][k] == [(j+1) % level_breedte,k]:
            aantal_obstakels += 1
        if a[j][(k+1) % level_hoogte] == [j,(k+1) % level_hoogte]:
            aantal_obstakels += 1
        
        if aantal_obstakels >= 3:   #als er om het vakje heen 3 of 4 vakjes een hekje, slang of doodlopend paadje zijn:
            a[j][k] = [j,k]
            b.append([j,k])
            momenteel_doodloopcheck((j-1) % level_breedte, k, level_hoogte, level_breedte, level, positie, f, doodlopend_momenteel_weergave, doodlopend_momenteel_lijst)
            momenteel_doodloopcheck(j, (k-1) % level_hoogte, level_hoogte, level_breedte, level, positie ,f, doodlopend_momenteel_weergave, doodlopend_momenteel_lijst)
            momenteel_doodloopcheck((j+1) % level_breedte, k, level_hoogte, level_breedte, level, positie, f, doodlopend_momenteel_weergave, doodlopend_momenteel_lijst)
            momenteel_doodloopcheck(j, (k+1) % level_hoogte, level_hoogte, level_breedte, level, positie ,f, doodlopend_momenteel_weergave, doodlopend_momenteel_lijst)
            
#momenteel doodlopende paden bepalen            
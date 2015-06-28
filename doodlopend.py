#Code voor het bepalen van permanent doodlopende paden

permanent_doodlopend_hulp = []
permanent_doodlopende_coordinaten = []

#functie die permanent doodlopende paden bepaalt
def permanent_doodloopcheck_level(j, k, level_breedte, level_hoogte, level, f): 
    j = 0
    while j < level_breedte:
        permanent_doodlopend_hulp.append([])
        k = 0
        while k < level_hoogte:
            permanent_doodlopend_hulp[j].append(0)     #maak een lijst met nullen
            k += 1
        j += 1

    j = 0
    while j < level_breedte:
        k = 0
        while k < level_hoogte:
            permanent_doodloopcheck_vakje(j, k, level_breedte, level_hoogte, level) #check voor elk vakje of het doodloopt
            k += 1
        j += 1
          
    return permanent_doodlopende_coordinaten

def permanent_doodloopcheck_vakje(j, k, level_breedte, level_hoogte, level): #check voor een vakje of het doodloopt
    if permanent_doodlopend_hulp[j][k] == 0 and level[k][j] != '#':
        
        aangrenzend = [level[(k+1) % level_hoogte][j] , level[(k-1) % level_hoogte][j] , level[k][(j+1) % level_breedte] , level[k][(j-1) % level_breedte]] #de vier vakjes eromheen
        
        aantal_hekjes = 0
        l = 0
        while l < 4:
            if aangrenzend[l] == "#":
                aantal_hekjes += 1
            l += 1
        if permanent_doodlopend_hulp[(j-1) % level_breedte][k] == [(j-1) % level_breedte,k]:
            aantal_hekjes += 1
        if permanent_doodlopend_hulp[j][(k-1) % level_hoogte] == [j,(k-1) % level_hoogte]:
            aantal_hekjes += 1
        if permanent_doodlopend_hulp[(j+1) % level_breedte][k] == [(j+1) % level_breedte,k]:
            aantal_hekjes += 1
        if permanent_doodlopend_hulp[j][(k+1) % level_hoogte] == [j,(k+1) % level_hoogte]:
            aantal_hekjes += 1
        if aantal_hekjes >= 3: #als er 3 of 4 hekjes of vakjes die doodlopend zijn omheen staan:
            permanent_doodlopend_hulp[j][k] = [j,k]
            permanent_doodlopende_coordinaten.append([j,k])
            permanent_doodloopcheck_vakje((j-1) % level_breedte, k, level_breedte, level_hoogte, level)
            permanent_doodloopcheck_vakje(j, (k-1) % level_hoogte, level_breedte, level_hoogte, level)
            permanent_doodloopcheck_vakje((j+1) % level_breedte, k, level_breedte, level_hoogte, level)
            permanent_doodloopcheck_vakje(j, (k+1) % level_hoogte, level_breedte, level_hoogte, level)
            
#simpele permanente doodlopende paden bepalen  






#momenteel doodlopende paden bepalen


#functie die momenteel doodlopende pade bepaalt
def momenteel_doodloopcheck_level(level_breedte, level_hoogte, level, positie, f): 
    momenteel_doodlopend_hulp = []
    momenteel_doodlopend_coordinaten = []
    
    j = 0
    while j < level_breedte:
        momenteel_doodlopend_hulp.append([])
        k = 0
        while k < level_hoogte:
            momenteel_doodlopend_hulp[j].append(0)     #maak een lijst met nullen
            k += 1
        j += 1
    
    j = 0
    while j < level_breedte:
        k = 0
        while k < level_hoogte:
            momenteel_doodloopcheck_vakje(j, k, level_hoogte, level_breedte, level, positie, f, momenteel_doodlopend_coordinaten, momenteel_doodlopend_hulp)    #check elk vakje op doodlopendheid
            k += 1
        j += 1
    
    return momenteel_doodlopend_coordinaten
    

def momenteel_doodloopcheck_vakje(j, k, level_hoogte, level_breedte, level, positie, f, momenteel_doodlopend_coordinaten, momenteel_doodlopend_hulp):   #check voor elk vakje of het dood loopt
  
    if momenteel_doodlopend_hulp[j][k] == 0 and (level[k][j] == "." or level[k][j] == "x"):
        
        aangrenzend_symbool = [level[(k+1) % level_hoogte][j] , level[(k-1) % level_hoogte][j] , level[k][(j+1) % level_breedte] , level[k][(j-1) % level_breedte]]    #de vier vakjes eromheen
        
        aangrenzend_coordinaten = [[j,(k+1) % level_hoogte] , [j,(k-1) % level_hoogte] , [(j+1) % level_breedte,k] , [(j-1) % level_breedte,k]]    #de coordinaten van die vakjes
        
        aantal_obstakels = 0
        l = 0
        while l < 4:
            if aangrenzend_symbool[l] != "." and aangrenzend_symbool[l] != "x" and str(aangrenzend_coordinaten[l]) != str(positie):
                aantal_obstakels += 1
            l += 1
        if momenteel_doodlopend_hulp[(j-1) % level_breedte][k] == [(j-1) % level_breedte,k]:
            aantal_obstakels += 1
        if momenteel_doodlopend_hulp[j][(k-1) % level_hoogte] == [j,(k-1) % level_hoogte]:
            aantal_obstakels += 1
        if momenteel_doodlopend_hulp[(j+1) % level_breedte][k] == [(j+1) % level_breedte,k]:
            aantal_obstakels += 1
        if momenteel_doodlopend_hulp[j][(k+1) % level_hoogte] == [j,(k+1) % level_hoogte]:
            aantal_obstakels += 1
        
        if aantal_obstakels >= 3:   #als er om het vakje heen 3 of 4 vakjes een hekje, slang of doodlopend paadje zijn:
            momenteel_doodlopend_hulp[j][k] = [j,k]
            momenteel_doodlopend_coordinaten.append([j,k])
            momenteel_doodloopcheck_vakje((j-1) % level_breedte, k, level_hoogte, level_breedte, level, positie, f, momenteel_doodlopend_coordinaten, momenteel_doodlopend_hulp)
            momenteel_doodloopcheck_vakje(j, (k-1) % level_hoogte, level_hoogte, level_breedte, level, positie ,f, momenteel_doodlopend_coordinaten, momenteel_doodlopend_hulp)
            momenteel_doodloopcheck_vakje((j+1) % level_breedte, k, level_hoogte, level_breedte, level, positie, f, momenteel_doodlopend_coordinaten, momenteel_doodlopend_hulp)
            momenteel_doodloopcheck_vakje(j, (k+1) % level_hoogte, level_hoogte, level_breedte, level, positie ,f, momenteel_doodlopend_coordinaten, momenteel_doodlopend_hulp)
            
#momenteel doodlopende paden bepalen            
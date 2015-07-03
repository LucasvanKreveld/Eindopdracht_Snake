#Code voor het bepalen van permanent doodlopende paden
import copy

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

#potentieel doodlopende paden

def potentieel_doodlopend(level_hoogte, level_breedte, level, levelcheck, Area, speler_nummer):
    potentieel_doodlopende_vakjes = []
    j = 0
    while j < level_breedte:
        k = 0
        while k < level_hoogte:
            if levelcheck([j,k]) == '.' or levelcheck([j,k]) == 'x':
                area = Area(j, k)
                areasigns = []
                q = 0
                while q < len(area):
                    areasigns.append(levelcheck(area[q]))
                    q += 1
                if areasigns.count('x') + areasigns.count('.') + areasigns.count(str(speler_nummer)) == 2:
                    potentieel_doodlopende_vakjes.append([j, k])
            k += 1
        j += 1
    return potentieel_doodlopende_vakjes
    
def potentieel_doodlopende_gang_check(x, y, z, w, level, levelcheck, al_gehad, speler_nummer, afstand, kortstepadzoeker, slanghoofden, level_hoogte, level_breedte, Area, potentieel_doodlopende_vakjes, f):
    if [x,y] in al_gehad:
        al_gehad = []
        return 'geen gevaar'
        
    al_gehad.append([x,y])
    if [x,y] in potentieel_doodlopende_vakjes:
        f.write("\n")
        f.write(str([x,y]) + " zit in potentieel_doodlopende_vakjes")
        hallpiece = Area(x, y)
        uitweg = copy.deepcopy(hallpiece)
        for i in range(0, len(hallpiece)):
            if levelcheck(hallpiece[i]) == '#' or hallpiece[i] == [z,w]:
                uitweg.remove(hallpiece[i])
        if uitweg[0] in potentieel_doodlopende_vakjes:
            f.write("\n")
            f.write("De gang gaat verder... ")
            return potentieel_doodlopende_gang_check(uitweg[0][0], uitweg[0][1], x, y, level, levelcheck, al_gehad, speler_nummer, afstand, kortstepadzoeker, slanghoofden, level_hoogte, level_breedte, Area, potentieel_doodlopende_vakjes, f)
        else:
            f.write("\n")
            f.write("We zijn bij het einde van de gang, nu zoeken we naar vijanden.")
            return gevaarchecker(uitweg[0][0], uitweg[0][1], x, y, level, level_hoogte, level_breedte, levelcheck, speler_nummer, afstand, kortstepadzoeker, slanghoofden, al_gehad, f)
    else:
        al_gehad = []
        return 'geen gevaar'
            
def gevaarchecker(x, y, z, w, level, level_hoogte, level_breedte, levelcheck, speler_nummer, afstand, kortstepadzoeker, slanghoofden, al_gehad, f):
    vijandenafstanden = []
    vijandencoordinaten = []
    j = 0
    while j < level_breedte:
        k = 0
        while k < level_hoogte:
            if [j, k] in slanghoofden and levelcheck([j,k]) != str(speler_nummer) and afstand(x, y, j, k) < len(al_gehad) + 1:
                vijandencoordinaten.append([j,k])
                vijandenafstanden.append(afstand(x, y, j, k))
            k += 1
        j += 1
    
    gevarenpad = 'geen directe paden'
    
    while len(vijandenafstanden) > 0:
        j = vijandenafstanden.index(min(vijandenafstanden))
        f.write("\n")
        f.write("\n")
        f.write("We bekijken speler " + str(j) + ". De afstand tussen hem en " + str([x,y]) + " is " + str(vijandenafstanden[j]) + ".")
        gevarenpad = kortstepadzoeker(x, y, slanghoofden[j][0], slanghoofden[j][1])
        f.write("\n")
        f.write("gevarenpad is " + str(gevarenpad))
        if gevarenpad == 'geen directe paden':
            vijandencoordinaten.remove(vijandencoordinaten[j])
            vijandenafstanden.remove(vijandenafstanden[j])
        else:
            f.write("\n")
            f.write("Dit is gevaarlijk!")
            break
    
    if gevarenpad == 'geen directe paden':
        al_gehad = []
        f.write("\n")
        f.write("geen gevaar")
        return 'geen gevaar'
    
    else:
        al_gehad = []
        return len(gevarenpad)
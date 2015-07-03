#!/bin/python
import random
import copy
from doodlopend import *
import sys
import math
import time

tijd = 0.1

###Initialisatie
# We lezen het doolhof en posities in

level_hoogte = int(input())         #Lees hoe groot het level is
level_breedte = int(input())

level = []                          #Lees het level regel voor regel
for y in range(level_hoogte):
    level.append(list(input()))

aantal_spelers = int(input())       #Lees het aantal spelers en hun posities
begin_posities = []
for i in range(aantal_spelers):
    begin_positie = [int(s) for s in input().split()]   #Maak lijst met x en y
    begin_posities.append(begin_positie)      #Voeg dit coordinaat toe aan begin_posities

speler_nummer = int(input())        #Lees welk spelernummer wij zijn

###De tijdstap


# deze lijst houdt bij hoeveel punten elke speler heeft
scores = []
j = 0
while j < aantal_spelers:
    scores.append(0)
    j += 1

#deze lijst houdt voor elke beurt, voor elke speler bij waar elk stukje van zijn staart is.
#het is een lijst met voor elke beurt een nieuwe lijst met voor elke speler een nieuwe lijst met coordinaten van alle stukjes van de slang.
spelercoordinaten = [[]]

k = 0
j = 0
while j < aantal_spelers:
    spelercoordinaten[0].append([copy.deepcopy(begin_posities[j])])
    j += 1
#snap de posities van de spelers
#hou bij hoe lang elke snake is
lengtes = []
j = 1
while j <= aantal_spelers:
    lengtes.append(1)
    j += 1
#hou bij hoe lang elke snake is/

dode_spelers = []

#doodlopende paden bepalen
permanent_doodlopend_hulp = []
permanent_doodlopende_coordinaten = []
permanent_doodlopende_coordinaten = permanent_doodloopcheck_level(j, k, level_breedte, level_hoogte, level)


def levelcheck(x):
    return level[x[1]][x[0]]


# kortstepad
def permuteer(a, b, d, e, x0, y0, horizontaal, verticaal):
    c = a + b
    comp = []
    
    j = 0
    while j < c:
        comp.append(0)
        j += 1
        
    j = 0
    while j < a:
        i = random.randrange(c)
        while comp[i] == d:
            i = random.randrange(c)
        comp[i] = d
        j += 1
        
    j = 0
    while j < c:
        if comp[j] != d:
            comp[j] = e
        j += 1
        
    j = 0
    while j < c:
        if comp[j] == d:
            x0 += (horizontaal)
        else:
            y0 += (verticaal)
        comp[j] = [int(x0%level_breedte), int(y0%level_hoogte)]
        j += 1
    return comp

def kortstepadzoeker(x1, y1, x2, y2, T1):
    # if afstand(x1, y1, x2, y2) > 6:
    #     return 'geen directe paden'
    blabla = []
    bla = copy.deepcopy(kortstepadzoekerhulp(x1, y1, x2, y2, -1, -1, T1))
    if bla != 'geen directe paden':
        blabla.append(copy.deepcopy(bla))
    
    bla = copy.deepcopy(kortstepadzoekerhulp(x1, y1, x2, y2, -1, 1, T1))
    if bla != 'geen directe paden':
        blabla.append(copy.deepcopy(bla))
    
    bla = copy.deepcopy(kortstepadzoekerhulp(x1, y1, x2, y2, 1, 1, T1))
    if bla != 'geen directe paden':
        blabla.append(copy.deepcopy(bla))
    
    bla = copy.deepcopy(kortstepadzoekerhulp(x1, y1, x2, y2, 1, -1, T1))
    if bla != 'geen directe paden':
        blabla.append(copy.deepcopy(bla))
    
    if len(blabla) == 0:
        return 'geen directe paden'
    
    else:
        blablo = []
        i = 0
        while i < len(blabla):
            blablo.append(len(blabla[i]))
            i += 1
    
        j = blablo.index(min(blablo))
        return blabla[j]
    
    
def kortstepadzoekerhulp(x1, y1, x2, y2, horizontaal, verticaal, T1):

    x0 = copy.deepcopy(x1)
    y0 = copy.deepcopy(y1)
    paden = []
    m = 0
    u = 0
    q = 0
    n = 100
    while u < n:
        T2 = time.perf_counter()
        if T2 - T1 >= tijd:
            return 'geen directe paden'
        pad = permuteer(abs(x1 - x2), abs(y1 - y2), 'd', 'e', x0, y0, horizontaal, verticaal)
        o = 0
        while pad in paden:
            o += 1
            pad = permuteer(abs(x1 - x2), abs(y1 - y2), 'd', 'e', x0, y0, horizontaal, verticaal)
            if o > 100:
                q = 1
                break
        if q == 1:
            pad = 'geen directe paden'
            break
        paden.append(copy.deepcopy(pad))
        i = 0
        h = 0
        while i < len(pad):
            if levelcheck(pad[i]) != '.' and levelcheck(pad[i]) != 'x':
                h = 1
                break
            i += 1
        if h == 1:
            u += 1
        else:
            m = 1
            break
    
    if m == 0:
        pad = 'geen directe paden'
    
    return pad

# kortstepad/

# Dit programma levert de coördinaat voor de slang waar hij de volgende beurt het beste naar toe kan gaan.
# Area is de functie die het gebied van 3x3 bepaalt met als middelpunt [x,y].
def Area(x,y):
    area=[]
    area.append([(x-1) % level_breedte , y])
    area.append([x , (y-1) % level_hoogte])
    area.append([x , (y+1) % level_hoogte])
    area.append([(x+1) % level_breedte , y])
    return area

# muur_check is de functie die bepaalt of een bepaalde coördinaat toegangbaar is.       
def muur_check(x,y):
    if level[y][x] != "." and level[y][x] != "x" and [x,y] not in achterwerken:
        return -100000
    if level[y][x] != "." and level[y][x] != "x" and [x,y] in achterwerken:
        return -50000
    elif [x,y] in permanent_doodlopende_coordinaten and lengtes[speler_nummer] > 1:
        return -10000
    elif [x,y] in momenteel_doodloopcheck_level(level_breedte, level_hoogte, level, spelercoordinaten[tijdstap][speler_nummer][0]) and lengtes[speler_nummer] > 1:
        return -1000
    else:
        return 0
        
# eten_check is de functie die gaat kijken of een coördinaat eten bevat of niet. We willen namelijk dat de slang zolang mogelijk van het eten afblijft.
def eten_check(x,y):
    if level[y][x] == ".":
        if eetmodus == 0:
            return 10
        else:
            return 0
    if level[y][x] == 'x':
        if eetmodus == 1:
            return 10
        else:
            return 0
    else:
        return 0
            
# vrije_coordinaten_check is de functie die de hoeveelheid vrije coördinaten rond een bepaald punt bepaalt.
def vrije_coordinaten_check(x,y):
    area = Area(x,y)
    Mark = 0
    for i in range(0,len(area)):
        if level[area[i][1]][area[i][0]] == "." and eetmodus == 0:
            Mark += 2
        elif level[area[i][1]][area[i][0]] == "x" and eetmodus == 0:
            Mark += 1
        elif level[area[i][1]][area[i][0]] == "." and eetmodus == 1:
            Mark += 1
        elif level[area[i][1]][area[i][0]] == "x" and eetmodus == 1:
            Mark += 2
        elif area[i] in slanghoofden:
            if scores[int(levelcheck(area[i]))] <= scores[speler_nummer]:
                Mark -= 100
        
        if level[area[i][1]][area[i][0]] == "." or level[area[i][1]][area[i][0]] == "x":
            karea = Area(area[i][0], area[i][1])
            karea.remove([x,y])
            for j in range(0, len(karea)):
                if karea[j] in slanghoofden and str(levelcheck(karea[j])) != str(speler_nummer):
                    Mark -= 100
            
    return Mark

al_gehad = []

def potentieel_doodlopend_check(x, y):
    if (levelcheck([x,y]) == '.' or levelcheck([x,y]) == 'x') and lengtes[speler_nummer] > 1:
        area = Area(x, y)
        areasigns = []
        for i in range(0, len(area)):
            areasigns.append(levelcheck(area[i]))
        if areasigns.count('.') + areasigns.count('x') + areasigns.count(str(speler_nummer)) == 2:
            al_gehad = []
            potentieel_doodlopende_vakjes = potentieel_doodlopend(level_hoogte, level_breedte, level, levelcheck, Area, speler_nummer)
            pot = potentieel_doodlopende_gang_check(x, y, spelercoordinaten[tijdstap][speler_nummer][0][0], spelercoordinaten[tijdstap][speler_nummer][0][1], level, levelcheck, al_gehad, speler_nummer, afstand, kortstepadzoeker, slanghoofden, level_hoogte, level_breedte, Area, potentieel_doodlopende_vakjes)
            if pot != 'geen gevaar':
                return -100
            else:
                return -2
        else:
            return 0
    else:
        return 0
                        
        

def doodlopend_lengte_check(L, Freespaces):
    checklist = []
    for i in range(0,len(L)):
        if level[L[i][1]][L[i][0]] == "." or level[L[i][1]][L[i][0]] == "x":
            area = Area(L[i][0] , L[i][1])
            for j in range(0,len(area)):
                if level[area[j][1]][area[j][0]]=="." or level[area[j][1]][area[j][0]]=="x":
                    if area[j] not in checklist and area[j] not in Freespaces and area[j] not in L:
                        checklist.append(area[j])
    new = []
    for i in range(0,len(checklist)):
        if checklist[i] not in Freespaces:
            new.append(checklist[i])
    if new != []:
        for i in range(0,len(new)):
            Freespaces.append(new[i])
        getal = doodlopend_lengte_check(new,Freespaces)
        
        return getal
    else:
        getal = int(len(Freespaces))
        return getal
   
# kortstepad_check checkt of een coordinaat onderdeel is van een kortste pad
def kortstepad_check(x, y, z, w, kortpad):

    if kortpad == 'geen directe paden':
        return 0
    if eetmodus == 0:
        return 0
    if [z,w] != kortpad[0]:
        return 0
    else:
        return 5

        
# beste_zet is de functie die aan de hand van de bovenstaande functies de coördinaat bepaald waar de slang de volgende beurt naar toe moet gaan.
def beste_zet(x, y):
    
    etenscoordinaten = []
    j = 0
    while j < level_hoogte:
        k = 0
        while k < level_breedte:
            if level[j][k] == 'x':
                if [k,j] not in momenteel_doodlopend_coordinaten:
                    if afstand(spelercoordinaten[tijdstap][speler_nummer][0][0], spelercoordinaten[tijdstap][speler_nummer][0][1], k, j) < 10:
                        if len(etenscoordinaten) < 5:
                            etenscoordinaten.append([k,j])
            k += 1
        j += 1

    etensafstanden = []
    if len(etenscoordinaten) > 0:
        j = 0
        while j < len(etenscoordinaten):
            etensafstanden.append(afstand(spelercoordinaten[tijdstap][speler_nummer][0][0], spelercoordinaten[tijdstap][speler_nummer][0][1], etenscoordinaten[j][0], etenscoordinaten[j][1]))
            j += 1
    
    
    kortpad = 'geen directe paden'
    while len(etensafstanden) > 0:
        T1 = time.perf_counter()
        j = etensafstanden.index(min(etensafstanden))
        kortpad = kortstepadzoeker(x, y, etenscoordinaten[j][0], etenscoordinaten[j][1], T1)
        if kortpad == 'geen directe paden':
            etenscoordinaten.remove(etenscoordinaten[j])
            etensafstanden.remove(etensafstanden[j])
        else:
            etensafstanden = []
    
    
    area = Area(x, y)
    rating = []
    for i in range(0,len(area)):
        X=doodlopend_lengte_check([[area[i][0] , area[i][1]]] , [[area[i][0] , area[i][1]]])
        Mark = muur_check(area[i][0], area[i][1]) + eten_check(area[i][0], area[i][1]) + vrije_coordinaten_check(area[i][0], area[i][1]) + 10*X + kortstepad_check(x, y, area[i][0], area[i][1], kortpad) + potentieel_doodlopend_check(area[i][0], area[i][1])
        rating.append(Mark)
    maxelement = max(rating)
    return(area[rating.index(maxelement)])

#prioriteiten/

#functie die afstand tussen twee punten berekent
def afstand(x1, y1, x2, y2):
    
    dx = min(abs(x1 - x2), abs(x1 - x2 + level_breedte))
    dy = min(abs(y1 - y2), abs(y1 - y2 + level_hoogte))
    dz = dx + dy
    return dz
#functie die afstand tussen twee punten berekent\


eetmodus = 0
tijdstap = -1
while True:
    tijdstap += 1
    
    j = 0
    while j < aantal_spelers:
        if j not in dode_spelers:
            scores[j] = tijdstap + lengtes[j]*100 + len(dode_spelers)*1000
        j += 1
    
    if eetmodus == 0 and lengtes[speler_nummer] > 1:
        eetmodus = 1
    
    slanghoofden = []
    j = 0
    while j < aantal_spelers:
        if j not in dode_spelers:
            slanghoofden.append(spelercoordinaten[tijdstap][j][0])
        j += 1
    
    achterwerken = []
    j = 0
    while j < aantal_spelers:
        achterwerken.append(spelercoordinaten[tijdstap][j][-1])
        j += 1
    

    #check de frequentie waarin voedsel verschijnt
    if tijdstap == 10:
        hoeveelheid_eten = 0   
        x = 0
        while x < level_breedte:
            y = 0
            while y < level_hoogte:
                if level[y][x] == "x":
                    hoeveelheid_eten += 1
                y += 1
            x += 1
        
        a = 0
        while a < aantal_spelers:
            eten_gepakt = lengtes[a] - 1
            a += 1
        hoeveelheid_eten += eten_gepakt
        
        eten_frequentie = (float(hoeveelheid_eten)*10) / (aantal_spelers*level_hoogte*level_breedte)
        
        if eten_frequentie < 0.05:
            eetmodus = 1
    
    #scan voor deze beurt of er doodlopende paadjes zijn die eventueel door slangen zijn gemaakt
    momenteel_doodlopend_hulp = []
    momenteel_doodlopend_coordinaten = []
    momenteel_doodloopcheck_level(level_breedte, level_hoogte, level, spelercoordinaten[tijdstap][speler_nummer][0])

    # dit stukje bepaalt aan de hand van de beste_zet functie welke richting we op gaan
    doelcoordinaat = beste_zet(spelercoordinaten[tijdstap][speler_nummer][0][0], spelercoordinaten[tijdstap][speler_nummer][0][1])
    if doelcoordinaat[0] == (spelercoordinaten[tijdstap][speler_nummer][0][0] + 1)% level_breedte:
        richting = 'r'
    elif doelcoordinaat[0] == (spelercoordinaten[tijdstap][speler_nummer][0][0] - 1)% level_breedte:
        richting = 'l'
    elif doelcoordinaat[1] == (spelercoordinaten[tijdstap][speler_nummer][0][1] + 1)% level_hoogte:
        richting = 'd'
    else:
        richting = 'u'
    
    print('move')                   #Geef door dat we gaan bewegen
    print(richting)                 #Geef de richting door

    line = input()                  #Lees nieuwe informatie

    if line == "":
        line = input()
    
    if line == "quit":              #We krijgen dit door als het spel is afgelopen
        print("bye")                #Geef door dat we dit begrepen hebben
        break

    speler_bewegingen = line        #String met bewegingen van alle spelers
                                    #Nu is speler_bewegingen[i] de richting waarin speler i beweegt
    
    #dit stukje van de code updatet de lijst spelercoordinaten door een de informatie van de posities van de volgende beurt toe te voegen
    spelercoordinaten.append([])
    j = 0
    while j < aantal_spelers:
        spelercoordinaten[tijdstap + 1].append([])
        k = 1
        while k <= lengtes[j]:
            spelercoordinaten[tijdstap + 1][j].append([0,0])
            k += 1
        j += 1
    
    #hier komt informatie over de nieuwe spelercoordinaten van de spelers
    j = 0
    while j < aantal_spelers:
        level[spelercoordinaten[tijdstap][j][0][1]][spelercoordinaten[tijdstap][j][0][0]] = '.'
        if speler_bewegingen[j] == 'u':
            spelercoordinaten[tijdstap + 1][j][0] = [spelercoordinaten[tijdstap][j][0][0], (spelercoordinaten[tijdstap][j][0][1] - 1 + level_hoogte)% level_hoogte]
        elif speler_bewegingen[j] == 'd':
            spelercoordinaten[tijdstap + 1][j][0] = [spelercoordinaten[tijdstap][j][0][0], (spelercoordinaten[tijdstap][j][0][1] + 1 + level_hoogte)% level_hoogte]
        elif speler_bewegingen[j] == 'l':
            spelercoordinaten[tijdstap + 1][j][0] = [(spelercoordinaten[tijdstap][j][0][0] - 1 + level_breedte)%level_breedte, spelercoordinaten[tijdstap][j][0][1]]
        elif speler_bewegingen[j] == 'r':
            spelercoordinaten[tijdstap + 1][j][0] = [(spelercoordinaten[tijdstap][j][0][0] +  1 + level_breedte)%level_breedte, spelercoordinaten[tijdstap][j][0][1]]
        else:
            spelercoordinaten[tijdstap + 1][j][0] = copy.deepcopy(spelercoordinaten[tijdstap][j][0])
            dode_spelers.append(j)
        
        #hier gaan we herkennen of speler j eten pakt
        if level[spelercoordinaten[tijdstap + 1][j][0][1]][spelercoordinaten[tijdstap + 1][j][0][0]] == "x":
            lengtes[j] += 1
            spelercoordinaten[tijdstap + 1][j].append([0,0])
        #hier gaan we herkennen wie er eten pakt/
        
        #hier zorgen we dat de dode slangen niet in de muur terecht komen
        if not (level[spelercoordinaten[tijdstap + 1][j][0][1]][spelercoordinaten[tijdstap + 1][j][0][0]] == "x" or level[spelercoordinaten[tijdstap + 1][j][0][1]][spelercoordinaten[tijdstap + 1][j][0][0]] == "."):
            if levelcheck(spelercoordinaten[tijdstap + 1][j][0]) == '#':
                spelercoordinaten[tijdstap + 1][j][0] = copy.deepcopy(spelercoordinaten[tijdstap][j][0])
            else:
                l = 0
                k = 0
                while k < aantal_spelers:
                    if k == speler_nummer or k in dode_spelers:
                        k += 1
                    else:
                        if spelercoordinaten[tijdstap + 1][j][0] == spelercoordinaten[tijdstap + 1][k][0]:
                            if scores[j] < scores[k]:
                                k += 1
                            elif scores[j] == scores[k]:
                                if int(j) < int(k):
                                    k += 1
                                else:
                                    spelercoordinaten[tijdstap + 1][j][0] = copy.deepcopy(spelercoordinaten[tijdstap][j][0])
                                    k += 1
                            else:
                                spelercoordinaten[tijdstap + 1][j][0] = copy.deepcopy(spelercoordinaten[tijdstap][j][0])
                                k += 1
                        elif levelcheck(spelercoordinaten[tijdstap + 1][j][0]) == str(k):
                            spelercoordinaten[tijdstap + 1][j][0] = copy.deepcopy(spelercoordinaten[tijdstap][j][0])
                            k += 1
                        else:
                            k += 1
        #hier zorgen we dat de dode slangen niet in de muur terecht komen/
        
        if spelercoordinaten[tijdstap + 1][j][0] == spelercoordinaten[tijdstap][j][0]:
            u = 2
            while u <= lengtes[j]:
                spelercoordinaten[tijdstap + 1][j][u - 1] = copy.deepcopy(spelercoordinaten[tijdstap][j][u - 1])
                u += 1
        else:
            u = 2
            while u <= lengtes[j]:
                spelercoordinaten[tijdstap + 1][j][u - 1] = copy.deepcopy(spelercoordinaten[tijdstap][j][u - 2])
                u += 1
        
        h = 0
        while h < level_hoogte:
            b = 0 
            while b < level_breedte:
                if [b,h] in spelercoordinaten[tijdstap][j]:
                    level[h][b] = "."
                if [b,h] in spelercoordinaten[tijdstap + 1][j]:
                    level[h][b] = str(j)
                b += 1
            h += 1
        j += 1
    #hier komt informatie over de nieuwe spelercoordinaten van de spelers/
    
    aantal_voedsel = int(input())   #Lees aantal nieuw voedsel en spelercoordinaten
    voedsel_spelercoordinaten = []
    for i in range(aantal_voedsel):
        voedsel_positie = [int(s) for s in input().split()]
        # Sla de voedsel positie op in een lijst en in het level
        voedsel_spelercoordinaten.append(voedsel_positie)
        level[voedsel_positie[1]][voedsel_positie[0]] = "x"
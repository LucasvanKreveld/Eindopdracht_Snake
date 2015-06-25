#!/bin/python
import random
import copy
from deadend import *
import sys


f = open("annopriori.txt", 'w')

###Initialisatie
# We lezen het doolhof en beginposities in

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

# We beginnen op de volgende positie:
positie = begin_posities[speler_nummer]

#snap de posities van de spelers
posities = [[]]

j = 0
while j < aantal_spelers:
    posities[0].append([copy.deepcopy(begin_posities[j])])
    j += 1
#snap de posities van de spelers

f.write("Ik ben speler " + str(speler_nummer))
f.write("\n")
    
# u=up, d=down, l=left, r=right
# dx en dy geven aan in welke richting 'u', 'r', 'd' en 'l' zijn:
dx = [ 0, 1, 0,-1]
dy = [-1, 0, 1, 0]

#herken de hekjes en zet ze in een lijst
gevarenzone = []

j = 0
while j < level_breedte:
    k = 0
    while k < level_hoogte:
        if level[k][j] == '#':
            gevarenzone.append([j,k])
        k += 1
    j += 1
#herken de hekjes en zet ze in een lijst/

#hou bij hoe lang elke snake is
lengtes = []
j = 1
while j <= aantal_spelers:
    lengtes.append(1)
    j += 1
#hou bij elke lang elke snake is/

f.write("De gevaarlijke coördinaten zijn: " + str(gevarenzone))

#doodlopende paden bepalen
doodlopend = []
doodlopend_permanent = []
permanent_doodloopcheck_veld(j, k, level_breedte, level_hoogte, level, f)

# Dit programma levert de coördinaat voor de slang waar hij de volgende beurt het beste naar toe kan gaan.
# Area is de functie die het gebied van 3x3 bepaalt met als middelpunt [x,y].
def Area(x,y):
    area=[]
    area.append([(x-1) % level_breedte , y])
    area.append([x , (y-1) % level_hoogte])
    area.append([x , (y+1) % level_hoogte])
    area.append([(x+1) % level_breedte , y])
    return area

# Check1 is de functie die bepaalt of een bepaalde coördinaat toegangbaar is.       
def Check1(x,y):
    if level[y][x] != "." and level[y][x] != "x" :
        return -10000
    elif [x,y] in doodlopend_permanent:
        return -1000
    elif [x,y] in momenteel_doodloopcheck_veld(level_breedte, level_hoogte, level, positie, f):
        return -100
    else:
        return 0
        
# Check2 is de functie die gaat kijken of een coördinaat eten bevat of niet. We willen namelijk dat de slang zolang mogelijk van het eten afblijft.
def Check2(x,y):
    if level[y][x] == ".":
        if lengtes[speler_nummer] == 1:
            return 100
        else:
            return 0
    else:
        return 0
            
# Check3 is de functie die de hoeveelheid vrije coördinaten rond een bepaald punt bepaalt.
def Check3(x,y):
    area = Area(x,y)
    Mark = 0
    for i in range(0,len(area)):
        if level[area[i][1]][area[i][0]] == ".":
            Mark += 2
        elif level[area[i][1]][area[i][0]] == "x":
            Mark += 1
    return Mark

def Check4(L,Freespaces):
    checklist = []
    for i in range(0,len(L)):
        area = Area(L[i][0] , L[i][1])
        for j in range(0,len(area)):
            if level[area[j][1]][area[j][0]]=='.' or level[area[j][1]][area[j][0]]=='x':
                checklist.append(area[j])
    D=L.intersect(checklist)
    checklist.remove(D)
    if checklist == []:
        return len(Freespaces)
    else:
        Freespaces.append(checklist)
        Check4(checklist)
    
# Prior is de functie die aan de hand van de bovenstaande functies de coördinaat bepaald waar de slang de volgende beurt naar toe moet gaan.
def Prior(x,y):
    area = Area(x,y)
    rating = []
    for i in range(0,len(area)):
        Mark = Check1(area[i][0] , area[i][1]) + Check2(area[i][0] , area[i][1]) + Check3(area[i][0] , area[i][1]) + Check4([[area[i][0] , area[i][1]]],[])
        rating.append(Mark)
    maxelement = max(rating)
    return(area[rating.index(maxelement)])

#prioriteiten/


eetmodus = 0
turn = -1
while True:
    
    turn += 1
    
    f.write("\n \n")
    f.write("Beurt " + str(turn) + ":")
    
    f.write("\n")
    j = 0
    while j < level_hoogte:
        k = 0
        while k < level_breedte:
            if [k, j] == posities[turn][speler_nummer][0]:
                f.write("m")
            else:
                f.write(str(level[j][k]))
            k += 1
        f.write("\n")
        j += 1
    
    j = 0
    while j < aantal_spelers:
        f.write("\n")
        f.write("De lengte van speler " + str(j) + " is " + str(lengtes[j]))
        j += 1
       
    f.write("\n")
    f.write("De posities zijn " + str(posities[turn]) + ", mijn positie is " + str(positie))
    
    #scan voor deze beurt of er doodlopende paadjes zijn die eventueel door slangen zijn gemaakt
    doodlopend_momenteel_lijst = []
    doodlopend_momenteel_weergave = []
    momenteel_doodloopcheck_veld(level_breedte, level_hoogte, level, positie, f)
    
    f.write("\n")
    f.write("doodlopend_momenteel_lijst is " + str(momenteel_doodloopcheck_veld(level_breedte, level_hoogte, level, positie, f)))
        

    
    doelcoordinaat = Prior(posities[turn][speler_nummer][0][0], posities[turn][speler_nummer][0][1])
    if doelcoordinaat[0] == (posities[turn][speler_nummer][0][0] + 1)% level_breedte:
        richting = 'r'
    elif doelcoordinaat[0] == (posities[turn][speler_nummer][0][0] - 1)% level_breedte:
        richting = 'l'
    elif doelcoordinaat[1] == (posities[turn][speler_nummer][0][1] + 1)% level_hoogte:
        richting = 'd'
    else:
        richting = 'u'
    
    f.write("\n")
    f.write("Ik ga naar " +str(richting) + " dus naar " + str(doelcoordinaat))

    positie[0] = doelcoordinaat[0]
    positie[1] = doelcoordinaat[1]
    
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

    f.write("\n")
    f.write("Speler bewegingen zijn: " + str(speler_bewegingen))
    
    posities.append([])
    j = 0
    while j < aantal_spelers:
        posities[turn + 1].append([])
        k = 1
        f.write("\n")
        f.write("De lengte van speler " + str(j) + " is "+ str(lengtes[j]) + " dus ")
        while k <= lengtes[j]:
            f.write("voeg [0,0] nummer " + str(k) + " toe ") 
            posities[turn + 1][j].append([0,0])
            k += 1
        f.write("\n")
        f.write("De lijst met coordinaten van speler " + str(j) + " is: " + str(posities[turn + 1][j]))
        j += 1
    
    #hier komt informatie over de nieuwe posities van de spelers
    j = 0
    while j < aantal_spelers:
        level[posities[turn][j][0][1]][posities[turn][j][0][0]] = '.'
        if speler_bewegingen[j] == 'u':
            posities[turn + 1][j][0] = [posities[turn][j][0][0], (posities[turn][j][0][1] - 1 + level_hoogte)% level_hoogte]
            f.write("\n")
            f.write("Speler " + str(j) + " beweegt omhoog van " + str(posities[turn][j][0]) + " naar " + str(posities[turn + 1][j][0]) + ".")
        elif speler_bewegingen[j] == 'd':
            posities[turn + 1][j][0] = [posities[turn][j][0][0], (posities[turn][j][0][1] + 1 + level_hoogte)% level_hoogte]
            f.write("\n")
            f.write("Speler " + str(j) + " beweegt omlaag van " + str(posities[turn][j][0]) + " naar " + str(posities[turn + 1][j][0]) + ".")
        elif speler_bewegingen[j] == 'l':
            posities[turn + 1][j][0] = [(posities[turn][j][0][0] - 1 + level_breedte)%level_breedte, posities[turn][j][0][1]]
            f.write("\n")
            f.write("Speler " + str(j) + " beweegt naar links van " + str(posities[turn][j][0]) + " naar " + str(posities[turn + 1][j][0]) + ".")
        elif speler_bewegingen[j] == 'r':
            posities[turn + 1][j][0] = [(posities[turn][j][0][0] +  1 + level_breedte)%level_breedte, posities[turn][j][0][1]]
            f.write("\n")
            f.write("Speler " + str(j) + " beweegt naar rechts van " + str(posities[turn][j][0]) + " naar " + str(posities[turn + 1][j][0]) + ".")
        else:
            posities[turn + 1][j][0] = copy.deepcopy(posities[turn][j][0])
        
        #hier gaan we herkennen of speler j eten pakt
        f.write("\n")
        f.write("De volgende positie van speler " + str(j) + " is " + str(posities[turn + 1][j][0]) + " en dat is een " + str(level[posities[turn + 1][j][0][1]][posities[turn + 1][j][0][0]]) + " ")
        if level[posities[turn + 1][j][0][1]][posities[turn + 1][j][0][0]] == "x":
            f.write("dus de lengte van speler " + str(j) + " groeit van " + str(lengtes[j]) + " naar " + str(lengtes[j] + 1) + ".")
            lengtes[j] += 1
            f.write("\n")
            f.write("Voeg nog een [0,0] toe voor speler " + str(j))
            posities[turn + 1][j].append([0,0])
        #hier gaan we herkennen wie er eten pakt/
        
        #hier zorgen we dat de dode slangen niet in de muur terecht komen
        if not (level[posities[turn + 1][j][0][1]][posities[turn + 1][j][0][0]] == "x" or level[posities[turn + 1][j][0][1]][posities[turn + 1][j][0][0]] == "."):
            posities[turn + 1][j][0] = copy.deepcopy(posities[turn][j][0])
        #hier zorgen we dat de dode slangen niet in de muur terecht komen/
        
        if posities[turn + 1][j][0] == posities[turn][j][0]:
            u = 2
            while u <= lengtes[j]:
                posities[turn + 1][j][u - 1] = copy.deepcopy(posities[turn][j][u - 1])
                u += 1
        else:
            u = 2
            while u <= lengtes[j]:
                posities[turn + 1][j][u - 1] = copy.deepcopy(posities[turn][j][u - 2])
                u += 1
        
#        k = 1
#        while k <= lengtes[j]:
#            level[posities[turn + 1][j][k - 1][1]][posities[turn + 1][j][k - 1][0]] = str(j)
#            k += 1
        h = 0
        while h < level_hoogte:
            b = 0 
            while b < level_breedte:
                if [b,h] in posities[turn][j]:
                    level[h][b] = "."
                if [b,h] in posities[turn + 1][j]:
                    level[h][b] = str(j)
                b += 1
            h += 1
        j += 1
    #hier komt informatie over de nieuwe posities van de spelers/
    
    
    aantal_voedsel = int(input())   #Lees aantal nieuw voedsel en posities
    voedsel_posities = []
    for i in range(aantal_voedsel):
        voedsel_positie = [int(s) for s in input().split()]
        # Sla de voedsel positie op in een lijst en in het level
        voedsel_posities.append(voedsel_positie)
        level[voedsel_positie[1]][voedsel_positie[0]] = "x"
        
    sys.stdout.flush()


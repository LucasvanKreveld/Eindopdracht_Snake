#!/bin/python
import random
import copy
from deadend import *


f = open("anno.txt", 'w')

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
    
    #kijk voor deze beurt welke vakjes veilig zijn
    navigate = []
    
    posup = [0,0]
    posup[0] = (positie[0]  + level_breedte)%level_breedte
    posup[1] = (positie[1] - 1 + level_hoogte)%level_hoogte
    
    posdown = [0,0]
    posdown[0] = (positie[0] + level_breedte)%level_breedte
    posdown[1] = (positie[1] + 1 + level_hoogte)%level_hoogte
    
    posleft = [0,0]
    posleft[0] = (positie[0] - 1 + level_breedte)%level_breedte
    posleft[1] = (positie[1] + level_hoogte)%level_hoogte
    
    posright = [0,0]
    posright[0] = (positie[0] + 1 + level_breedte)%level_breedte
    posright[1] = (positie[1] + level_hoogte)%level_hoogte
    
    if eetmodus == 0:
        f.write("\n")
        f.write("Boven me zit vakje " + str(posup) + ", en dat is een " + str(level[posup[1]][posup[0]]))
        if (level[posup[1]][posup[0]] == "."):
            f.write("\n")
            f.write("Het is dus veilig om naar boven te gaan.")
            navigate.append('u')
        else:
            f.write("\n")
            f.write("Het is dus niet veilig om naar boven te gaan.")
        
        f.write("\n")
        f.write("Onder me zit  vakje " + str(posdown) + ", en dat is een " + str(level[posdown[1]][posdown[0]]))
        if (level[posdown[1]][posdown[0]] == "."):
            f.write("\n")
            f.write("Het is dus veilig om naar onder te gaan.")
            navigate.append('d')
        else:
            f.write("\n")
            f.write("Het is dus niet veilig om naar onder te gaan.")
        
        f.write("\n")
        f.write("Links van me zit  vakje " + str(posleft) + ", en dat is een " + str(level[posleft[1]][posleft[0]]))
        if (level[posleft[1]][posleft[0]] == "."):
            f.write("\n")
            f.write("Het is dus veilig om naar links te gaan.")
            navigate.append('l')
        else:
            f.write("\n")
            f.write("Het is dus niet veilig om naar links te gaan.")
        
        f.write("\n")
        f.write("Rechts van me zit  vakje " + str(posright) + ", en dat is een " + str(level[posright[1]][posright[0]]))
        if (level[posright[1]][posright[0]] == "."):
            f.write("\n")
            f.write("Het is dus veilig om naar rechts te gaan.")
            navigate.append('r')
        else:
            f.write("\n")
            f.write("Het is dus niet veilig om naar rechts te gaan.")
            
        if len(navigate) == 0:
            f.write("\n")
            f.write("Er zijn geen lege vakjes, als ik kan eten moet ik dat doen.")
            eetmodus = 1
            if (level[posup[1]][posup[0]] == "x"):
                navigate.append('u')
            if (level[posdown[1]][posdown[0]] == "x"):
                navigate.append('d')
            if (level[posleft[1]][posleft[0]] == "x"):
                navigate.append('l')
            if (level[posright[1]][posright[0]] == "x"):
                navigate.append('r')
            if len(navigate) == 0:
                navigate.append('u')
                navigate.append('d')
                navigate.append('l')
                navigate.append('r')
    else:
        xcount = 0
        xnavigate = []
        f.write("\n")
        f.write("Boven me zit vakje " + str(posup) + ", en dat is een " + str(level[posup[1]][posup[0]]))
        if (level[posup[1]][posup[0]] == "x" or level[posup[1]][posup[0]] == "."):
            if level[posup[1]][posup[0]] == "x":
                xnavigate.append('u')
                xcount += 1
            f.write("\n")
            f.write("Het is dus veilig om naar boven te gaan.")
            navigate.append('u')
        else:
            f.write("\n")
            f.write("Het is dus niet veilig om naar boven te gaan.")
        
        f.write("\n")
        f.write("Onder me zit  vakje " + str(posdown) + ", en dat is een " + str(level[posdown[1]][posdown[0]]))
        if (level[posdown[1]][posdown[0]] == "x" or level[posdown[1]][posdown[0]] == "."):
            if level[posdown[1]][posdown[0]] == "x":
                xnavigate.append('d')
                xcount += 1
            f.write("\n")
            f.write("Het is dus veilig om naar onder te gaan.")
            navigate.append('d')
        else:
            f.write("\n")
            f.write("Het is dus niet veilig om naar onder te gaan.")
        
        f.write("\n")
        f.write("Links van me zit  vakje " + str(posleft) + ", en dat is een " + str(level[posleft[1]][posleft[0]]))
        if (level[posleft[1]][posleft[0]] == "x" or level[posleft[1]][posleft[0]] == "."):
            if level[posleft[1]][posleft[0]] == "x":
                xnavigate.append('l')
                xcount += 1
            f.write("\n")
            f.write("Het is dus veilig om naar links te gaan.")
            navigate.append('l')
        else:
            f.write("\n")
            f.write("Het is dus niet veilig om naar links te gaan.")
        
        f.write("\n")
        f.write("Rechts van me zit  vakje " + str(posright) + ", en dat is een " + str(level[posright[1]][posright[0]]))
        if (level[posright[1]][posright[0]] == "x" or level[posright[1]][posright[0]] == "."):
            if level[posright[1]][posright[0]] == "x":
                xnavigate.append('r')
                xcount += 1
            f.write("\n")
            f.write("Het is dus veilig om naar rechts te gaan.")
            navigate.append('r')
        else:
            f.write("\n")
            f.write("Het is dus niet veilig om naar rechts te gaan.")
        f.write("\n")
        f.write("xcount is " + str(xcount))
        if xcount > 0:
            f.write("\n")
            f.write("Er is eten, dus daar ga ik naar toe")
            navigate = []
            p = 0
            while p < len(xnavigate):
                navigate.append(xnavigate[p])
                p += 1
        else:
            f.write("\n")
            f.write("Er is geen eten, dus ik moet naar een leeg vakje als dat kan")
        
        
        if len(navigate) == 0:
            navigate.append('u')
            navigate.append('d')
            navigate.append('l')
            navigate.append('r')
    #kijk voor deze beurt welke vakjes veilig zijn
    
    f.write("\n")
    f.write("Mijn opties zijn " + str(navigate))
    
    richting = '0'
    while not(richting in navigate):
        i = random.randrange(4)         #Kies een random richting
        f.write("\n")
        f.write("Zal ik " + 'urdl'[i] + " kiezen?")
        richting = 'urdl'[i]           #u=up, d=down, l=left, r=right
    
    positie[0] += dx[i]             #Verander de huidige positie
    positie[1] += dy[i]
                                    #Let op periodieke randvoorwaarden!
    positie[0] = (positie[0] + level_breedte)% level_breedte
    positie[1] = (positie[1] + level_hoogte) % level_hoogte
    
    f.write("\n")
    f.write("Ik kies "+ 'urdl'[i] + ".")
    
    
    
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


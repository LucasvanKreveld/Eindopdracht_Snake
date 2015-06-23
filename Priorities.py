# Dit programma levert de coördinaat voor de slang waar hij de volgende beurt het beste naar toe kan gaan.
# Area is de functie die het gebied van 3x3 bepaalt met als middelpunt [x,y].
def Area(x,y):
    area=[]
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            area.append([(x+i) % level_breedte , (y+j) % level_hoogte])
    return area
    
# Check1 is de functie die bepaalt of een bepaalde coördinaat toegangbaar is.       
def Check1(x,y):
    if level[y][x] == "#" or (level[y][x] != "." and level[y][x] != "x") :
        return -10000
    elif ([x,y] in doodlopend_permanent):
        return -1000
    elif [x,y] in doodlopend_momenteel_weergave:
        return -100
    else:
        return 0
        
# Check2 is de functie die gaat kijken of een coördinaat eten bevat of niet. We willen namelijk dat de slang zolang mogelijk van het eten afblijft.
def Check2(x,y):
    if level[y][x] == ".":
        return 1
    else:
        return 0
        
# Check3 is de functie die de hoeveelheid vrije coördinaten rond een bepaald punt bepaalt.
def Check3(x,y):
    area = Area(x,y) - [[x,y]]
    Mark = 0
    for i in range(0,len(area)):
        if level[area[i][1]][area[i][0]] == ".":
            Mark += 2
        elif level[area[i][1]][area[i][0]] == "x":
            Mark += 1
    return Mark

# Prior is de functie die aan de hand van de bovenstaande functies de coördinaat bepaald waar de slang de volgende beurt naar toe moet gaan.
def Prior(x,y):
    area = Area(x,y)
    rating = []
    for i in range(0,len(area)):
        Mark = Check1(area[i][0] , area[i][1]) + Check2(area[i][0] , area[i][1]) + Check3(area[i][0] , area[i][1])
        rating.append(Mark)
    maxelement = max(rating)
    return(area[rating.index(maxelement)])
    
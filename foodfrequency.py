    #check de frequentie waarin voedsel verschijnt
hoeveelheid_eten = 0    
    if tijdstap == 10:
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
            hoeveelheid_eten += eten_gepakt
        
        eten_frequentie = float(hoeveelheid_eten) / 10
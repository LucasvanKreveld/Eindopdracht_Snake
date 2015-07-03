def levelherkenner(level, level_breedte, level_hoogte):
    mogelijke_levels = [1,2,3]
    aantal_hekjes = 0
    j = 0
    while j < level_breedte:
        if not (level[0][j] != '#' and level[2][j] != '#' and level[4][j] != '#' and level[6][j] != '#' and level[8][j] != '#'):
            mogelijke_levels.remove(3)
            break
        j += 1
    if 3 in mogelijke_levels:
        return 3
    j = 0
    while j < level_breedte:
        k = 0
        while k < level_hoogte:
            if level[k][j] == '#':
                aantal_hekjes += 1
            k += 1
        j += 1
    hekjesratio = aantal_hekjes/(level_hoogte*level_breedte)
    
    if hekjesratio < 0.35:
        return 1
    
    else:
        return 2
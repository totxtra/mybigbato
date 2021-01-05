def coordonnees_bato(ecran): #Recupere les coordonnees des bateaux
    coord_list = [[],[],[],[],[]]
    for i in ecran:
        for j in i:
            if j[1] == 5:
                coord_list[0].append(j[0])
            elif j[1] == 4:
                coord_list[1].append(j[0])
            elif j[1] == 3:
                coord_list[2].append(j[0])
            elif j[1] == 2:
                coord_list[3].append(j[0])
            elif j[1] == 1:
                coord_list[4].append(j[0])

    return coord_list # [[5],[4],[3],[3],[2]]

def touche(tir, coord_bato):
    for i in range(len(coord_bato)):
        if tir in coord_bato[i]:
            coord_bato[i].remove(tir)
            return coord_bato
    else:
        return coord_bato
    
def test_coule(coord_bato): # teste si un bateau a été coulé
    try:
        if not coord_bato[0]:
            return ["porte-avion coulé", 0]
        elif not coord_bato[1]:
            return ["croiseur coulé", 1]
        elif not coord_bato[2]:
            return ["contre-torpilleur coulé", 2]
        elif not coord_bato[3]:
            return ["contre_torpilleur coulé", 3]
        elif  not coord_bato[4]:
            return ["torpilleur coulé", 4] 
        else:
            return False
    except:
        print("erreur")
    
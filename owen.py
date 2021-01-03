import random
#-------------------------------------------------------

def afficher(mat,visible):  #affichage console python
    a = '\n--------------------------------------------\n   | A | B | C | D | E | F | G | H | I | J |\n'
    k = ['A0']
    for i in mat:
        c = str(
            int(k[0][1]) + 1
        ) 
        while len(c) < 3:
            c += ' '
        a += c + '|'
        for k in i:
            b = ''
            if k[2] == 1 and k[1] > 0:
                b += ' +'
            elif k[2] == 1 and k[1] == 0:
                b += ' x'
            elif k[1] > 0 and visible==1:#seulement si on veut que les bateaux soient visibles
                b += ' ' + str(k[1])
            else:
                b += ' -'
            if len(b) < 3:
                b += ' '
            b += '|'
            a += b
        a += '\n'
    return a + '--------------------------------------------\n'


def recherche(mat):     #|-|3| dans une situation telle que celle-ci, il se peut que l'ia 'oublie'
    ct = 0              #|2|3| la case du haut, vu qu'elle cherche en priorité à l'horizontale.
    for a in range(9):  #|2|3| la fonction dernierrecours permet de tirer à côté de là où un
        for b in range(0, 9, 2):#bateau a été touché.
            if a % 2 == 0:
                b += 1
            if mat[a][b][2] == 1:
                ct += 1
    if ct != 50:
        return rechercheorganisee(mat)
    else:
        return dernierrecours(mat)


def rechercheorganisee(mat):  #recherche aléatoire mais méthodique (en sautant une case à chaque fois)
    while True:
        try:
            x = random.randint(0, 9)   #|x| |x|
            y = random.randint(0,4)*2  #| |x| |
            if x % 2 == 0:             #|x| |x|
                y += 1
            if mat[x][y][2] == 1:
                raise ValueError
            mat[x][y][2] = 1
            print("l'ia a tiré en ", 'ABCDEFGHIJ'[y],str(x+1))
            if mat[x][y][1] > 0:
                return mat, 'touché', [x, y]
            else:
                return mat, 'recherche'
            break
        except:
            pass


def dernierrecours(mat):  #il peut y avoir des occurrences où l'ia est perdue, donc on la fait tirer à côté de là où un bateau a été touché
    while True:
        try:
            x = random.randint(0, 9)      #| |x| |
            y = random.randint(0, 4) * 2  #|x| |x|
            if x % 2 == 1:                #| |x| |
                y += 1
            if mat[x][y][2] == 1:
                raise ValueError
            mat[x][y][2] = 1
            ct = 0
            if (mat[x][y + 1][2] == 1 and mat[x][y + 1] > 0) or (mat[x][y - 1][2] == 1 and mat[x][y - 1]) > 0 or (mat[x + 1][y][2] == 1 and mat[x + 1][y] > 0):
                ct = 1
            if ct == 0:
                raise ValueError
            print("l'ia a tiré en ", 'ABCDEFGHIJ'[y],str(x+1))
            break
        except:
            pass


def rechercheori(mat, cible):  #long car bcp de commentaires et de if
    #l'ia va faire le tour de la cible pour determiner
    #return matrice,etat,cible,orientation,limite(de chaque coté du bateau, ex: -+++-,la traque se termine une fois que les 2 sont trouvées),long(voir traque())
    print(cible)
    x = cible[0]  #ligne
    y = cible[1]  #colonne
    #les verifications suivantes se font de la sorte:
    #si l'on a pas déjà tiré sur la case en question, on y tire;si ça touche, on passe à la traque
    #comme les 2 dernieres conditions sont valables si les 2 premières sont fausses, on aura trouvé une limite du bateau.
    if y != 9:  #ne pas sortir de la matrice
        if mat[x][y + 1][2] != 1:  #colonne suivante, bateau horizontal ?
            mat[x][y + 1][2] = 1
            print("l'ia a tiré en ", 'ABCDEFGHIJ'[y+1],str(x+1))
            if mat[x][y + 1][1] > 0:
                return mat, 'traque', cible, 0, 0, 2
            else:
                return mat, 'touché', cible
    if x != 9:
        if mat[x + 1][y][2] != 1:  #ligne suivante, bateau vertical?
            mat[x + 1][y][2] = 1
            print("l'ia a tiré en ", 'ABCDEFGHIJ'[y],str(x+2))
            if mat[x + 1][y][1] > 0:
                return mat, 'traque', cible, 1, 0, 2
            else:
                return mat, 'touché', cible
    if y != 0:
        if mat[x][y - 1][2] != 1:  #colonne précédente
            mat[x][y - 1][2] = 1
            print("l'ia a tiré en ", 'ABCDEFGHIJ'[y-1],str(x+1))
            if mat[x][y - 1][1] > 0:
                return mat, 'traque', cible, 0, 1, -2
            else:
                return mat, 'touché', cible
    if x != 0:
        if mat[x - 1][y][2] != 1:  #ligne précédente
            mat[x - 1][y][2] = 1
            print("l'ia a tiré en ", 'ABCDEFGHIJ'[y],str(x))
            if mat[x - 1][y][1] > 0:
                return mat, 'traque', cible, 1, 1, -2
            else:
                return mat, 'touché', cible
    return mat.recherche()


def traque(mat, cible, ori, lim,long):  #longueur due à la profusion de conditions if
    #explication des parametres:
    #cible = case trouvée par la recherche
    #ori=orientation du bateau trouvée en second lieu
    #lim= nombre d'extrémités du bateau trouvées, si l'une d'elles est déjà trouvée, on cherche de l'autre côté
    #long:
    x = cible[0]  #x=ligne, y = colonne
    y = cible[1]
    if lim == 0:
        if ori == 1:
            if x + long < 10:  #tant que la case en question existe
                x += long
            else:  #sinon on a trouvé une limite
                return traque(mat, cible, ori, 1, -1)
        else:  #idem pour y
            if y + long < 10:
                y += long
            else:
                return traque(mat, cible, ori, 1, -1)
    else: #
        if ori == 1:
            if x + long > -1:
                x += long
            else:
                return recherche(mat)
        else:
            if y + long > -1:
                y += long
            else:
                return recherche(mat)


    if lim == 1:  # si l'une des limites est déjà trouvée, l'ia cherche dans l'autre sens
        long -= 1
    else:
        long += 1
    if mat[x][y][2] != 1:  #tirer si ce n'est pas déjà fait
        mat[x][y][2] = 1
        print("l'ia a tiré en ", 'ABCDEFGHIJ'[y],str(x+1))
    else:  #si c'est déjà fait, vérifier l'état de la case en question
        if mat[x][y][
                1] > 0:  #si il y a un bateau dessus, on traque la case suivante
            return traque(mat, cible, ori, lim, long)
        else:
            if lim == 1:  #si l'ia a déjà trouvé une extremité
                return recherche(mat)
            else:  #sinon on vient d'en trouver une !
                return traque(mat, cible, ori, 1, -1)
    if mat[x][y][1] == 0:
        if lim == 1:  #si l'ia a déjà trouvé une extremité
            return mat, 'recherche'
        else:  #sinon on vient d'en trouver une !
            return mat, 'traque', cible, ori, 1, -1
    else:
        return mat, 'traque', cible, ori, lim, long


def tiriarandom(mat):  #recherche 100% aléatoire, peut tirer n'importe où
    while True:
        try:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if mat[x][y][2] == 1:
                raise ValueError
            mat[x][y][2] = 1
            print("l'ia a tiré en ", 'ABCDEFGHIJ'[y],str(x+1))
            if mat[x][y][1] > 0:
                return mat, 'touché' , [x,y]
            else:
                return mat, 'recherche'
            break
        except:
            pass


def verifpoints(mat):
    pts = 0
    for i in mat:
        for k in i:
            if k[1] > 0 and k[2] == 1:
                pts += 1
    return pts


def tiria(pIA, diff):
    ecran = pIA[0]
    phase = pIA[1]
    if phase == 'recherche' and diff == 3:
        pIA = recherche(ecran)  # recherche méthodique
    elif phase == 'recherche' and diff == 2:  #recherche aléatoire
        pIA = tiriarandom(ecran)
    elif phase == 'touché' and diff > 1:  #valable pour diff 2 et 3, tire autour de la case touchée avec la recherche pour determiner l'orientation du bateau
        cible = pIA[2]
        pIA = rechercheori(ecran, cible)
    elif phase == 'traque' and diff > 1:  #valable pour diff 2 et 3, tire d'un côté et de l'autre du bateau touché
        pIA = traque(ecran, pIA[2], pIA[3], pIA[4], pIA[5])
    else:  #valable pour la phase 'recherche' de diff 2 et pour diff 1. quand on dit facile, on dit VRAIMENT facile.
        pIA = tiriarandom(ecran)

    ecran = pIA[0]
    return ecran, pIA


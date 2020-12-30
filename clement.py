import owen
import random
#Chaque bateaux est définie par : son nombre de cases, son sens,ses coordonnées et son code
porte_avion = [5,0,[0,0],5]
croiseur = [4,0 ,[0,0],4]
contre_torpilleur_1 = [3,0,[0,0],3]
contre_torpilleur_2 = [3,0,[0,0],2]
torpilleur = [2,0,[0,0],1]
bateauxj = [porte_avion, croiseur, contre_torpilleur_1, contre_torpilleur_2, torpilleur]
bateaux_ia = bateauxj
def ecran():
    a = 'ABCDEFGHIJ'
    ecran = [[[k + str(i + 1), 0, 0] for k in a] for i in range(10)]
    return ecran
#Le but de case est que 
def case(bateaux_ia) :
    for i in range(len(bateaux_ia)) :
        max = 10 - bateaux_ia[i][0]
        bateaux_ia[i][1] = (random.randint(0,1))
        if bateaux_ia[i][1] == 0 :
            x = random.randint(0, max)
            y = random.randint(0, 10)
        else:
            x = random.randint(0, 10)
            y = random.randint(0, max)
        bateaux_ia[i][2] = [x,y]
    return bateaux_ia

bateaux_ia = case(bateaux_ia)

def ajout_bateaux_ia() :
    porte_avion = [5,0,[0,0],5]
    croiseur = [4,0 ,[0,0],4]
    contre_torpilleur_1 = [3,0,[0,0],3]
    contre_torpilleur_2 = [3,0,[0,0],2]
    torpilleur = [2,0,[0,0],1]
    bateaux_ia = [porte_avion, croiseur, contre_torpilleur_1, contre_torpilleur_2, torpilleur]
    bateaux_ia = case(bateaux_ia)
    carte_ia = ecran()
    for i in range(len(bateaux_ia)) :
        for k in range(len(carte_ia)) :
            if k == bateaux_ia[i][2][0] :
                for j in range(len(carte_ia)) :
                    if j == bateaux_ia[i][2][1] :
                        carte_ia[j][k][1] = bateaux_ia[i][3]
                        for x in range(1,bateaux_ia[i][0]) :
                            if bateaux_ia[i][1] == 0 :
                                carte_ia[j][k+x][1] = bateaux_ia[i][3]
                            else:
                                carte_ia[j+x][k][1] = bateaux_ia[i][3]
    return carte_ia

def ajout_bateaux_j() :
    porte_avion = [5, 0, [0, 0], 5]
    croiseur = [4, 0, [0, 0], 4]
    contre_torpilleur_1 = [3, 0, [0, 0], 3]
    contre_torpilleur_2 = [3, 0, [0, 0], 2]
    torpilleur = [2, 0, [0, 0], 1]
    liste_nom_bateaux = ["porte_avion", "croiseur", "contre_torpilleur_1", "contre_torpilleur_2", "torpilleur"]
    cases = [["A", 0], ["B", 1], ["C", 2], ["D", 3], ["E", 4], ["F", 5], ["G", 6], ["H", 7], ["I", 8], ["J", 9]]
    bateauxj = [porte_avion, croiseur, contre_torpilleur_1, contre_torpilleur_2, torpilleur]
    cartej = ecran()
    z = 0
    for i in range(len(bateauxj)) :
        print("Placer votre", liste_nom_bateaux[i],", qui est de longeur :",bateauxj[i][0])
        while z == 0 :
          try:
                coordonnées = input("Indiquez la case dans laquelle sera placer le point le plus en haut à gauche (A1,B1 ...) :")
                coordonnées_liste = list(coordonnées)
                print("0 : horizontal")
                print("1 : vertical")
                sens = int(input("Dans quel sens voulez vous le placer ? :"))
                for b in range(len(cases)) :
                    if cases[b][0] == coordonnées_liste[0] :
                        coordonnées_liste[0] = cases[b][1]
                if 1 <= int(coordonnées_liste[1]) <= 10 :
                    if 0 <= sens <= 1:
                        if ((int(coordonnées_liste[1]) + bateauxj[i][0] <= 11) and (sens == 1)):
                            z = 1
                        elif (coordonnées_liste[0] + bateauxj[i][0] <= 10) and (sens == 0) :
                            z = 1
                        else :
                            raise TypeError
                    else :
                        raise EnvironmentError
          except TypeError:
            print('case invalide')
          except EnvironmentError:
            print('0 ou 1')
        coordonnées_liste = list(coordonnées)
        for a in range(len(cases)) :
            if cases[a][0] == coordonnées_liste[0] :
                coordonnées_liste[0] = cases[a][1]
        coordonnées_liste[1] = int(coordonnées_liste[1]) - 1
        bateauxj[i][1] = sens
        bateauxj[i][2] = coordonnées_liste
        for k in range(len(cartej)):
            if k == bateauxj[i][2][0]:
                for j in range(len(cartej)):
                    if j == bateauxj[i][2][1]:
                        cartej[j][k][1] = bateauxj[i][3]
                        for x in range(1, bateauxj[i][0]):
                            if bateauxj[i][1] == 0:
                                cartej[j][k + x][1] = bateauxj[i][3]
                            else:
                                cartej[j + x][k][1] = bateauxj[i][3]
        print(owen.afficher(cartej))
        z = 0
    return cartej



def test_ia() :
  while True:
    try:
      ecranj = ajout_bateaux_ia()
      a=0
      for i in ecranj:
        for k in i:
          if k[1]>0:
            a+=1
      if a!=17:
        raise EnvironmentError
      return ecranj
      break
    except:
      pass

def test_j() :
  while True:
    try:
      ecranj = ajout_bateaux_j()
      a=0
      for i in ecranj:
        for k in i:
          if k[1]>0:
            a+=1
      if a!=17:
        raise EnvironmentError
      return ecranj
      break
    except:
      pass
















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































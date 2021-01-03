import owen
import random
import os

def cls(): 
  os.system('cls' if os.name=='nt' else 'clear') #pour clear la console : cls()

def ecran(): #Faite par Owen, je l'ai emprunté ^^
    a = 'ABCDEFGHIJ'
    ecran = [[[k + str(i + 1), 0, 0] for k in a] for i in range(10)]
    return ecran

#case() à pour but de définir pour l'ia les paramètres qui permettront de placer ses bateaux de manière aléatoire  
def case(bateaux_ia) :
    for i in range(len(bateaux_ia)) :
        max = 10 - bateaux_ia[i][0]   #Le max permet de ne pas dépasser la bordure
        bateaux_ia[i][1] = (random.randint(0,1))  # 0 signifie horizontal et 1 vertical
        if bateaux_ia[i][1] == 0 :    #Les coordonnées dépendent du sens !
            x = random.randint(0, max)
            y = random.randint(0, 10)
        else:
            x = random.randint(0, 10)
            y = random.randint(0, max)
        bateaux_ia[i][2] = [x,y]
    return bateaux_ia #la fonction sera sous forme : bateaux_ia[taille,sens,coordonnées,valeur]

#ajout_bateaux_ia2() sert à placer les bateaux de l'ia sur l'écran (Attention, elle permet seulement de placer les bateaux mais elle ne fait pas attention à la superposition de ses derniers, c'est pour cela qui il y a la fonction ajout_bateaux_ia qui permet de tester la superposition des bateaux )

def ajout_bateaux_ia2() :#véritable fonction ajout bateau ia 
    bateaux_ia = [[5,0,[0,0],5], [4,0 ,[0,0],4], [3,0,[0,0],3], [3,0,[0,0],2], [2,0,[0,0],1]]#porte_avion, croiseur, contre_torpilleur_1, contre_torpilleur_2, torpilleur
    bateaux_ia = case(bateaux_ia)
    carte_ia = ecran()
    for i in range(len(bateaux_ia)) :
        for k in range(len(carte_ia)) :
            if k == bateaux_ia[i][2][0] :
                for j in range(len(carte_ia)) :
                    if j == bateaux_ia[i][2][1] :
                        for x in range(bateaux_ia[i][0]) :
                            if bateaux_ia[i][1] == 0 :
                                carte_ia[j][k+x][1] = bateaux_ia[i][3]
                            else:
                                carte_ia[j+x][k][1] = bateaux_ia[i][3]
    return carte_ia

def ajout_bateaux_j() :
    liste_nom_bateaux = ["porte avion", "croiseur", "contre torpilleur n°1", "contre torpilleur n°2", "torpilleur"]
    bateauxj = [[5, 5], [4, 4], [3, 3], [3,2], [2,1]]#porte_avion, croiseur, contre_torpilleur_1, contre_torpilleur_2, torpilleur]
    cartej = ecran()
    for i in range(len(bateauxj)) :
        print("Placer votre", liste_nom_bateaux[i],", qui est de longeur :",bateauxj[i][0],"cases.")
        print("La case sera le point le plus en haut à gauche du bateaux")
        ct=0
        while ct==0 :
          try:
                coordonnées=input("Indiquez la case (A1,B1 ...) :").upper()
                for l in cartej:
                  for j in l:
                    if j[0]==coordonnées:
                      coordonnées_liste=cartej.index(l),l.index(j)
                coordonnées=coordonnées_liste#génèrera une NameError si coordonnées liste n'a jamais été défini
                print("0 : horizontal")
                print("1 : vertical")
                sens = int(input("Dans quel sens voulez vous le placer ? : "))
                if not (sens==1 or sens ==0):
                  raise ValueError
                for x in range(bateauxj[i][0]):
                  if sens==1:
                    if cartej[coordonnées_liste[0]+x][coordonnées_liste[1]][1]>0:
                      raise IndexError
                  else:
                    if cartej[coordonnées_liste[0]][coordonnées_liste[1]+x][1]>0:
                      raise IndexError
                ct=1
          except ValueError:
            print('sens = 0 ou 1')
          except IndexError:
            print('case  invalide')  
          except NameError:
            print('case inexistante')     
        cls()
        for h in range(bateauxj[i][0]):
          if sens==1:
            cartej [coordonnées_liste[0]+h][coordonnées_liste[1]][1]=bateauxj[i][1]
          else:
            cartej[coordonnées_liste[0]][coordonnées_liste[1]+h][1]=bateauxj[i][1]
        print(owen.afficher(cartej,1))
    return cartej

def ajout_bateaux_ia() :#juste un test pour savoir si il n'y a pas de bateaux superposés
  while True:
    try:
      ecranj = ajout_bateaux_ia2()#véritable fonction
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

def resultat(ptsjoueur,ptsia) :
  if ptsjoueur == 17 :
    return "Victoire, vous avez abattu la flotte adverse, vous êtes le roi des flots ^^ "
  elif ptsia == 17 :
    return "Défaite :( , vous ferez mieux la prochaine fois ^^'"
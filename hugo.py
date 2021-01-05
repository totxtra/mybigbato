import owen
import clement


def tir_joueur(carte_j) :
    test_g = 0
    while test_g == 0 :
        print("Vous devez renseigner une lettre suivie d'un chiffre.")
        #demander ou l on veut tirer
        tir = input("Où voulez-vous tirer ? ")
        tir=tir.upper()
        #définitions d un compteur
        s = 0
        #parcourir la carte
        for i in range(len(carte_j)) :
            for j in range (len(carte_j[i])) :
                #vérifie si la case existe
                s+=1
                if tir == carte_j[i][j][0] :
                    #vérifie si il y a deja eu un tire sur l'emplacement choisie
                    if 0 == carte_j[i][j][2] :
                        carte_j[i][j][2] = 1
                        test_g = 1
                    else :
                      print('/!\ Capitaine, vous avez déjà tiré ici !')
                      s=0
                if s == 100 :
                  print("/!\ Vous avez tiré en terre inconnue, le cannonier n'a pas compris votre ordre !")         
    return carte_j, tir


#fonction rejouer créée par Hugo
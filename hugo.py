import owen
import clement
import csv

def leaderboard(ct,win) :
    if win == 17 :
        result = 'gagné'
    else :
        result = 'perdu'
    print(f"Vous avez {result} en {ct} tours.")
  

#login()
#register(login())


def tir_joueur(carte_j) :
    test_g = 0
    while test_g == 0 :
        print("Vous devez renseigner une lettre suivie d'un chiffre.")
        #demander ou l on veut tirer
        tir = input("Où voulez-vous tirer ? ")
        tir=tir.upper()
        #parcourir la carte
        for i in range(len(carte_j)) :
            for j in range (len(carte_j[i])) :
                #vérifie si la case existe
                if tir == carte_j[i][j][0] :
                    #vérifie si il y a deja eu un tire sur l'emplacement choisie
                    if 0 == carte_j[i][j][2] :
                        carte_j[i][j][2] = 1
                        test_g = 1
    return carte_j
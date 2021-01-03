#main.py
import os
import owen
import time
import hugo
import clement

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

'''' 
reader_2 = csv.DictReader(open('logins.csv','r'))
logins=[dict(row) for row in reader_2]'''


def choix_difficulte():
    print("Bienvenue dans la Bataille Navale,")
    print("L'équipe de développement vous souhaite une agréable partie !")
    while True:
        try:
            diff = int(input('Choisissez une difficulté de 1 à 3 : '))
            if not 0 < diff < 4:
                raise ValueError
            break
        except:
            print('de 1 à 3')
    cls()
    time.sleep(0.5)
    return diff


def round(ecranj, ecrania, pIA, difficulte, ct, ptsjoueur, ptsia):
    print(
        owen.afficher(ecranj, 0),
        f"\nLe joueur a {ptsjoueur} pts\nL'ordinateur a {ptsia} pts\n")
    ecranj = hugo.tir_joueur(ecranj)
    test_ptsjoueur = owen.verifpoints(ecranj)
    if test_ptsjoueur != ptsjoueur:
        print("Vous avez touché l'ennemi !")
    ptsjoueur = test_ptsjoueur
    print(owen.afficher(ecranj, 0))
    print('----------------------------\n')
    cls()  #ia
    print(owen.afficher(ecrania, 1))
    b = owen.tiria(pIA, difficulte)
    ecrania = b[0]
    pIA = b[1]
    cls()
    print(f'| Tour {ct}', '|\n\nVos bateaux:')
    print(owen.afficher(ecrania, 1))
    test_ptsia = owen.verifpoints(ecrania)
    if test_ptsia != ptsia:
        print("L'ennemi vous a touché !")
    ptsia = test_ptsia
    print("Bateaux de l'ordinateur :")
    ct += 1
    return ecranj, ecrania, pIA, ct, ptsjoueur, ptsia


def main():
    nbr_bato = [[5,4,3,3,2],[5,4,3,3,2]]# 0 = j 1 = ia
    ptsjoueur = 0
    ptsia = 0
    difficulte = -1
    difficulte = choix_difficulte()
    print(owen.afficher(clement.ecran(), 1))
    ecranj = clement.ajout_bateaux_ia()  #ajout des bateaux de l'ia
    ecrania = clement.ajout_bateaux_j()  #ajout des bateaux du joueur
    cls()
    pIA = [
        ecrania, 'recherche'
    ]  #ensemble de paramètres pour l'ia, le premier étant sa matrice de jeu et le 2eme son état, 'recherche','touché' ou 'traque', et certaines valeurs seront ajoutées après certaines phases: la cible, l'orientation de la cible, puis le parametre long, voir fonction traque() par Owen
    ct = 1
    while ptsjoueur != 17 and ptsia != 17:  #17=place totale prise par les bateaux
        ecranj, ecrania, pIA, ct, ptsjoueur, ptsia = round(
            ecranj, ecrania, pIA, difficulte, ct, ptsjoueur, ptsia)
    print(clement.resultat(ptsjoueur, ptsia))


if __name__ == "__main__":
    play =1
    while play == 1 :
      main()
      
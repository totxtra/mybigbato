#main.py
import os
import owen
import time
import hugo
import clement
import maxime


def cls():
	os.system('cls' if os.name == 'nt' else 'clear')


def choix_difficulte():
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


def round(ecranj, ecrania, pIA, difficulte, ct, ptsjoueur, ptsia, coordj,coordia, jsp, coulé):
    print(owen.afficher(ecranj, 0),f"\nLe joueur a {ptsjoueur} pts\nL'ordinateur a {ptsia} pts\n")
    if jsp == 1:
        print(coulé[0])
    tir_j = hugo.tir_joueur(ecranj)
    ecranj = tir_j[0]
    coord_tir = tir_j[1]
    test_ptsjoueur = owen.verifpoints(ecranj)
    if test_ptsjoueur != ptsjoueur:
		print("Vous avez touché l'ennemi !")
		coordj = maxime.touche(coord_tir, coordj)
		coulé = maxime.test_coule(coordj)
		if coulé != False:
			print(coulé[0])
			coordj[coulé[1]].append("coulé")
	ptsjoueur = test_ptsjoueur
	print(owen.afficher(ecranj, 0), '\n----------------------------\n')
	time.sleep(1)
	cls()  #----------
	print(owen.afficher(ecrania, 1))
	tir_ia = owen.tiria(pIA, difficulte)
	ecrania = tir_ia[0]
	pIA = tir_ia[1]
	cls()
	print(f'| Tour {ct}', '|\n\nVos bateaux:\n', owen.afficher(ecrania, 1))
	test_ptsia = owen.verifpoints(ecrania)
	if test_ptsia != ptsia:
		print("L'ennemi vous a touché !")
		coordia = maxime.touche(coord_tir, coordia)
		coulé = maxime.test_coule(coordia)
		if coulé != False:
			coordia[coulé[1]].append("coulé")
            jsp = 1
	ptsia = test_ptsia
	print("Bateaux de l'ordinateur :")
	ct += 1
	return ecranj, ecrania, pIA, ct, ptsjoueur, ptsia, coordj, coordia, jsp, coulé


def main():
	print(
	    "Bienvenue dans la Bataille Navale,\nL'équipe de développement vous souhaite une agréable partie !"
	)
	ptsjoueur = 0
	ptsia = 0
	difficulte = -1
	difficulte = choix_difficulte()
	print(owen.afficher(clement.ecran(), 1))
	ecranj = clement.ajout_bateaux_ia()  #ajout des bateaux de l'ia
	ecrania = clement.ajout_bateaux_j()  #ajout des bateaux du joueur
	coordonneesj = maxime.coordonnees_bato(ecranj)
	coordonneesia = maxime.coordonnees_bato(ecrania)
	cls()
	pIA = [
	    ecrania, 'recherche'
	]  #ensemble de paramètres pour l'ia, le premier étant sa matrice de jeu et le 2eme son état, 'recherche','touché' ou 'traque', et certaines valeurs seront ajoutées après certaines phases: la cible, l'orientation de la cible, puis le parametre long, voir fonction traque() par Owen
	ct = 1
    jsp,coulé = 0,0
	while ptsjoueur != 17 and ptsia != 17:  #17=place totale prise par les bateaux
		ecranj, ecrania, pIA, ct, ptsjoueur, ptsia, coordonneesj, coordonneesia, jsp, coulé = round(
		    ecranj, ecrania, pIA, difficulte, ct, ptsjoueur, ptsia,
		    coordonneesj, coordonneesia, jsp,coulé)
	print(clement.resultat(ptsjoueur, ptsia))


if __name__ == "__main__":
    play = 1
	#rejouer ?
    while play == 1:
        main()
        print("Voulez-vous rejouer ?")
        test_y = 0
		#demande si l utilisateur rejoue
        while test_y == 0:
            try:
                s = input("Taper 1 pour rejouer et 0 pour arreter : ")
                if s != '1' and s != '0':
                    print('Capitaine, ne vous déconcentrez pas !! Vous devez taper 1 ou 0 !')
                else:
                    test_y = 1
            except :
                print("Capitaine, ne vous déconcentrez pas !! Vous devez taper 1 ou 0 !")

        play = s

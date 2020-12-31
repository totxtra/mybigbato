#main.py
import tkinter
import owen 
import time
import hugo
import clement

'''' 
reader_2 = csv.DictReader(open('logins.csv','r'))

logins=[dict(row) for row in reader_2]'''

def ecran():
    a = 'ABCDEFGHIJ'
    ecran = [[[k + str(i + 1), 0, 0] for k in a] for i in range(10)]
    return ecran

def choix_difficulte():
    while True:
        try:
            diff = int(input('Choisissez une difficulté de 1 à 3 : '))
            if not 0 < diff < 4:
                raise ValueError
            break
        except:
            print('de 1 à 3')
    return diff

def round(ecranj, ecrania, pIA, difficulte,ct,ptsjoueur,ptsia):
    print(f'tour {ct}')
    print(owen.afficher(ecranj,0))
    ecranj=hugo.tir_joueur(ecranj)
    ptsjoueur=owen.verifpoints(ecranj)
    print('joueur : %spts' % ptsjoueur)
    print(owen.afficher(ecranj,0))
    print('----------------------------')
    b=owen.tiria(pIA,difficulte)
    ecrania=b[0]
    pIA=b[1]
    time.sleep(2)
    print(owen.afficher(ecrania,1))
    ptsia=owen.verifpoints(ecrania)
    print('ia : %s pts' % ptsia)
    print('----------------------------')
    ct+=1
    return ecranj, ecrania, pIA,difficulte,ct,ptsjoueur,ptsia

def main():
  ptsjoueur=0
  ptsia=0
  difficulte = -1
  ecrania = ecran()
  difficulte= choix_difficulte()
  ecranj=clement.test_ia()#ajout des bateaux
  ecrania=clement.test_j() 
  pIA=[ecrania,'recherche']#ensemble de paramètres pour l'ia, le premier étant sa matrice de jeu et le 2eme son état, 'recherche','touché' ou 'traque', et certaines valeurs seront ajoutées après certaines phases: la cible, l'orientation de la cible, puis le parametre long, voir fonction traque() par Owen
  ct=0
  while ptsjoueur!=17 and ptsia !=17:#17=place totale prise par les bateaux
    ecranj, ecrania, pIA, difficulte,ct,ptsjoueur,ptsia = round(ecranj, ecrania, pIA, difficulte,ct,ptsjoueur,ptsia)

if __name__ == "__main__":
    main()

#main.py
import owen 
import time
import hugo
#import brocoli
import clement

'''' 
reader_2 = csv.DictReader(open('logins.csv','r'))

logins=[dict(row) for row in reader_2]'''

#def round():
  #return

def main():
  ptsjoueur=0
  ptsia=0
  ecrania = owen.ecran()
  difficulte=owen.difficulte()

  ecranj=clement.test_ia()#ajout des bateaux
  ecrania=clement.test_j()
  
  pIA=[ecrania,'recherche']#ensemble de paramètres pour l'ia, le premier étant sa matrice de jeu et le 2eme son état, 'recherche','touché' ou 'traque', et certaines valeurs seront ajoutées après certaines phases: la cible, l'orientation de la cible, puis le parametre long, voir fonction traque()
  ct=0
  while ptsjoueur!=17 and ptsia !=17:#17=place totale prise par les bateaux
    print(f'tour {ct}')
    a=hugo.tir_joueur(ecranj)#demande ou le joueur veut tirer, retourne la matrice changée et si ça a touché
    ptsjoueur=owen.verifpoints(ecranj)
    print('joueur :%spts' % ptsjoueur)
    ecranj=a[0]
    print(owen.afficher(ecranj))
    print('----------------------------')
    b=owen.tiria(pIA,difficulte)
    ecrania=b[0]
    pIA=b[1]
    time.sleep(2)
    print(owen.afficher(ecrania))
    ptsia=owen.verifpoints(ecrania)
    print('ia : %s pts' % ptsia)
    print('----------------------------')
    ct+=1
    time.sleep(2)

if __name__ == "__main__":
    main()

    

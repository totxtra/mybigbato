import owen
import brocoli
import clement
import pyflemme
import csv
import owen
reader_2 = csv.DictReader(open('logins.csv','r'))
logins=[dict(row) for row in reader_2]


def login() :
  print("Que voulez vous faire ?")
  #Demande a l'utilisateur pour savoir ce qu il veut faire : s'inscrire ou se connecter 
  test_a =0
  while test_a ==0 :
    connect = pyflemme.intput("Taper 1 pour se connecter et 0 pour créer un compte : ")
    if connect!= 0 and connect != 1 :
      print("Entrez 1 ou 0 ")
    else :
      test_a = 1
  return connect



def register(connect) :
  #vérifie si l utilisateur veut se créer un compte
  if  connect == 0 :
    test_b=0
    while test_b ==0 :
      test_c = 0
      #demande du pseudo
      pseudo = input("Saisissez votre nom d'utilisateur : ")
      
      for i in logins :
        
        #vérification : le pseudo est utilisé ?
        if pseudo == i["Nom"] :
          print("Erreur ce nom est déja pris !")
          test_c = 1
          
      if " " in pseudo :
        #vérification : le pseudo contient des espaces ?
        print("Erreur, les espaces ne sont pas acceptés")
        test_c = 1

      if len(pseudo) <= 2 :
        #vérification : le pseudo contient au moins 3 caractère ?
        print("Erreur, votre pseudo a moins de trois carctère. ")
        test_c = 1
      if test_c == 0 :
        #Le pseudo est valide
        print(f"Le pseudo {pseudo} a été accepté.") 
        test_b = 1
  
  
  
  #vérifie si l utilisateur veut se connecter a un compte
  if  connect == 1 :
    test_d=0
    while test_d== 0 :
      test_e = 0
      #demande du pseudo
      pseudo = input("Saisissez votre nom d'utilisateur : ")
      for i in logins :
        
        #vérification : le pseudo est utilisé ?
        if not(pseudo == i["Nom"]) :
          print("Erreur ce nom n’existe pas .")
          test_e = 1
        
        else :
            test_f = 0
            while test_f ==0 :

              password = input("Entrer votre mot de passe : ")

              if pseudo == i["Mdp"] :
                print("Mot de passe accepté .")
                test_f = 1
              
              else :
                print("Mot de passe éroné")
                pass


  
  
  
  
  
  
  
    pass


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
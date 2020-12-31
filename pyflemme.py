def intput(c) :
    x=0
    while x==0 :
        try :
            v = int(input(c))
            x=1
        except :
            print("Erreur vous n'avez pas entré de nombre entier")
    return v

def floatput(c) :
    x=0
    while x==0 :
        try :
            v = float(input(c))
            x=1
        except :
            print("Erreur vous n'avez pas entré de nombre réel")
    return v

def boolput(c) :
    x=0
    while x==0 :
        try :
            v = bool(input(c))

            x=1
        except :
            print("Erreur vous n'avez pas entré de bouléen")
    return v

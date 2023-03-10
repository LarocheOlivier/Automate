# Ce fichier contient toutes les fonctions utilisées dans ce programme

import string

# =========COULEURS UTILISEES POUR LES MESSAGE DESTINE A L'UTILISATEUR=========
# titre
JAUNE = '\033[33m'
# error
ROUGE = '\033[31m'
# success
VERT = '\033[32m'
# reset de couleur
RES = '\033[39m'


# ==============================================================================

# Protection lors de la saisie de l'utilisateur
def protect_choix(nbch):
    while True:
        try:
            ch = int(input(f"Saisir un choix entre 1 et {nbch}: "))
            while (ch < 1) or (ch > nbch):
                ch = int(input(ROUGE + f"Saisir un choix entre 1 et {nbch}: ") + RES)
            break
        except ValueError:
            print(ROUGE + "Vous devez mettre un choix valable : " + RES)
    return ch


# Permet d'ouvrir et d'enregistrer chaque automate contenu dans les fichiers
def stock_automate(txt):
    with open(txt, 'r') as f:
        contenu = f.readlines()
    with open(txt, 'w') as f:
        for line in contenu:
            liste = line.split(",")
            liste[-1] = liste[-1].strip()
            Oldline = ",".join(str(x) for x in liste)
            f.write(f"{Oldline}\n")


# Fonction permettant de récupérer les informations du fichier voulu
def lire_fichier(x):
    #Définission de la variable fichier en fonction du numéro de l'automate saisie
    fichier = ""
    if (x == 1):
        fichier = "1-1.txt"
    elif (x == 1):
        fichier = "1-2.txt"
    #Ouvre le fichier correspondant et stock les données dans une liste
    with open(fichier, "r") as f:
        lines = f.read().split('\n')

    return lines

#Fonction permettant de retourner la liste des lettres de l'alphabet de l'automate (a = nb symb.)
def liste_symbs_function(a):
    liste_alph = string.ascii_lowercase
    liste_alph = list(liste_alph)
    liste_symbs = []
    for n in range(0, int(a)):
        liste_symbs.append(liste_alph[n])

    return liste_symbs

# Fonction permettant de récupérer la liste des états (a = nb états)
def liste_etats_function(a):
    print(a)
    liste_etats = []
    for i in range(0, int(a)):
        liste_etats.append(i)

    return liste_etats

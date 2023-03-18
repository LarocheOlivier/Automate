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

#Fonction qui renvoie un nombre, 0 si le nombre entré est pair et 1 si le nombre entré est impair
def pair_impair(nb):
    x = 3
    if nb % 2 == 0:
        x = 0
    else:
        x = 1

    return x

# Fonction qui renvoie le nombre de caractères d'une chaine de caractère
def count_char_str(str):
    nb = 0
    for i in range(0,len(str)):
        nb += 1

    return nb

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


# Fonction permettant de retourner les informations du fichier voulu
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

# Fonction permettant de retourner la liste des états (a = nb états)
def liste_etats_function(a):
    liste_etats = []
    for i in range(0, int(a)):
        liste_etats.append(i)

    return liste_etats

#Fonction permettant de couper la ligne des états INITIAUX/TERMINAUX pour ne retourner qu'une liste des états INITIAUX/TERMINAUX
def cutline_liste_etats(nb_etats, line):

    # Liste etats
    liste_etats = []

    print("")
    # Calcul l'indice maximale par rapport au nombre d'états)
    indice_max = 2*int(nb_etats)

    # Boucle permettant d'ajouter à la liste des états qu'on veut
    for i in range(2, indice_max+2, 2):
            liste_etats.append(line[i])

    return liste_etats

#Fonction permettant de retourner la liste des états terminaux ET initiaux
def liste_init_and_term(liste_init, liste_term):

    liste_init_term = []
    for x in liste_init:
        if x in liste_term:
            liste_init_term.append(x)

    return liste_init_term


#Fonction retournant la liste des états seulement initiaux/terminaux
def only_init_or_term(liste_init_or_term, liste_term_and_init):

    liste_only_init_or_term = []
    liste_init_or_term = set(liste_init_or_term)
    liste_term_and_init = set(liste_term_and_init)

    # Retourne une liste composé des états seulement init/term (différence avec la liste contenant les états init ET term
    liste_only_init_or_term = list(liste_init_or_term - liste_term_and_init)

    return liste_only_init_or_term

# Fonction permettant de retourner la liste de la ligne d'un automate pour l'AFFICHAGE (tout bien)
def make_ligne(i,nb_symb,nb_trans,liste_trans,liste_term,liste_init,liste_init_term):
    # Créer une liste contenant le bon nombre d'indice pour la ligne
    ligne = [" "] * int(nb_symb+1)
    # Boucle permettant de parcourir tous les caractères de toutes les transitions
    for a in range(0, nb_trans):
        # Si le premier caractère correspond à l'état i, alors ajouter l'état correspondant à la transition
        if int(liste_trans[a][0]) == i:
            # Donne l'indice correspondant à la lettre de la transition pour la ligne
            ind = ord(liste_trans[a][1]) - 96
            # Si l'élément de l'indice est déjà rempli par un état, alors ajouter le caractère
            if ligne[ind] != " ":
                chaine = ligne[ind]
                chaine = chaine + liste_trans[a][2]
                ligne[ind] = chaine
            # Sinon, initialiser la valeur à l'indice correspondant de la liste de la ligne
            else:
                ligne[ind] = liste_trans[a][2]
    #Permet d'ajouter la/les bonnes lettres à l'état, initial, terminal ou les deux
    #Permet d'initialiser le première indice à l'état associer avec la lettre
    ligne[0] = add_letters(i, liste_term, liste_init, liste_init_term) + str(i)

    #S'il n'y a pas de transitions à une case dans la ligne (pas de transitions), alors on met un tiret
    for u in range(len(ligne)):
        if ligne[u] == " ":
            ligne[u] = "-"

    return ligne

#-----------------------------------------------------------------------------------------------------------------------------------------------
#Fonction permettant d'ajouter la/les lettres correspondantes aux éléments d'une liste s'il s'agit d'une entrée, sortie ou les deux
def add_letters(i,liste_term,liste_init,liste_init_term):
    chaine = ""
    for k in range(0, len(liste_init)):
        if int(liste_init[k]) == i:
            chaine = "E-"
    for k in range(0, len(liste_term)):
        if int(liste_term[k]) == i:
            chaine = "S-"
    for k in range(0, len(liste_init_term)):
        if int(liste_init_term[k]) == i:
            chaine = "S-E-"

    return chaine
#---------------------------------------------------------------------------------------------------------------------

# Retourne la liste qui est la soustraction de la liste des états et la liste des états terminaux
def complementarisation(liste_etat_term,liste_etats):

    liste_finale = []

    # Parcours des deux listes, si un état de la liste des états ne se trouve pas dans la liste des états terminaux on ajoute à la liste finale
    for i in range(0,len(liste_etats)):
        for j in range(0,len(liste_etat_term)):
            if liste_etats[i] != int(liste_etat_term[j]):
                liste_finale.append(liste_etats[i])

    return liste_finale
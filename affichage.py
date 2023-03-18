# Ce fichier contient toutes les fonctions d'affichage de ce programme

from functions import *


# Fonction permettant d'afficher le menu principale
def print_main_menu():
    print("==================================================================\n")
    print("                  MANIPULATION D'AUTOMATES FINIS                  \n")
    print("==================================================================")
    print("Nous vous proposons une liste de 8 automates finis !\n\nQuel automate souhaitez-vous utiliser ?")

#------------------------------------------------------------------------------------------------------------------------------------FONCTION D'AFFICHAGE D'AUTOMATES-------------------------------------------------------------------------------------------

#Fonction affichant la première ligne du tableau, soit la liste des symboles
def print_symb_line(liste_symb,nb_etat):
    nb_symb = len(liste_symb)  # NB SYMBOLES
    char_espace = " "
    char_tiret = "-"

    # Si x = 1, nombre impair sinon pair
    x = pair_impair(int(nb_etat))
    # Liste des espaces
    liste_space = []

    space_av = 0
    space_ap = 0
    if x == 1:
        space_av = int((int(nb_etat) / 2 - 0.5) + 2)
        space_ap = int((int(nb_etat) / 2 - 0.5) + 2)
    else:
        space_av = int(int(nb_etat) / 2)
        space_ap = int((int(nb_etat) / 2) + 2)
    space_total = space_av + space_ap + 1
    liste_space.append(space_av)
    liste_space.append(space_ap)
    liste_space.append(space_total)

    ligne_rest = int((space_av + space_ap + 4) * nb_symb + 1) * char_tiret
    # Trait 1
    print(int((space_av + space_ap + 3)) * char_espace, end=" ")
    print(ligne_rest)
    print(int((space_av + space_ap + 3)) * char_espace,end=" ")

    for i in range(0, nb_symb):
        print("|", end=" ")
        print((liste_space[0] - 1) * char_espace, end=" ")
        print(liste_symb[i], end=" ")
        print((liste_space[1] - 1) * char_espace, end=" ")
    print("|")
    #Trait 2

    #Colonne 0 (états), invariant
    ligne_col_0 = (int(space_total) + 3) * char_tiret
    print(ligne_col_0, end="")
    print(ligne_rest)
    ligne_tot = ligne_col_0 + ligne_rest
    liste_space .append(ligne_tot)

    return liste_space


# Fonction permettant d'afficher les automates sous forme de tableau
def print_automate(liste_symb, liste_etats_initiaux, liste_etats_terminaux, liste_trans, nb_etats):

    # Affiche la ligne des symboles et initialise la liste des espaces [0]
    liste_space = print_symb_line(liste_symb, nb_etats)

    space_char = " "

    #Nombre
    nb_symb = len(liste_symb)
    nb_trans = len(liste_trans)

    #Liste des états initiaux ET terminaux
    liste_init_term = liste_init_and_term(liste_etats_initiaux, liste_etats_terminaux)

    #Liste contenant les états seulement initiaux
    liste_init = only_init_or_term(liste_etats_initiaux, liste_init_term)

    #Liste contenant les états seulement terminaux
    liste_term = only_init_or_term(liste_etats_terminaux, liste_init_term)

    # Boucle permettant de créer le bon nombre de ligne et la ligne correspondante à l'état
    for i in range(0, int(nb_etats)):
        ligne = make_ligne(i, nb_symb, nb_trans, liste_trans, liste_term, liste_init, liste_init_term)
        for y in range(len(ligne)):
            # Initialise une chaine de caractère de l'élément de la liste de la boucle
            str = ligne[y]
            # Compte le nombre de caractère de cette chaine
            nb_char = count_char_str(str)

            print("| ", end=" ")
            print(ligne[y], end=" ")
            print((liste_space[2] - 2 - int(nb_char)) * space_char, end=" ")
        print("|")
        print(liste_space[3])

#------------------------------------------------------------------------------------------------------------------------------------QUEL AUTOMATE ILS VEULENT TRAVAILLER---------------------------------------------------------------------------------------

# Fonction permettant de procéder à la lecture du fichier concerné
def exec_ch_main(ch):
    if ch == 1:

        #----------------------------------------RECUPERATION DES INFORMATIONS DE L'AUTOMATE SOUS FORME DE VARIABLES ET LISTES----------------------------
        # Liste contenant chaque ligne par indice
        liste_lignes = lire_fichier(1)
        nb_lignes = len(liste_lignes)

        # Permet d'obtenir la liste des symboles de l'automate
        nb_symbs = liste_lignes[0]                                                                  # NB SYMBOLES
        liste_symbs = liste_symbs_function(nb_symbs)                                                # LISTE DES SYMBOLES (ALPHABET) DE L'AUTOMATE

        # Permet d'obtenir la liste des états
        nb_etats = liste_lignes[1]                                                                  # NB ETATS
        liste_etats = liste_etats_function(nb_etats)                                                # LISTE DES ETATS (de 0 à n) DE L'AUTOMATE

        # Liste contenant la ligne des nb et etats initiaux (line initiaux est une liste)
        line_initiaux = liste_lignes[2]
        nb_etats_initiaux = line_initiaux[0]                                                         # NB ETATS INITIAUX
        liste_etats_initiaux = cutline_liste_etats(nb_etats_initiaux, line_initiaux)                 # LISTE DES ETATS INITIAUX

        # Liste contenant la ligne des nb et etats initiaux (line initiaux est une liste)
        line_terminaux = liste_lignes[3]
        nb_etats_terminaux = line_terminaux[0]                                                      # NB ETATS TERMINAUX
        liste_etats_terminaux= cutline_liste_etats(nb_etats_terminaux, line_terminaux)              # LISTE DES ETATS TERMINAUX

        # Création d'une liste contenant seulement les transitions de l'automate
        liste_trans = []
        for i in range(5, nb_lignes):                                                               # LISTE TRANSITIONS
            liste_trans.append(liste_lignes[i])

        nb_trans = len(liste_trans)                                                                 # NB TRANSITIONS

        #-------------------------AFFICHAGE DE L'AUTOMATE----------------------------------------------
        print_automate(liste_symbs, liste_etats_initiaux, liste_etats_terminaux, liste_trans, nb_etats)

        #---------------------------Complémentarisation------------------------------------------------

        # Faire la vérification si déterministe et complet

        # COMPLEMENTARISATION DE L'AUTOMATE ET AFFICHAGE
        # Retourne la liste des états terminaux

        print("Complémentarisation :\n")
        # La liste des états initiaux est sous forme de string et nom de int,
        # la fonction map convertit celle-ci
        liste_etats_initiaux = list(map(int, liste_etats_initiaux))
        liste_etats_terminaux = complementarisation(liste_etats_terminaux, liste_etats)
        print_automate(liste_symbs, liste_etats_initiaux, liste_etats_terminaux, liste_trans, nb_etats)

        #----------------------------------------------------------------------------------------------

        # elif ch == 2 :
        quit()

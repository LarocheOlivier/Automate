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
def print_symb_line(liste_symb):
    nb_symb = len(liste_symb)  # NB SYMBOLES
    print("         ", end=" ")
    space = 13 * nb_symb + 1
    print(space * "-")
    print("         ", end=" ")
    for i in range(0, nb_symb):
        print("|    ", end=" ")
        print(liste_symb[i], end=" ")
        print("    ", end=" ")
    print("|")
    print("----------+", end="")
    print((space-1) * "-")

# Fonction permettant d'afficher les automates sous forme de tableau
def print_automate(liste_symb, liste_etats_initiaux, liste_etats_terminaux, liste_trans, nb_etats):

    # Affiche la ligne des symboles
    print_symb_line(liste_symb)

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
        ligne = make_ligne(i, nb_symb, nb_trans, liste_trans,liste_term,liste_init,liste_init_term)
        for y in range(len(ligne)):
            print(ligne[y], end=" ")
        print("\n------------------------------------------\n")

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

        #----------------------------------------------------------AFFICHAGE-----------------------------------------------------------------------
        print_automate(liste_symbs, liste_etats_initiaux, liste_etats_terminaux, liste_trans, nb_etats)


        # elif ch == 2 :
        quit()

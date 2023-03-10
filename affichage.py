# Ce fichier contient toutes les fonctions d'affichage de ce programme

from functions import *


# Fonction permettant d'afficher le menu principale
def print_main_menu():
    print("==================================================================\n")
    print("                  MANIPULATION D'AUTOMATES FINIS                  \n")
    print("==================================================================")
    print("Nous vous proposons une liste de 8 automates finis !\n\nQuel automate souhaitez-vous utiliser ?")


# Fonction permettant de procéder à la lecture du fichier concerné
def exec_ch_main(ch):
    if ch == 1:

        #---------------------------------------------------------------RECUPERATION DES INFORMATIONS DE L'AUTOMATE SOUS FORME DE VARIABLES ET LISTES----------------------------------------------------------------
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
        liste_etats_initiaux = cutline_liste_etats(nb_etats_terminaux, line_terminaux)              # LISTE DES ETATS TERMINAUX

        # Création d'une liste contenant seulement les transitions de l'automate
        liste_trans = []
        for i in range(5, nb_lignes):                                                               # LISTE TRANSITIONS
            liste_trans.append(liste_lignes[i])

        nb_trans = len(liste_trans)                                                                 # NB TRANSITIONS
        #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # elif ch == 2 :
        quit()

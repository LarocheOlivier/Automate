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

        # Liste contenant chaque ligne par indice
        liste_lignes = lire_fichier(1)
        nb_indices_lignes = len(liste_lignes)

        # Permet de visualiser les valeurs de la liste
        """
        for i in range(0, nb):
            print(liste[i])
        """

        # Permet d'obtenir la liste des symboles de l'automate
        nb_symbs = liste_lignes[0]
        liste_symbs = liste_symbs_function(nb_symbs)

        # Permet d'obtenir la liste des états
        nb_etats = liste_lignes[1]
        liste_etats = liste_etats_function(nb_etats)

        nb_etats_init = liste_lignes[2]
        nb_etats_term = liste_lignes[3]
        nb_trans = liste_lignes[4]

        # Création d'une liste contenant seulement les transitions de l'automate
        liste_trans = []
        for i in range(5, nb_indices_lignes):
            liste_trans.append(liste_lignes[i])

        # elif ch == 2 :
        quit()

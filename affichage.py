# Ce fichier contient toutes les fonctions d'affichage de ce programme
import os

from functions import *
from standardisation import *
from déterminisation import *

# Fonction permettant d'afficher le menu principale
def print_main_menu():
    print("\n==============================================================================================================\n")
    print("                                     MANIPULATION D'AUTOMATES FINIS                                EFREI PARIS\n")
    print("Programme réalisé par Otto Sander, Olivier Laroche, Arthur Castelain, Constance Walusiak et Ariane Mailanandam")
    print("==============================================================================================================")
    print("Dans ce programme, vous allez répondre aux questions par Y,N et Q ou par des entiers :\nY : Oui\nN : Non\nQ : Pour revenir au menu principal")
    print("==============================================================================================================\n")
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


# Fonction permettant d'afficher les automates sous forme de tableau (stand == 1 si standardisé et == 0 sinon)
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

    liste_etats = get_liste_etats(liste_trans)

    #Si la liste initial n'est pas égal à 0, alors on affiche avant les lignes des états initiaux
    if len(liste_init) != 0:
        #Affiche d'abord les lignes des états initiaux
        for i in range(0, len(liste_init)):
            ligne = make_ligne(liste_init[i], nb_symb, nb_trans, liste_trans, liste_term, liste_init, liste_init_term)
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

        liste_etats_without_init = []
        #Puis ensuite afficher les autres états
        for i in range (0,len(liste_etats)):
            for j in range (0,len(liste_init)):
                if liste_etats[i] != liste_init[j]:
                    liste_etats_without_init.append(liste_etats[i])
        liste_etats_without_init = list(set(liste_etats_without_init))

        for i in range(0, len(liste_etats_without_init)):
            ligne = make_ligne(liste_etats_without_init[i], nb_symb, nb_trans, liste_trans, liste_term, liste_init, liste_init_term)
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
    else:
        #S'il n'y a pas d'état initiaux et que intiaux et terminaux alors...
        for i in range(0, len(liste_etats)):
            ligne = make_ligne(liste_etats[i], nb_symb, nb_trans, liste_trans, liste_term, liste_init,
                               liste_init_term)
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
#========================================================================================================================================================================

def all_process(ch,nb_symbs,liste_symbs,nb_etats,liste_etats,nb_etats_initiaux,liste_etats_initiaux,nb_etats_terminaux,liste_etats_terminaux,liste_trans,nb_trans):

    # Variable permettant d'afficher un automate standardisé, (Si stand == 0, l'automate n'est pas standardisé, sinon stand == 1
    stand = 0

    print("\nVoici l'automate que vous avez choisi :\n")

    # Affichage de l'automate
    print_automate(liste_symbs, liste_etats_initiaux, liste_etats_terminaux, liste_trans, nb_etats)

    deter = False

    # Vérifie si l'automate est standard
    info_stand = est_standard(nb_etats_initiaux, nb_trans, liste_etats_initiaux, liste_trans)
    if est_deterministe(ch) == 1:
        deter = True

    # Affichage des informations
    print("Voici les informations liées à cet automate :\n")
    print("Standart : ", info_stand)
    print("Déterministe : ", deter)
    print("Complet : ",est_complet())

    choice = input("\nCe choix vous convient-il ?\nRépondez par Y/N/Q : ")

    # Si l'utilisateur veut changer d'automate
    if choice == "N":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print_main_menu()
        ch = protect_choix(8)
        exec_ch_main(ch)

    # Sinon on lance tout pour cet automate
    else:

        #----------------------------------------------STANDARDISATION--------------------------------------------------------------------------------------------------------------------------
        # Si l'automate n'est pas standard
        while info_stand == False:
            choice = input("\nVoulez-vous le standardiser sachant qu'il ne l'est pas ?\nRépondez par Y/N/Q : ")
            if choice == "Y":

                print("\nVoici votre automate standardisé :\n")
                liste_standard = standardiser_automate(liste_etats, liste_trans,nb_trans, liste_etats_initiaux, nb_etats_initiaux, liste_etats_terminaux, nb_etats_terminaux)
                liste_trans_stand = liste_standard[1]
                liste_etats_initiaux_stand = liste_standard[2]
                liste_etats_terminaux_stand = liste_standard[3]

                print_automate(liste_symbs, liste_etats_initiaux_stand, liste_etats_terminaux_stand, liste_trans_stand, nb_etats)

                print("\nCet automate est maintenant standard !")
                info_stand = True
            elif choice == "N":
                # Si l'automate est déjà standart, on sort de la boucle
                info_stand = True
            elif choice == "Q":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print_main_menu()
                ch = protect_choix(8)
                exec_ch_main(ch)

        #-------------------------------------Déterminisation et Complétion----------------------------------------------------------------------------------------------------------------------
        if est_deterministe(ch) == 0 and est_complet() == 0:
            choice = input("Sachant que votre automate n'est ni déterministe ni complet, voulez-vous le déterminiser et le compléter ?\nRépondez par Y/N/Q : ")

            #Si l'utilisateur veut déterminiser et compléter l'automate
            if choice == "Y":

                print("\nVoici votre automate standardisé et complété :\n")
        # if est_deterministe(ch) == 1:
        #     if est_complet()==1:
        #         print_automate(liste_symbs, liste_etats_initiaux, liste_etats_terminaux, liste_trans, nb_etats)
        #     else :
        #         liste_trans = completion(1)
        #         print_automate(liste_symbs, liste_etats_initiaux, liste_etats_terminaux, liste_trans, nb_etats+1)
        # else :
                liste_symbs_f, New_Etat_Init, Liste_Etat_t_f, Newlist_trans, nbetatf = determinisatation(liste_symbs,liste_etats_initiaux,liste_etats_terminaux,liste_trans,nb_etats)
                print_automate(liste_symbs_f, New_Etat_Init, Liste_Etat_t_f, Newlist_trans, nbetatf)

            elif choice == "N":
                pass
            elif choice == "Q":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print_main_menu()
                ch = protect_choix(8)
                exec_ch_main(ch)

        #--------------------------------------------------COMPLEMENTAIRE----------------------------------------------------------------------------------------------------------------------
        choice = input("\nVoulez-vous obtenir l'automate complémentaire de l'automate initial ?\nRépondez par Y/N/Q : ")

        #Si l'utilisateur veut l'automate complémentaire, alors :
        if choice == "Y":
            print("\nComplémentarisation :\n")

            # La liste des états initiaux est sous forme de string et nom de int,
            # la fonction map convertit celle-ci
            liste_etats_terminaux = complementarisation(liste_etats_terminaux, liste_etats)

            # Affiche l'automate complémentaire
            print_automate(liste_symbs, liste_etats_initiaux, liste_etats_terminaux, liste_trans, nb_etats)

        #Si l'utilisateur ne veut pas le complémentaire ou quitter, alors retour au menu principale
        elif choice == "N" or choice == "Q":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print_main_menu()
            ch = protect_choix(8)
            exec_ch_main(ch)

#===============================================================================================================================================================================

# Fonction permettant de procéder à la lecture du fichier concerné
def exec_ch_main(ch):
    # Liste infos = [nb_symbs,   liste_symbs,    nb_etats,   liste_etats,    nb_etats_initiaux,  liste_etats_initiaux,   nb_etat_terminaux,  liste_etats_terminaux,  liste_trans,    nb_trans]
    liste_infos = get_infos(ch)

    # Variable par info
    nb_symbs = liste_infos[0]
    liste_symbs = liste_infos[1]
    nb_etats = liste_infos[2]
    liste_etats = liste_infos[3]
    nb_etats_initiaux = liste_infos[4]
    liste_etats_initiaux = liste_infos[5]
    nb_etats_terminaux = liste_infos[6]
    liste_etats_terminaux = liste_infos[7]
    liste_trans = liste_infos[8]
    nb_trans = liste_infos[9]

    # Effectue tous le processus de l'algorithme
    all_process(ch,nb_symbs, liste_symbs, nb_etats, liste_etats, nb_etats_initiaux, liste_etats_initiaux, nb_etats_terminaux, liste_etats_terminaux, liste_trans, nb_trans)

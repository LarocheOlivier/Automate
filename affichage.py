# Ce fichier contient toutes les fonctions d'affichage de ce programme

from functions import *
from standardisation import *
from déterminisation import *
from complementarisation import *
from reconnaissance_mots import *

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
def print_symb_line(liste_symb,nb_etat,space_max):

    nb_symb = len(liste_symb)
    char_espace = " "
    char_tiret = "-"

    #Ligne de tiret entre les symboles
    ligne_rest = int((space_max+1) * (nb_symb)) * char_tiret
    ligne_rest = ligne_rest + '-'


    # Trait 1 :
    print((space_max + 1)  * char_espace, end="")
    print(ligne_rest)

    #Ligne Symbole :
    print((space_max + 1)  * char_espace,end="")

    for i in range(0, nb_symb):
        print("| ", end="")
        print(liste_symb[i], end="")
        print((space_max - 2) * char_espace, end="")
    print("|")

    #Trait 2
    ligne_tot = ligne_rest + (char_tiret * (space_max + 1))
    print(ligne_tot)

    return ligne_tot

# Fonction permettant d'afficher les automates sous forme de tableau (stand == 1 si standardisé et == 0 sinon)
def print_automate(liste_symb, liste_etats_initiaux, liste_etats_terminaux, liste_trans, nb_etats):

    #Liste des états de l'automate
    liste_etats = get_liste_etats(liste_trans)

    #Donne le nombre d'espace maximal qu'il faut pour chaque case
    space_max = get_bigger_char(liste_etats) + 8

    # Affiche la ligne des symboles et renvoie la ligne séparant les états de tirets
    ligne_tiret_tot = print_symb_line(liste_symb, nb_etats,space_max)
    space_max -= 1

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

                print("| ", end="")
                print(ligne[y], end="")
                #Pour retirer l'espace en trop
                space_ap = space_max - nb_char
                print(space_ap * space_char, end="")
            print("|")
            print(ligne_tiret_tot)


        liste_etats_without_init = discommon_member(liste_init,liste_etats)

        for i in range(0, len(liste_etats_without_init)):
            ligne = make_ligne(liste_etats_without_init[i], nb_symb, nb_trans, liste_trans, liste_term, liste_init, liste_init_term)
            for y in range(len(ligne)):
                # Initialise une chaine de caractère de l'élément de la liste de la boucle
                str = ligne[y]
                # Compte le nombre de caractère de cette chaine
                nb_char = count_char_str(str)

                print("| ", end="")
                print(ligne[y], end="")
                # Pour retirer l'espace en trop
                space_ap = space_max - nb_char
                print(space_ap * space_char, end="")
            print("|")
            print(ligne_tiret_tot)

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

                print("| ", end="")
                print(ligne[y], end="")
                # Pour retirer l'espace en trop
                space_ap = space_max - nb_char
                print(space_ap * space_char, end="")
            print("|")
            print(ligne_tiret_tot)
#========================================================================================================================================================================

def all_process(ch,nb_symbs,liste_symbs,nb_etats,liste_etats,nb_etats_initiaux,liste_etats_initiaux,nb_etats_terminaux,liste_etats_terminaux,liste_trans,nb_trans):

    # Variable permettant d'afficher un automate standardisé, (Si stand == 0, l'automate n'est pas standardisé, sinon stand == 1
    stand = 0

    print("\nVoici l'automate que vous avez choisi :\n")

    # Affichage de l'automate
    print_automate(liste_symbs, liste_etats_initiaux, liste_etats_terminaux, liste_trans, nb_etats)

    # Vérifie si l'automate est standard
    info_stand = est_standard(nb_etats_initiaux, nb_trans, liste_etats_initiaux, liste_trans)
    deter = est_deterministe(ch)
    comp = est_complet_VF(liste_symbs, liste_trans)

    #Phrase standart
    if info_stand == True:
        info_stand = "Oui"
    else:
        info_stand = "Non"

    #Phrase complet
    if comp == 0:
        comp = "Non"
    else:
        comp = "Oui"

    #Phrase déterministe
    if deter == 1:
        deter = "Oui"
    elif deter == 2:
        deter = "Non, car il y a plusieurs états initiaux"
    elif deter == 3:
        deter = "Non, car il existe plusieurs états pour un symbole pour au moins une transition"
    elif deter == 4:
        deter = "Non, car il y a plusieurs états initiaux et il existe plusieurs états pour un symbole pour au moins une transition"

    # Affichage des informations
    print("\nVoici les informations liées à cet automate :\n")
    print("Standart : ", info_stand)
    print("Déterministe : ", deter)
    print("Complet : ",comp)

    info_stand = est_standard(nb_etats_initiaux, nb_trans, liste_etats_initiaux, liste_trans)

    choice = input("\nCe choix vous convient-il ?\nRépondez par Y/N/Q : ")

    # Si l'utilisateur veut changer d'automate
    if choice == "N":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print_main_menu()
        ch = protect_choix(39)
        exec_ch_main(ch)

    # Sinon on lance tout pour cet automate
    else:
        next = False
        choice = input("\nVoulez-vous effectuer un test de reconnaissance de mot sur cet automate ?\nRépondez par Y/N/Q : ")
        while next == False:
            if choice == "Y":
                choix_mot(liste_etats_initiaux,liste_trans,liste_etats_terminaux)
                break
            elif choice == "Q":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print_main_menu()
                ch = protect_choix(39)
                exec_ch_main(ch)
            elif choice == "N":
                break
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

                info_stand = True
            elif choice == "N":
                # Si l'automate est déjà standart, on sort de la boucle
                info_stand = True
            elif choice == "Q":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print_main_menu()
                ch = protect_choix(39)
                exec_ch_main(ch)

        #-------------------------------------Déterminisation et Complétion----------------------------------------------------------------------------------------------------------------------
        #Si l'automate n'est pas complet ET pas déterministe (Va déterminiser et compléter
        if (est_deterministe(ch) == 2 or est_deterministe(ch) == 3 or est_deterministe(ch) == 4):
            print("\nSachant que votre automate n'est pas déterministe ni complet, voici votre automate déterminisé et completé par la suite si besoin :\n")

            liste_symbs_f, New_Etat_Init, Liste_Etat_t_f, Newlist_trans, nbetatf = determinisatation(liste_symbs,liste_etats_initiaux,liste_etats_terminaux,liste_trans,nb_etats)
            print_automate(liste_symbs_f, New_Etat_Init, Liste_Etat_t_f, Newlist_trans, nbetatf)

        #Si notre automate est déjà déterministe mais pas complet
        elif est_deterministe(ch) == 1 and est_complet_VF(liste_symbs,liste_trans) == 0 :
            print("\n Sachant que votre automate est déjà déterministe mais pas complet, voici votre automate complet :\n")

            liste_trans = completion(liste_symbs, liste_trans)
            print_automate(liste_symbs, liste_etats_initiaux, liste_etats_terminaux, liste_trans, nb_etats)

            #--------------------------------------------------COMPLEMENTAIRE----------------------------------------------------------------------------------------------------------------------
        print("\nComme votre automate était déjà déterministe et complet ou qu'il a été déterminisé et complété si besoin par la suite,\nvous avez la possibilité d'obtenir de language complémentaire,\n")
        choice = input("\nVoulez-vous obtenir l'automate complémentaire ?\nRépondez par Y/N/Q : ")

        #Si l'utilisateur veut l'automate complémentaire, alors :
        if choice == "Y":

            #Si l'automate initial était déjà déterministe et complet
            if est_deterministe(ch) == 1 and est_complet_VF(liste_symbs,liste_trans) == 1:
                print("\nComplémentarisation de l'automate initial :\n")

                liste_etats_terminaux = complementarisation(liste_etats_terminaux, liste_etats)

                # Affiche l'automate complémentaire
                print_automate(liste_symbs, liste_etats_initiaux, liste_etats_terminaux, liste_trans, nb_etats)

            #Si l'automate a dû être déterminisé et complété
            elif (est_deterministe(ch) == 2 or est_deterministe(ch) == 3 or est_deterministe(ch) == 4):
                print("\nComplémentarisation de l'automate déterminisé et complété :\n")

                #Récupération liste des nouveaux états
                liste_etats_comp_det = []
                for i in range(0,len(Newlist_trans)):
                    liste = get_numbers_trans_av_ap(Newlist_trans[i])
                    liste_etats_comp_det.append(liste[0])
                    liste_etats_comp_det.append(liste[1])

                liste_etats_comp_det = list(set(liste_etats_comp_det))

                liste_etats_terminaux = complementarisation(Liste_Etat_t_f, liste_etats_comp_det)

                # Affiche l'automate complémentaire
                print_automate(liste_symbs_f, New_Etat_Init, liste_etats_terminaux, Newlist_trans, nbetatf)

            #Si notre automate était déjà déterministe mais pas complet
            elif est_deterministe(ch) == 1 and est_complet_VF(liste_symbs,liste_trans) == 0:
                print("\nComplémentarisation de l'automate complet :\n")

                liste_etats_terminaux = complementarisation(liste_etats_terminaux, liste_etats)

               # Affiche l'automate complémentaire
                print_automate(liste_symbs, liste_etats_initiaux, liste_etats_terminaux, liste_trans, nb_etats)


        #Si l'utilisateur ne veut pas le complémentaire ou quitter, alors retour au menu principale
        elif choice == "Q" or choice == "N":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print_main_menu()
            ch = protect_choix(39)
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

    if int(nb_symbs)== 0:
        print("\nCette automate reconnait tous les mots, il est donc impossible d'effectuer quelconque opération, retour au menu principal")
        print_main_menu()
        ch = protect_choix(39)
        exec_ch_main(ch)
    else:
        # Effectue tous le processus de l'algorithme
        all_process(ch,nb_symbs, liste_symbs, nb_etats, liste_etats, nb_etats_initiaux, liste_etats_initiaux, nb_etats_terminaux, liste_etats_terminaux, liste_trans, nb_trans)
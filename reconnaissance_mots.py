#Ce fichier permet la reconnaissance de mots

def choix_mot(liste_etats_initiaux, liste_trans, liste_etats_terminaux):
    choice = input("Inserer le mot : \nRépondez par Y/N : ")
    res = reconnaitre_mot(choice, liste_etats_initiaux, liste_trans, liste_etats_terminaux)
    if res == True:
        print("Le mot " + choice + "a bien ete reconnu ! " )
    else:
        print("Le mot " + choice + "n'a pas ete reconnu ! ")



def reconnaitre_mot(mot, liste_etats_initiaux, liste_trans, liste_etats_terminaux):
    etats_t = liste_etats_initiaux

    for symb in mot:
        nv_etats = []
        for etat_t in etats_t:
            for trans in liste_trans:
                if trans[0] == etat_t and trans[1] == symb:
                    nv_etats.append(trans[2])
        etats_t = nv_etats
    for etat_t in etats_t:
        for etat_terminal in liste_etats_terminaux:
            if etat_t == etat_terminal:
                return True
    return False
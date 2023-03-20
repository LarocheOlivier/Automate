# Ce fichier permet de standardiser un automate

# Fonction permettant de vérifier si l'automate est standard ou pas (bool)
def est_standard(nb_etats_initiaux, nb_trans, liste_etats_initiaux, transitions):
    for k in range(int(nb_etats_initiaux) + 1):

        # condition sur entrée - plus d'une entrée
        if len(liste_etats_initiaux[k]) > 1:
            return False

        # condition sur entrée - si y a pas d'entrée
        elif len(liste_etats_initiaux[k]) == 0:
            return True

        else:
            temp = 0
            for i in range(nb_trans - 1):
                if liste_etats_initiaux[0] == transitions[i][2]:
                    temp += 1

            if temp <= 1:
                return True
            else:
                return False


# fonction qui permet de standardiser l'automate
def standardiser_automate(liste_etats, liste_trans, nb_trans, liste_etats_initiaux, nb_etats_initiaux,
                          liste_etats_finaux, nb_etats_finaux):
    if est_standard(nb_etats_initiaux, nb_trans, liste_etats_initiaux, liste_trans) == False:

        # Mise à jour de la liste des états
        liste_etats_std = liste_etats.copy()
        liste_etats_std.insert(0, "i")

        # Mise à jour liste etat initial - condition : que 1 seule entrée
        liste_etats_initiaux_std = ["i"]

        # Mise à jour état final
        liste_etats_finaux_std = []
        for k in range(int(nb_etats_finaux)):
            for m in range(int(nb_etats_initiaux)):
                if liste_etats_finaux[k] == liste_etats_initiaux[m]:
                    liste_etats_finaux_std.insert(0, "i")

        if (liste_etats_finaux_std != None):  # cas si pas de reconnaissance du mot vide - les sorties restent les mêmes
            if liste_etats_finaux_std != "i":
                liste_etats_finaux_std = liste_etats_finaux.copy()

        # Mise à jour liste des transitions
        liste_trans_std = liste_trans.copy()
        for i in range(int(nb_trans) + 1):
            for j in range(int(nb_etats_initiaux) + 1):
                if liste_etats_initiaux[j - 1] == liste_trans[i - 1][0]:
                    liste_trans_std[i - 1] = "i" + liste_trans[i - 1][1:]
                else:
                    liste_trans_std[i - 1] = liste_trans[i - 1][:]

        l = 0
        for k in range(int(nb_trans) + 1):

            for j in range(int(nb_etats_initiaux)):
                if liste_etats_initiaux[j - 1] == liste_trans[k - 1][0]:
                    x = liste_trans[k - 1][:]
                    liste_trans_std.insert(l, x)

        return liste_etats_std, liste_trans_std, liste_etats_initiaux_std, liste_etats_finaux_std

    else:
        print("Automate déjà standard")
#Fichier permettant de retourner le complémentaire

# Retourne la liste qui est la soustraction de la liste des états et la liste des états terminaux
def complementarisation(liste_etat_term,liste_etats):

    liste_finale = []

    # Parcours des deux listes, si un état de la liste des états ne se trouve pas dans la liste des états terminaux on ajoute à la liste finale
    for i in range(0, len(liste_etats)):
        for j in range(0, len(liste_etat_term)):
            if str(liste_etats[i]) != str(liste_etat_term[j]):
                liste_finale.append(liste_etats[i])

    return liste_finale
from functions import*
from affichage import*

def est_deterministe(x):
    verif1 = 1
    verif2 = 1

    #récupération de la liste (automate à déterminisé)

    ottomate = lire_fichier(x)

# --------------------------------------------------------------------------------------------------------------------
        # Parcour de la liste automates afin d'y déterminer le nombre d'entrée pour y valider
        # ou non la première contrainte
        # Si il est présent une entrée alors la contrainte (propriété) est validée
        # Sinon elle ne l'ai pas est l'automate sera donc non déterministe
# --------------------------------------------------------------------------------------------------------------------

    for i in range(len(ottomate)):
        for j in range(len(ottomate[i])):

            # Indices contenant les entrées
            if i == 2 and j == 0 :
                # Vérification du nombre de sorti pour en déduire l'état de la première contrainte
                #Pas déterministe
                if (ottomate[i][j] != "1"):
                    verif1 = 0
                #Déterministe
                else :
                    verif1 = 1


#--------------------------------------------------------------------------------------------------------------------
        # Parcour et réduction de la liste automate, dans le but de pouvoir avoir les infos nous intéressant
        # Pour cela on élimine donc toute la partie comprenant le nombre d'entrée, sortie alphabet etc...
        #Ainsi on les stocke dans une nouvelle liste dédiée (plus courte)
# --------------------------------------------------------------------------------------------------------------------

    Liste_test = []
    for i in range(len(ottomate)):
        if (i > 4):
            Liste_recup = []
            for j in range(len(ottomate[i])):
                    if (j == 0 or j == 1):
                        Liste_recup += ottomate[i][j]
            Liste_test.append(Liste_recup)

# --------------------------------------------------------------------------------------------------------------------
        # Parcour de la liste précédente (liste raccourci) puis création d'une nouvelle liste 1D
        # cette nouvelle liste nous permettra par la suite de notamment de pouvoir
        # comparer chaque indice i du Tableau 2D à ce même tableau 2D, afin pouvoir
        # déterminer par la suite si un état comporte un même caractère vers 2 états
        # différent
# --------------------------------------------------------------------------------------------------------------------

    for i in range(len(Liste_test)):
        Liste_temp = []
        for j in range(len(Liste_test[i])):
            if (j == 0):
                Liste_temp += Liste_test[i][j]
                Liste_temp += Liste_test[i][j+1]
            #print(Liste_temp)

# --------------------------------------------------------------------------------------------------------------------
        # On va maintenant comparer cette indice i ( liste 1D de cette forme : [j0, j1], servant de comparateur )
        # à la liste 2D complète (liste raccourci toujours)
        # Puis dès qu'un indice i ( [j0, j1] ) est identique à notre liste comparatrice,
        # nous allons la placer dans une n-nième liste (Liste_occ) qui va déterminer
        # si il existe un ou plusieurs caractère pour un état
# --------------------------------------------------------------------------------------------------------------------
            Liste_occ = []
            for k in range(len(Liste_test)):
                Liste_rep = []
                for l in range(len(Liste_temp)):
                    for m in range(len(Liste_test[k])):
                        if (Liste_temp[l] == Liste_test[k][m]):
                            Liste_rep += Liste_test[k][m]
                    #print("Liste_temp : ", Liste_temp)

# --------------------------------------------------------------------------------------------------------------------
        # Le cpt ici nous permet de parcourir la liste est déterminer qu'elle contiennent bien 2
        # 2 éléments (elle vire tout les éléments qui ne nous intéresse pas )
# --------------------------------------------------------------------------------------------------------------------
                cpt = 0
                for n in range(len(Liste_rep)):
                    cpt += 1

                if (cpt > 1) :
                    Liste_occ.append(Liste_rep)
            count = 0

            for o in range(len(Liste_occ)):
                count += 1
# --------------------------------------------------------------------------------------------------------------------
        # Le capteur "count" nous sert à parcourir la liste "Lise_occ" et donc
        # déterminer si elle comporte un ou plusieurs indice
        # Si la liste ne comporte qu'un seul élément, alors c'est bon
        # Dans le cas contraire, il existe donc plusieurs caractère pour un
        # même état de départ, l'automate n'est donc pas déterministe
# --------------------------------------------------------------------------------------------------------------------

        if (count > 1):
            verif2 = 0

        # print(count)
        # print(stop)

# --------------------------------------------------------------------------------------------------------------------
        # Règle permettant de déterminer si l'automate est déterministe en fonction des
        # propriété de la déterminisation et dans le cas contraire, d'en montrer la cause
        # puis de retourner la valeur 1 ou 0 selon si il est déterministe ou non (respectivement)
# --------------------------------------------------------------------------------------------------------------------

    #Déterministe
    if verif1 == 1 and verif2 == 1 :
        return 1
    #Non déterministe,car il y a plusieurs états initiaux !
    if verif1 == 0 and verif2 == 1 :
        return 2
    #Cet automate n'est pas déterministe, car il existe plusieurs caractères partant d'une même transition !
    if verif1 == 1 and verif2 == 0 :
        return 3
    #Cet automate n'est pas déterministe car: Il existe plusieurs états initiaux ! ET Il existe plusieurs caractères partant d'une même transition !:
    if verif1 == 0 and verif2 == 0 :
        return 4


# Mettre en argument x + refaire la partie avec les symboles
#--------------------------------------------------------------

def get_liste_trans_etat(Etat,liste_transi):
    Liste_final = []
    for i in range(len(liste_transi)):
        if Etat == get_numbers_trans_av_ap(liste_transi[i])[0]:
            Liste_final.append(liste_transi[i])
    return Liste_final

def get_only_letter(str):
    for i in range(0,len(str)):
        if str[i] > chr(96) and str[i]< chr(105) or str[i]> chr(105) and str[i] < chr(123):
            return str

def get_numbers_trans_av(chaine_trans):
    # Permet de détecter la fin de la chaine
    chaine_trans = chaine_trans + "."
    liste_finale = []
    str = ""
    for i in range(0, len(chaine_trans)):
        # Si le caractère se trouve entre "a" et "z" sans le "i" == symbole de l'automate
        if chaine_trans[i] > chr(96) and chaine_trans[i] < chr(105) or chaine_trans[i] > chr(105) and chaine_trans[i] < chr(123) or chaine_trans[i] == ".":
            liste_finale.append(str)
            str = ""
        else:
            str = str + chaine_trans[i]

    return liste_finale
def get_liste_etats_2(liste_trans):
    liste_finale = []

    for i in range(len(liste_trans)):
        liste_etat = get_numbers_trans_av_ap(liste_trans[i])
        liste_finale.append(liste_etat[0])

    liste_finale = list(set(liste_finale))

    return liste_finale

def verif(Etat,Listetransi):
    if Etat in get_liste_etats_2(Listetransi):
        return 1
    else:
        return 0

def transition(Etat,liste_trans,liste_symbs,Newlist_trans,liste_etat,Liste_temp):
    if verif(Etat,Newlist_trans)==1:
        return Newlist_trans,liste_etat
    else:
        liste_etat.append(Etat)
        Listetrans1 = []
        for x in range(0,len(Etat)):
            for z in range(0, len(liste_trans)):
                        if Etat[x]==liste_trans[z][0]:
                            Listetrans1.append(liste_trans[z])
        for s in range(0, len(liste_symbs)):
                                    transic = ""
                                    for r in range(0, len(Listetrans1)):
                                        if Listetrans1[r][1] == liste_symbs[s]:
                                            # Test pour ne pas avoir de doublon
                                            for e in range(0, len(transic)):
                                                if transic[e] == Listetrans1[r][2]:
                                                    pass
                                            transic += Listetrans1[r][2]
                                    Newlist_trans.append(Etat + liste_symbs[s] + transic)
                                    if verif(transic,Newlist_trans) == 1:
                                        liste_etat.append(transic)
                                    # Affectation des nouveaux états issu de la nouvelle entrée
                                    else :
                                        Liste_temp.append(transic)
                                    # Affectation des transitions issu de la nouvelle entrée

        return Newlist_trans, liste_etat


def determinisatation(liste_symbs, liste_etats_initiaux, liste_etats_terminaux, liste_trans, nb_etats):
    # Merge des entrées
        # New liste etats init
        New_Etat_Init = []
        L = ""
        for i in range(0, len(liste_etats_initiaux)):
            L += liste_etats_initiaux[i]

        New_Etat_Init.append(L)
        Newlist_trans = []
        ListtransEntree = []
        # stockage des transitions issu des entrées
        for j in range(0, len(L)):
            for k in range(0, len(liste_trans)):
                if L[j] == liste_trans[k][0]:
                    ListtransEntree.append(liste_trans[k])
        Liste_etat = []
        Liste_etat.append(L)
        Liste_temp = []
        for s in range(0, len(liste_symbs)):
            transic = ""
            for r in range(0, len(ListtransEntree)):
                if ListtransEntree[r][1] == liste_symbs[s]:
                    # Test pour ne pas avoir de doublon
                    for e in range(0, len(transic)):
                        if transic[e] == ListtransEntree[r][2]:
                            pass
                    transic += ListtransEntree[r][2]
            # Affectation des nouveaux états issu de la nouvelle entrée
            Liste_temp.append(transic)
            # Affectation des transitions issu de la nouvelle entrée
            Newlist_trans.append(L + liste_symbs[s] + transic)
        while len(Liste_temp) != 0:
            for i in range(0, len(Liste_temp)):
                if Liste_temp[i] in Liste_etat:
                    Liste_temp.pop(i)
                    break
                else :
                    Newlist_trans , Liste_etat = transition(Liste_temp[0],liste_trans,liste_symbs,Newlist_trans,Liste_etat,Liste_temp)
                    break
        Liste_etat = list(set(Liste_etat))
        Liste_Etat_t_f = []
        for t in range(0, len(liste_etats_terminaux)):
            for r in range(0, len(Liste_etat)):
                for s in range(0, len(Liste_etat[r])):
                    if Liste_etat[r][s]== liste_etats_terminaux[t]:
                        Liste_Etat_t_f.append(Liste_etat[r])
        Liste_Etat_t_f = list(set(Liste_Etat_t_f))
        nbetatf = 0
        Finaltranslist = Newlist_trans
        Listesymb2 = liste_symbs


        for c in range(0,len(Liste_etat)):
            stockletter = []
            nbetatf +=1
            Listtranstemp = []
            Listtranstemp = get_liste_trans_etat(Liste_etat[c], Newlist_trans)

        return Listesymb2, New_Etat_Init,Liste_Etat_t_f , Newlist_trans, nbetatf






def est_complet_VF(Listessymb2, Newlist_trans) :
    lst_symb = Listessymb2
    lst_trans = Newlist_trans
    verif = 1
    L_element = lst_element_manquantVF(lst_symb, lst_trans)
    #print("L_element : ", L_element)
    if (len(L_element) != 0):
        verif = 0

    if (verif == 0):
        return 0
    else:
        return 1


def completion(Listessymb2, Newlist_trans):

    lst_symb = Listessymb2
    lst_trans =Newlist_trans

    #if (est_complet_VF(lst_symb, lst_trans) != 0) :
    l_compl = lst_element_manquantVF(lst_symb, lst_trans)
    lst_etat_P = []
    lst_sec = []
    for n in range(len(lst_symb)) :
        lst_etat_P.append("P" + lst_symb[n] + "P")
    #print("liste_etat_P : ", lst_etat_P)
    for m in range(len(l_compl)) :
        l_compl[m] += "P"
    #print("L_compl_bis : ", l_compl)


    for o in range(len(l_compl)) :
        lst_sec.append(l_compl[o])
    #print("Lst_sec : ", lst_sec)

    for p in range(len(lst_sec)) :
        str = "".join(lst_sec[p])
        lst_trans.append(str)

    for q in range(len(lst_etat_P)) :
        lst_trans.append(lst_etat_P[q])

    return lst_trans


def lst_element_manquantVF(lst_symb, lst_trans):
    # Récupération d'une liste de état via la liste de transition (sans le symbole) : ETAPE 1
    Liste_etat = []
    for a in range(len(lst_symb)):
        Liste_temp = []
        # Liste_nv permet de recup toute les transitions pour chaque caractère et les ajouter dans une Liste d'état final
        Liste_nv = []
        for b in range(len(lst_trans)):
            Liste_temp2 = []
            for c in range(len(lst_trans[b])):
                if (lst_symb[a] in lst_trans[b]):
                    if (lst_symb[a] != lst_trans[b][c]):
                        Liste_temp2 += lst_trans[b][c]
                    else:
                        break
            Liste_temp.append(Liste_temp2)

        # Boucle permettant d'enlever les listes vides (inutiles) créer à cause des conditions précédentes
        for e in Liste_temp:
            if e:
                Liste_nv.append(e)

        Liste_etat.append(Liste_nv)

    # Elimination des doublons de la liste d'états (correspondant aux états ayant une transition en "a" et en "b" et qui sont donc présent 2 fois)
    Liste_etat_t = []
    for f in range(len(Liste_etat)):
        for g in range(len(Liste_etat[f])):
            if (Liste_etat[f][g] not in Liste_etat_t):
                Liste_etat_t.append(Liste_etat[f][g])
        # print("Liste_nv : ", Liste_nv)

    # Transformation d'une liste 2D en liste simple contenant des str tel que : '013'
    Liste_etat_dep = []
    for h in range(len(Liste_etat_t)):
        str = ''.join(Liste_etat_t[h])
        Liste_etat_dep.append(str)

    # print("Liste_etat : ", Liste_etat)
    #print("Liste état dep : ", Liste_etat_dep)

    # Ajout des symboles à tous les états qui permettrons la comparaison avec les transition de
    # de la déterminisation, ce qui permettra de récuperer les transition manquante (à compléter)
    lst_var = []
    for i in range(len(Liste_etat_dep)):
        for j in range(len(lst_symb)):
            lst_temp = []
            lst_temp += Liste_etat_dep[i] + lst_symb[j]
            lst_var.append(lst_temp)

    # Formation de cette liste de comparaison en str tel que : '013a'
    lst_compl = []
    for k in range(len(lst_var)):
        str = "".join(lst_var[k])
        lst_compl.append(str)
    #print("lst_compl : ", lst_compl)

    # Copie de l'ETAPE 1 mais en gardant cette fois-ci le symbole (ce qui était génant pour en faire une fonction)
    # Cela permettra de comparer les transitions de la déterminisation par rapport à la liste des état totale précédent
    # et de donc de récuperer la liste des transitions manquantes

    Liste_EtatSymb = []
    for a in range(len(lst_symb)):
        Liste_temp = []
        Liste_nv = []
        for b in range(len(lst_trans)):
            Liste_temp2 = []
            for c in range(len(lst_trans[b])):
                if (lst_symb[a] in lst_trans[b]):
                    if (lst_symb[a] != lst_trans[b][c]):
                        Liste_temp2 += lst_trans[b][c]
                    if (lst_symb[a] == lst_trans[b][c]):
                        Liste_temp2 += lst_trans[b][c]
                        break
            Liste_temp.append(Liste_temp2)

        for e in Liste_temp:
            if e:
                Liste_nv.append(e)

        Liste_EtatSymb.append(Liste_nv)

    # print("Liste_EtatSymb : ",Liste_EtatSymb)

    # Elimination des doublons de la liste d'états (correspondant aux états ayant une transition en "a" et en "b" et qui sont donc présent 2 fois)
    Liste_Etat_t = []
    for f in range(len(Liste_EtatSymb)):
        for g in range(len(Liste_EtatSymb[f])):
            if (Liste_EtatSymb[f][g] not in Liste_Etat_t):
                Liste_Etat_t.append(Liste_EtatSymb[f][g])
        # print("Liste_nv : ", Liste_nv)

    # Transformation d'une liste 2D en liste simple contenant des str tel que : '013'
    Liste_Etat_Dep = []
    for h in range(len(Liste_Etat_t)):
        str = ''.join(Liste_Etat_t[h])
        Liste_Etat_Dep.append(str)

    #print("Liste_Etat_Dep : ", Liste_Etat_Dep)

    # Ajout des états manquants dans une nouvelle liste, laquelle sera ajoutée par la suite au transition de
    # l'automate déterminisé (avec la transition en "P")
    lst_trans_supp = []


    for k in range(len(Liste_Etat_Dep)):
        for l in range(len(lst_compl)):
            if (lst_compl[k] not in Liste_Etat_Dep):
                lst_trans_supp += lst_compl[k]


    #print("lst_trans_supp : ", lst_trans_supp)
    return lst_trans_supp
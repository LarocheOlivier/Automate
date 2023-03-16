def est_deterministe():
    # Ouverture du fichier
    with open('automates', "r") as fichier_AF:
        print("\n")
        ottomate = []
        verif1 = 1
        verif2 = 1

        # Lecture des lignes du fichier contenant les automates + ajout dans une liste
        for ligne in fichier_AF:
            L = []
            for ch in ligne:
                    if ch != "\n" and ch != " ":
                        L += ch
            ottomate.append(L)
        #print("ottomate : ", ottomate)

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
                    if (ottomate[i][j] != "1"):
                        #print("pas déterministe, car plus d'une entrée !")
                        verif1 = 0
                    else :
                        #print("une seule entrée !")
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
        print("Liste_test :", Liste_test)

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

            print("Liste_occ : ", Liste_occ)
            # print(count)
            # print(stop)

# --------------------------------------------------------------------------------------------------------------------
        # Règle permettant de déterminer si l'automate est déterministe en fonction des
        # propriété de la déterminisation et dans le cas contraire, d'en montrer la cause
        # puis de retourner la valeur 1 ou 0 selon si il est déterministe ou non (respectivement)
# --------------------------------------------------------------------------------------------------------------------

        if verif1 == 1 and verif2 == 1 :
            print("Cet automate est déterministe !")
            print("\n")
            return 1
        if verif1 == 0 and verif2 == 1 :
            print("Cet n'est pas déterministe, car il y a plusieurs états initiaux !")
            print("\n")
            return 0
        if verif1 == 1 and verif2 == 0 :
            print("Cet automate n'est pas déterministe, car il existe plusieurs caractères partant d'une même transition !")
            print("\n")
            return 0
        if verif1 == 0 and verif2 == 0 :
            print("Cet automate n'est pas déterministe, car : \n")
            print("      - Il existe plusieurs états initiaux !")
            print("      - Il existe plusieurs caractères partant d'une même transition !")
            print("\n")
            return 0








def est_complet():
    print("nothing")

def completion():
    print("nothing")

def determinisation_completion():
    print("nothing")


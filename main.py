#Ce fichier est la boucle principale de ce programme

from affichage import*
from functions import*
#
# Vérification Python
if __name__ == '__main__':

    while True:
        print_main_menu()
        ch = protect_choix(39)
        exec_ch_main(ch)
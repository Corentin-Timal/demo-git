"""
Ecrire l'algorithme de la suite de fibonacci:

C'est une suite définie par Un = Un-1 + Un-2
"""

def élément_fibo(indice:int=1)->int:
    """
    Fonction qui retourne le terme de la suite de Fibonacci d'indice donné.
    
    Param: indice: type int, valeur par défaut 1
    Retourne : type int, fibo(n)
    """
    if indice==1: return 0
    elif indice==2: return 1
    else:
        return élément_fibo(indice-1)+élément_fibo(indice-2)


def fibonacci():
    """
    Fonction qui calcule et affiche les n premiers membres de la suite de Fibonacci (Un= Un-1 + Un-2)
    """

    # L'utilisateur doit saisir le nombre d'éléments de la suite de Fibonacci qu'il veut calculer 
    # (minimum 2 éléments: 0 et 1 ; max 30 éléments pour ne pas faire crasher la machine)
    n_éléments = -1
    while n_éléments<2 or n_éléments>30:
        n_éléments = int(input("Saisir le nombre de termes de la suite de Fibonacci (entre 2 et 30):"))
    
    # Calcul des n premiers éléments de la suite de Fibonacci 
    liste_suite_fibo = [élément_fibo(i+1) for i in range(n_éléments)]
    # Affichage du résultat (sous forme d'éléments en dehors de la liste)
    print("Les {} premiers éléments de la suite de Fibonacci sont :\n".format(n_éléments), ', '.join([str(terme) for terme in liste_suite_fibo]))

    

# Appel de la fonction principale
fibonacci()
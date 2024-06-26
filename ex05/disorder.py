import random

def tri_insertion_decroissant(tab):
    for i in range(1, len(tab)):
        valeur_a_inserer = tab[i]
        position = i

        # Déplacement des éléments plus petits que la valeur à insérer vers la droite
        while position > 0 and tab[position - 1] < valeur_a_inserer:
            tab[position] = tab[position - 1]
            position -= 1

        # Insérer la valeur à sa position correcte
        tab[position] = valeur_a_inserer

# Fonction pour générer un tableau d'entiers aléatoires de plus de 15 indices
def generer_tableau_aleatoire(taille):
    return [random.randint(1, 100) for _ in range(taille)]

# Générer un tableau d'entiers aléatoires de plus de 15 indices
tableau = generer_tableau_aleatoire(20)

print("Tableau initial :", tableau)

# Trier le tableau par ordre décroissant en utilisant la fonction tri_insertion_decroissant
tri_insertion_decroissant(tableau)

print("Tableau trié par ordre décroissant :", tableau)

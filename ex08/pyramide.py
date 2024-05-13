def print_pyramid(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

def main():
    # Demander à l'utilisateur le nombre de lignes
    while True:
        try:
            n = int(input("Entrez le nombre de lignes de la pyramide : "))
            if n > 0:
                break
            else:
                print("Veuillez entrer un entier positif.")
        except ValueError:
            print("Veuillez entrer un entier valide.")

    # Afficher la pyramide
    print_pyramid(n)

if __name__ == "__main__":
    main()

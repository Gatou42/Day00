def count_characters(string):
    count = 0
    for char in string:
        count += 1
    return count

# Exemple d'utilisation :
chaine = "Bonjour, monde !"
print("Nombre de caractères:", count_characters(chaine))

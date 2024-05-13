def alphabet_letters():
    alphabet = ""
    for i in range(ord('a'), ord('z')+1):
        alphabet += chr(i) + " "
    return alphabet

# Utilisation de la fonction
print(alphabet_letters())

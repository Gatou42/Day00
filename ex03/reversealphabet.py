def reverse_alphabet_letters():
    alphabet = ""
    for i in range(ord('z'), ord('a')-1, -1):
        alphabet += chr(i) + " "
    return alphabet

# Utilisation de la fonction
print(reverse_alphabet_letters())

with open("notes.csv", encoding="utf-8") as fichier:
    next(fichier)
    total = 0
    nombre = 0
    for ligne in fichier:
        champs = ligne.strip().split(",")
        total += int(champs[2])
        nombre += 1
print(f"Moyenne générale: {total/nombre :.2f}")
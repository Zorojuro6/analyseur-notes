totaux ={}
compteurs ={}

with open("notes.csv", encoding="utf-8") as fichier:
    next(fichier)
    for ligne in fichier:
        champs = ligne.strip().split(",")
        nom = champs[0]
        note = int(champs[2])
        if nom not in totaux:
            totaux[nom]= 0
            compteurs[nom]= 0
        totaux[nom] += note
        compteurs[nom] += 1 
for nom in totaux:
    print(f"{nom} : {totaux[nom]/ compteurs[nom]:.2f}")
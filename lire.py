totaux ={}
compteurs ={}

with open("notes.csv", encoding="utf-8") as fichier:
    next(fichier)
    meilleure_note = None
    meilleure_nom = ""
    pire_note = None
    pire_nom = ""
    for ligne in fichier:
        champs = ligne.strip().split(",")
        nom = champs[0]
        note = int(champs[2])
        if meilleure_note == None or note > meilleure_note:
            meilleure_note = note
            meilleure_nom = nom
        if pire_note == None or note < pire_note:
            pire_note = note
            pire_nom = nom
        if nom not in totaux:
            totaux[nom]= 0
            compteurs[nom]= 0
        totaux[nom] += note
        compteurs[nom] += 1 
for nom in totaux:
    print(f"{nom} : {totaux[nom]/ compteurs[nom]:.2f}")
print(f"Meilleure note: {meilleure_note} ({meilleure_nom})")
print(f"Pire note: {pire_note} ({pire_nom})")
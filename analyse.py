def lire_notes(chemin):
    eleves = []
    with open(chemin, encoding="utf-8") as fichier:
        next(fichier)
        for ligne in fichier:
            champs = ligne.strip().split(",")
            try:
                note = int(champs[2])
            except ValueError:
                continue
            eleves.append({"nom": champs[0], "matiere": champs[1], "note": note})
    return eleves

if __name__ == "__main__":
    print(lire_notes("notes.csv"))                
            
    
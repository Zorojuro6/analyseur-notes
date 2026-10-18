def lire_notes(chemin):
    eleves = []
    ignorees = 0
    with open(chemin, encoding="utf-8") as fichier:
        next(fichier)
        for ligne in fichier:
            champs = ligne.strip().split(",")
            try:
                note = int(champs[2])
            except ValueError:
                ignorees += 1
                continue
            eleves.append({"nom": champs[0], "matiere": champs[1], "note": note})
    return eleves, ignorees

def moyennes(eleves):
    totaux = {}
    compteurs = {}
    for ligne in eleves:
        nom = ligne["nom"]
        if nom not in totaux:
            totaux[nom] = 0
            compteurs[nom] = 0
        totaux[nom] += ligne["note"]
        compteurs[nom] += 1
    resultat ={}
    for nom in totaux:
        resultat[nom] = totaux[nom]/compteurs[nom]
    return resultat        
if __name__ == "__main__":
    eleves, ignorees = lire_notes("invalid.csv")
    print(moyennes(eleves))
    if ignorees>0:
        print(f"Attention: {ignorees} ligne(s) ignorée(s)")
                    
            
    
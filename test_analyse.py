from analyse import moyennes, lire_notes, meilleure_note, pire_note

def test_moyennes():
    eleves = [
        {"nom": "Marie", "matiere": "Maths", "note": 10},
        {"nom":"Marie", "matiere":"Maths", "note": 20},
        {"nom":"Paul", "matiere":"Maths", "note": 12},
    ]
    assert moyennes(eleves) == {"Marie": 15, "Paul": 12}

def test_moyennes_liste_vide():
    assert moyennes([]) == {}

def test_lire_notes_ignore_les_lignes_invalides():
    eleves, ignorees = lire_notes("invalid.csv")
    assert len(eleves) == 2
    assert ignorees == 1

def test_moyennes_par_matiere():
    eleves = [
        {"nom": "Marie", "matiere": "Maths", "note": 10},
        {"nom":"Paul", "matiere":"Maths", "note": 14},
        {"nom":"Marie", "matiere":"Info", "note": 18},
    ]
    assert moyennes(eleves, "matiere") == {"Maths": 12, "Info": 18}
    
def test_meilleure_note_avec_notes_negatives():
    eleves = [
        {"nom": "Ana", "matiere": "Maths", "note": -3},
        {"nom":"Leo", "matiere":"Maths", "note": -5},
    ]
    assert meilleure_note(eleves)["nom"]=="Ana"

def test_pire_note_avec_notes_negatives():
    eleves = [
        {"nom": "Ana", "matiere": "Maths", "note":-3},
        {"nom":"Leo", "matiere":"Maths", "note": -5},
    ]
    assert pire_note(eleves)["nom"] == "Leo"

def test_notes_liste_vide():
    assert meilleure_note([]) is None
    assert pire_note([]) is None

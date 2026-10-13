from analyse import moyennes 

def test_moyennes():
    eleves = [
        {"nom": "Marie", "matiere": "Maths", "note": 10},
        {"nom":"Marie", "matiere":"Maths", "note": 20},
        {"nom":"Paul", "matiere":"Maths", "note": 12},
    ]
    assert moyennes(eleves) == {"Marie": 15, "Paul": 12}

def test_moyennes_liste_vide():
    assert moyennes([]) == {}
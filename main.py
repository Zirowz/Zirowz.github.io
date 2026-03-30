import random
import unicodedata

def clean(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn').lower().replace(" ", "")

prenoms_h = ["Lucas", "Nathan", "Hugo", "Enzo", "Louis", "Gabriel", "Arthur", "Jules"]
prenoms_f = ["Emma", "Léa", "Chloé", "Manon", "Inès", "Camille", "Sarah", "Jade"]

noms_rue = ["de la République", "Victor Hugo", "Jean Jaurès", "du Général de Gaulle", "des Écoles", "de la Gare"]
villes_cp = [
    ("Paris", "750"),
    ("Lyon", "690"),
    ("Marseille", "130"),
    ("Toulouse", "310"),
    ("Nice", "060"),
    ("Nantes", "440")
]

domaines = ["gmail.com", "outlook.fr", "hotmail.fr"]

nom = input("Nom : ")
prenom = input("Prénom : ")

age = random.randint(18, 65)

ville, debut_cp = random.choice(villes_cp)
code_postal = debut_cp + str(random.randint(10, 99))

numero = random.randint(1, 150)
rue = random.choice(noms_rue)

parent1 = random.choice(prenoms_h)
parent2 = random.choice(prenoms_f)

base_email = clean(prenom) + "." + clean(nom)
style = random.choice([
    base_email,
    base_email + str(random.randint(1,99)),
    clean(prenom)[0] + clean(nom),
    clean(prenom) + clean(nom) + str(random.randint(10,99))
])
email = style + "@" + random.choice(domaines)

print("\n--- Profil fictif ---")
print(f"Nom : {nom}")
print(f"Prénom : {prenom}")
print(f"Âge : {age} ans")
print(f"Adresse : {numero} rue {rue}, {code_postal} {ville}")
print(f"Père : {parent1} {nom}")
print(f"Mère : {parent2} {nom}")
print(f"Email : {email}")

import random
import unicodedata
import json

def clean(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn').lower().replace(" ", "")

prenoms_h = ["Lucas", "Nathan", "Hugo", "Enzo", "Louis", "Gabriel", "Arthur", "Jules"]
prenoms_f = ["Emma", "Léa", "Chloé", "Manon", "Inès", "Camille", "Sarah", "Jade"]

noms = ["Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard", "Petit", "Durand"]

noms_rue = ["de la République", "Victor Hugo", "Jean Jaurès", "du Général de Gaulle", "des Écoles", "de la Gare"]
villes_cp = [
    ("Paris", "750"),
    ("Lyon", "690"),
    ("Marseille", "130"),
    ("Toulouse", "310"),
    ("Nice", "060"),
    ("Nantes", "440")
]

domaines = ["gmail.com", "outlook.fr", "hotmail.fr"]

def gen_tel():
    return "0" + str(random.choice([6,7])) + "".join([str(random.randint(0,9)) for _ in range(8)])

def gen_personne(id):
    sexe = random.choice(["H", "F"])
    prenom = random.choice(prenoms_h if sexe == "H" else prenoms_f)
    nom = random.choice(noms)

    age = random.randint(18, 65)

    ville, debut_cp = random.choice(villes_cp)
    code_postal = debut_cp + str(random.randint(10, 99))

    numero = random.randint(1, 150)
    rue = random.choice(noms_rue)

    parent1 = random.choice(prenoms_h)
    parent2 = random.choice(prenoms_f)

    base_email = clean(prenom) + "." + clean(nom)
    style = random.choice([
        base_email,
        base_email + str(random.randint(1,99)),
        clean(prenom)[0] + clean(nom),
        clean(prenom) + clean(nom) + str(random.randint(10,99))
    ])
    email = style + "@" + random.choice(domaines)

    return {
        "id": id,
        "prenom": prenom,
        "nom": nom,
        "age": age,
        "adresse": f"{numero} rue {rue}, {code_postal} {ville}",
        "pere": f"{parent1} {nom}",
        "mere": f"{parent2} {nom}",
        "email": email,
        "telephone": gen_tel()
    }

base = []

nb = int(input("Nombre de profils à générer : "))

for i in range(nb):
    base.append(gen_personne(i+1))

for personne in base:
    print(personne)

with open("fake_database.json", "w", encoding="utf-8") as f:
    json.dump(base, f, indent=4, 
    ensure_ascii=False)
    
    import random
import unicodedata
import sqlite3

def clean(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn').lower().replace(" ", "")

prenoms_h = ["Lucas", "Nathan", "Hugo", "Enzo", "Louis", "Gabriel", "Arthur", "Jules"]
prenoms_f = ["Emma", "Léa", "Chloé", "Manon", "Inès", "Camille", "Sarah", "Jade"]

noms = ["Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard", "Petit", "Durand"]

noms_rue = ["de la République", "Victor Hugo", "Jean Jaurès", "du Général de Gaulle", "des Écoles", "de la Gare"]
villes_cp = [
    ("Paris", "750"),
    ("Lyon", "690"),
    ("Marseille", "130"),
    ("Toulouse", "310"),
    ("Nice", "060"),
    ("Nantes", "440")
]

domaines = ["gmail.com", "outlook.fr", "hotmail.fr"]

def gen_tel():
    return "0" + str(random.choice([6,7])) + "".join([str(random.randint(0,9)) for _ in range(8)])

def gen_personne():
    sexe = random.choice(["H", "F"])
    prenom = random.choice(prenoms_h if sexe == "H" else prenoms_f)
    nom = random.choice(noms)
    age = random.randint(18, 65)

    ville, debut_cp = random.choice(villes_cp)
    code_postal = debut_cp + str(random.randint(10, 99))

    numero = random.randint(1, 150)
    rue = random.choice(noms_rue)

    parent1 = random.choice(prenoms_h)
    parent2 = random.choice(prenoms_f)

    base_email = clean(prenom) + "." + clean(nom)
    style = random.choice([
        base_email,
        base_email + str(random.randint(1,99)),
        clean(prenom)[0] + clean(nom),
        clean(prenom) + clean(nom) + str(random.randint(10,99))
    ])
    email = style + "@" + random.choice(domaines)

    return (
        prenom,
        nom,
        age,
        f"{numero} rue {rue}, {code_postal} {ville}",
        f"{parent1} {nom}",
        f"{parent2} {nom}",
        email,
        gen_tel()
    )

conn = sqlite3.connect("fake_database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prenom TEXT,
    nom TEXT,
    age INTEGER,
    adresse TEXT,
    pere TEXT,
    mere TEXT,
    email TEXT,
    telephone TEXT
)
""")

nb = int(input("Nombre de profils à générer : "))

for _ in range(nb):
    cursor.execute("""
    INSERT INTO utilisateurs (prenom, nom, age, adresse, pere, mere, email, telephone)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, gen_personne())

conn.commit()

cursor.execute("SELECT * FROM utilisateurs")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
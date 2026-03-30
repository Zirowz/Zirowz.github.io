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
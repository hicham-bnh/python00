# 🌱 Python Garden Community

*Learn Python fundamentals through gardening scenarios*

---

## 📖 À propos du projet

Bienvenue dans **Python Garden Community** !  
Ce projet pédagogique enseigne les concepts fondamentaux de Python à travers des exercices thématiques autour du jardinage. Chaque exercice est conçu pour vous aider à progresser pas à pas en vous amusant. 🌿

---

## 📁 Structure du projet

```
python-garden/
│
├── ex0/
│   └── ft_hello_garden.py
│
├── ex1/
│   └── ft_plot_area.py
│
├── ex2/
│   └── ft_harvest_total.py
│
├── ex3/
│   └── ft_plant_age.py
│
├── ex4/
│   └── ft_water_reminder.py
│
├── ex5/
│   ├── ft_count_harvest_iterative.py
│   └── ft_count_harvest_recursive.py
│
├── ex6/
│   └── ft_garden_summary.py
│
└── ex7/
    └── ft_seed_inventory.py
```

---

## 🚀 Exercices

### 🌿 Exercice 0 : Hello Garden
**Fonction :** `ft_hello_garden`  
**Objectif :** Afficher un message de bienvenue à la communauté

```python
def ft_hello_garden():
    print("Hello, Garden Community!")
```

---

### 📐 Exercice 1 : Surface du parterre
**Fonction :** `ft_plot_area`  
**Objectif :** Calculer et afficher la surface d'un parterre

```python
def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(f"Plot area: {length * width}")
```

---

### 🥕 Exercice 2 : Total de la récolte
**Fonction :** `ft_harvest_total`  
**Objectif :** Calculer le poids total de la récolte sur 3 jours

```python
def ft_harvest_total():
    day_1 = int(input("Day 1 harvest: "))
    day_2 = int(input("Day 2 harvest: "))
    day_3 = int(input("Day 3 harvest: "))
    print(f"Total harvest: {day_1 + day_2 + day_3}")
```

---

### 🌾 Exercice 3 : Vérification de l'âge de la plante
**Fonction :** `ft_plant_age`  
**Objectif :** Vérifier si une plante est prête pour la récolte selon son âge

```python
def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
```

---

### 💧 Exercice 4 : Rappel d'arrosage
**Fonction :** `ft_water_reminder`  
**Objectif :** Rappeler quand arroser les plantes

```python
def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
```

---

### ⏳ Exercice 5 : Compter jusqu'à la récolte
**Fonctions :** `ft_count_harvest_iterative` & `ft_count_harvest_recursive`  
**Objectif :** Compter les jours jusqu'à la récolte (itératif et récursif)

#### Version itérative
```python
def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")
```

#### Version récursive
```python
def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    
    def count_day(i):
        if i <= days:
            print(f"Day {i}")
            count_day(i + 1)
    
    count_day(1)
    print("Harvest time!")
```

---

### 📊 Exercice 6 : Résumé du jardin
**Fonction :** `ft_garden_summary`  
**Objectif :** Afficher un résumé du jardin (nom et nombre de plantes)

```python
def ft_garden_summary():
    garden_name = input("Enter garden name: ")
    plant_count = int(input("Enter number of plants: "))
    print(f"Garden: {garden_name}")
    print(f"Plants: {plant_count}")
    print("Status: Growing well!")
```

---

### 🌰 Exercice 7 : Inventaire de graines
**Fonction :** `ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None`  
**Objectif :** Gérer l'inventaire de graines avec annotations de type

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
```

---

## 🔧 Démarrage

- Installation : Aucun package spécial requis — juste Python 3.x !
- Exécution : Chaque fichier est autonome. Exemple :
```bash
python ex0/ft_hello_garden.py
```
- Contribution : Les contributions sont les bienvenues via des pull requests.

---

## 🎯 Objectifs d'apprentissage

Maîtriser les bases de Python :
- Entrée/sortie utilisateur
- Calculs et opérations simples
- Conditions
- Boucles (itératives & récursives)
- Fonctions et annotations de type
- Manipulation de chaînes

---

> "The best time to plant a tree was 20 years ago. The second best time is now."

---

## Badges

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white) ![Level](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge) ![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

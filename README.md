<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Garden Community - README Preview</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
            font-size: 16px;
            line-height: 1.5;
            color: #1f2328;
            background-color: #0d1117;
            padding: 0;
        }

        .container {
            max-width: 1012px;
            margin: 0 auto;
            padding: 32px;
            background-color: #0d1117;
        }

        .readme-box {
            background-color: #0d1117;
            border: 1px solid #30363d;
            border-radius: 6px;
            padding: 32px;
            color: #e6edf3;
        }

        h1 {
            font-size: 2em;
            font-weight: 600;
            padding-bottom: 0.3em;
            margin-bottom: 16px;
            border-bottom: 1px solid #21262d;
            color: #e6edf3;
        }

        h2 {
            font-size: 1.5em;
            font-weight: 600;
            padding-bottom: 0.3em;
            margin-top: 24px;
            margin-bottom: 16px;
            border-bottom: 1px solid #21262d;
            color: #e6edf3;
        }

        h3 {
            font-size: 1.25em;
            font-weight: 600;
            margin-top: 24px;
            margin-bottom: 16px;
            color: #e6edf3;
        }

        h4 {
            font-size: 1em;
            font-weight: 600;
            margin-top: 16px;
            margin-bottom: 8px;
            color: #e6edf3;
        }

        p {
            margin-bottom: 16px;
            color: #e6edf3;
        }

        hr {
            height: 2px;
            padding: 0;
            margin: 24px 0;
            background-color: #21262d;
            border: 0;
        }

        code {
            padding: 0.2em 0.4em;
            margin: 0;
            font-size: 85%;
            background-color: rgba(110,118,129,0.4);
            border-radius: 6px;
            font-family: ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace;
            color: #e6edf3;
        }

        pre {
            padding: 16px;
            overflow: auto;
            font-size: 85%;
            line-height: 1.45;
            background-color: #161b22;
            border-radius: 6px;
            margin-bottom: 16px;
            border: 1px solid #30363d;
        }

        pre code {
            display: inline;
            padding: 0;
            margin: 0;
            overflow: visible;
            line-height: inherit;
            word-wrap: normal;
            background-color: transparent;
            border: 0;
            font-size: 100%;
            color: #e6edf3;
        }

        strong {
            font-weight: 600;
            color: #e6edf3;
        }

        ul {
            padding-left: 2em;
            margin-bottom: 16px;
        }

        li {
            margin-top: 0.25em;
            color: #e6edf3;
        }

        blockquote {
            padding: 0 1em;
            color: #7d8590;
            border-left: 0.25em solid #30363d;
            margin: 0 0 16px 0;
        }

        blockquote em {
            font-style: italic;
        }

        .center {
            text-align: center;
        }

        img {
            max-width: 100%;
            height: auto;
        }

        a {
            color: #58a6ff;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="readme-box">
            <h1>🌱 Python Garden Community</h1>
            <p>🎓 Une série d'exercices Python pour apprendre la programmation</p>
            <hr>

            <h2>📖 À propos du projet</h2>
            <p>Hey! Bienvenue dans <strong>Python Garden Community</strong>, un projet pédagogique qui introduit les <strong>concepts fondamentaux de Python</strong> à travers des scénarios de jardinage.<br>
            Chaque exercice est conçu pour maîtriser progressivement les bases de la programmation.</p>
            <hr>

            <h2>📁 Structure du projet</h2>
            <pre><code>python-garden/
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
    └── ft_seed_inventory.py</code></pre>
            <hr>

            <h2>🚀 Les Exercices</h2>

            <h3>🌿 Exercice 0 : Hello Garden</h3>
            <p><strong>Fonction :</strong> <code>ft_hello_garden</code><br>
            <strong>Objectif :</strong> Afficher un message de bienvenue à la communauté de jardinage.</p>
            <pre><code>def ft_hello_garden():
    print("Hello, Garden Community!")</code></pre>
            <hr>

            <h3>📐 Exercice 1 : Garden Plot Area</h3>
            <p><strong>Fonction :</strong> <code>ft_plot_area</code><br>
            <strong>Objectif :</strong> Demander la longueur et la largeur d'un terrain, puis calculer et afficher la superficie.</p>
            <pre><code>def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(f"Plot area: {length * width}")</code></pre>
            <hr>

            <h3>🥕 Exercice 2 : Harvest Total</h3>
            <p><strong>Fonction :</strong> <code>ft_harvest_total</code><br>
            <strong>Objectif :</strong> Demander le poids des récoltes de 3 jours et calculer le total.</p>
            <pre><code>def ft_harvest_total():
    day_1 = int(input("Day 1 harvest: "))
    day_2 = int(input("Day 2 harvest: "))
    day_3 = int(input("Day 3 harvest: "))
    print(f"Total harvest: {day_1 + day_2 + day_3}")</code></pre>
            <hr>

            <h3>🌾 Exercice 3 : Plant Age Check</h3>
            <p><strong>Fonction :</strong> <code>ft_plant_age</code><br>
            <strong>Objectif :</strong> Demander l'âge d'une plante en jours et vérifier si elle est prête à récolter.</p>
            <pre><code>def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")</code></pre>
            <hr>

            <h3>💧 Exercice 4 : Water Reminder</h3>
            <p><strong>Fonction :</strong> <code>ft_water_reminder</code><br>
            <strong>Objectif :</strong> Demander depuis combien de jours la plante n'a pas été arrosée et afficher un message de rappel.</p>
            <pre><code>def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")</code></pre>
            <hr>

            <h3>⏳ Exercice 5 : Count to Harvest</h3>
            <p><strong>Fonctions :</strong> <code>ft_count_harvest_iterative</code> et <code>ft_count_harvest_recursive</code><br>
            <strong>Objectif :</strong> Compter les jours jusqu'à la récolte, soit de manière itérative soit de manière récursive.</p>

            <h4>Version itérative</h4>
            <pre><code>def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")</code></pre>

            <h4>Version récursive</h4>
            <pre><code>def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    
    def count_day(i):
        if i <= days:
            print(f"Day {i}")
            count_day(i + 1)
    
    count_day(1)
    print("Harvest time!")</code></pre>
            <hr>

            <h3>📊 Exercice 6 : Garden Summary</h3>
            <p><strong>Fonction :</strong> <code>ft_garden_summary</code><br>
            <strong>Objectif :</strong> Afficher un résumé du jardin avec son nom et le nombre de plantes.</p>
            <pre><code>def ft_garden_summary():
    garden_name = input("Enter garden name: ")
    plant_count = int(input("Enter number of plants: "))
    print(f"Garden: {garden_name}")
    print(f"Plants: {plant_count}")
    print("Status: Growing well!")</code></pre>
            <hr>

            <h3>🌰 Exercice 7 : Seed Inventory with Type Annotations</h3>
            <p><strong>Fonction :</strong> <code>ft_seed_inventory</code><br>
            <strong>Objectif :</strong> Gérer l'inventaire des graines, en affichant des informations sur le type et la quantité des graines.</p>
            <pre><code>def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")</code></pre>
            <hr>

            <h2>🔧 Instructions</h2>
            <ul>
                <li><strong>Installation :</strong> Aucun besoin d'installation spécifique, Python 3.x suffit pour exécuter ces scripts.</li>
                <li><strong>Exécution :</strong> Chaque fichier est un script autonome. Pour l'exécuter, lance le fichier correspondant :
                    <pre><code>python ex0/ft_hello_garden.py</code></pre>
                </li>
                <li><strong>Contributions :</strong> Si tu veux contribuer, n'hésite pas à proposer des améliorations ou des corrections via des pull requests.</li>
            </ul>
            <hr>

            <h2>🎯 Objectifs pédagogiques</h2>
            <p>Ces exercices permettent de découvrir et de pratiquer :</p>
            <ul>
                <li>✅ Entrées/sorties utilisateur</li>
                <li>✅ Calculs et opérations de base</li>
                <li>✅ Structures conditionnelles</li>
                <li>✅ Boucles (itératives et récursives)</li>
                <li>✅ Fonctions et annotations de type</li>
                <li>✅ Gestion de chaînes de caractères</li>
            </ul>
            <hr>

            <blockquote>
                <p><em>"Le meilleur moment pour planter un arbre était il y a 20 ans. Le deuxième meilleur moment, c'est maintenant."</em></p>
            </blockquote>
            <hr>

            <p class="center">
                <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
            </p>
        </div>
    </div>
</body>
</html>

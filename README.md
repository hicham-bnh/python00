<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Garden Community</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
            color: #e0e6f0;
            line-height: 1.6;
            padding: 40px 20px;
        }

        .container {
            max-width: 1100px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            margin-bottom: 60px;
            padding: 40px 20px;
            background: linear-gradient(135deg, rgba(76, 175, 80, 0.1), rgba(139, 195, 74, 0.1));
            border-radius: 20px;
            border: 2px solid rgba(76, 175, 80, 0.3);
            box-shadow: 0 8px 32px rgba(76, 175, 80, 0.15);
        }

        h1 {
            font-size: 3.5em;
            font-weight: 700;
            background: linear-gradient(135deg, #4CAF50, #8BC34A);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 15px;
            text-shadow: 0 0 30px rgba(76, 175, 80, 0.5);
        }

        .subtitle {
            font-size: 1.3em;
            color: #9ca3af;
            font-weight: 300;
        }

        .section {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .section:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 40px rgba(76, 175, 80, 0.2);
        }

        h2 {
            font-size: 2em;
            color: #4CAF50;
            margin-bottom: 20px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        h3 {
            font-size: 1.5em;
            color: #8BC34A;
            margin: 25px 0 15px 0;
            font-weight: 600;
        }

        h4 {
            font-size: 1.2em;
            color: #9ca3af;
            margin: 15px 0 10px 0;
            font-weight: 500;
        }

        .divider {
            height: 2px;
            background: linear-gradient(90deg, transparent, #4CAF50, transparent);
            margin: 40px 0;
            border-radius: 2px;
        }

        pre {
            background: #1a1f3a;
            border: 1px solid rgba(76, 175, 80, 0.3);
            border-radius: 10px;
            padding: 20px;
            overflow-x: auto;
            margin: 15px 0;
            box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.3);
        }

        code {
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            color: #a5d6a7;
        }

        .inline-code {
            background: rgba(76, 175, 80, 0.2);
            padding: 3px 8px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            color: #8BC34A;
            font-size: 0.9em;
        }

        .info-box {
            background: rgba(76, 175, 80, 0.1);
            border-left: 4px solid #4CAF50;
            padding: 15px 20px;
            margin: 20px 0;
            border-radius: 5px;
        }

        .info-box strong {
            color: #4CAF50;
        }

        ul {
            list-style: none;
            padding-left: 0;
        }

        li {
            padding: 8px 0 8px 30px;
            position: relative;
        }

        li:before {
            content: "🌱";
            position: absolute;
            left: 0;
        }

        .quote {
            text-align: center;
            font-size: 1.3em;
            font-style: italic;
            color: #9ca3af;
            padding: 30px;
            margin: 40px 0;
            border-left: 4px solid #4CAF50;
            background: rgba(76, 175, 80, 0.05);
            border-radius: 10px;
        }

        .badges {
            text-align: center;
            margin: 40px 0;
        }

        .badges img {
            margin: 10px;
            transition: transform 0.3s ease;
        }

        .badges img:hover {
            transform: scale(1.1);
        }

        .exercise-card {
            background: linear-gradient(135deg, rgba(76, 175, 80, 0.05), rgba(139, 195, 74, 0.05));
            border-radius: 12px;
            padding: 25px;
            margin: 20px 0;
            border: 1px solid rgba(76, 175, 80, 0.2);
            transition: all 0.3s ease;
        }

        .exercise-card:hover {
            border-color: #4CAF50;
            box-shadow: 0 5px 25px rgba(76, 175, 80, 0.2);
        }

        .tree-structure {
            background: #0d1117;
            border: 1px solid rgba(76, 175, 80, 0.3);
            border-radius: 10px;
            padding: 20px;
            font-family: 'Courier New', monospace;
            color: #8BC34A;
        }

        strong {
            color: #4CAF50;
            font-weight: 600;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌱 Python Garden Community</h1>
            <p class="subtitle">Learn Python fundamentals through gardening scenarios</p>
        </div>

        <div class="section">
            <h2>📖 About This Project</h2>
            <p>Welcome to <strong>Python Garden Community</strong>! This is an educational project that teaches <strong>fundamental Python concepts</strong> through engaging gardening-themed exercises. Each exercise is carefully designed to help you progressively master programming basics while having fun! 🌿</p>
        </div>

        <div class="divider"></div>

        <div class="section">
            <h2>📁 Project Structure</h2>
            <div class="tree-structure">
<code>python-garden/
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
    └── ft_seed_inventory.py</code>
            </div>
        </div>

        <div class="divider"></div>

        <div class="section">
            <h2>🚀 Exercises</h2>

            <div class="exercise-card">
                <h3>🌿 Exercise 0: Hello Garden</h3>
                <div class="info-box">
                    <strong>Function:</strong> <span class="inline-code">ft_hello_garden</span><br>
                    <strong>Goal:</strong> Display a welcome message to the gardening community
                </div>
                <pre><code>def ft_hello_garden():
    print("Hello, Garden Community!")</code></pre>
            </div>

            <div class="exercise-card">
                <h3>📐 Exercise 1: Garden Plot Area</h3>
                <div class="info-box">
                    <strong>Function:</strong> <span class="inline-code">ft_plot_area</span><br>
                    <strong>Goal:</strong> Calculate and display the area of a garden plot
                </div>
                <pre><code>def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(f"Plot area: {length * width}")</code></pre>
            </div>

            <div class="exercise-card">
                <h3>🥕 Exercise 2: Harvest Total</h3>
                <div class="info-box">
                    <strong>Function:</strong> <span class="inline-code">ft_harvest_total</span><br>
                    <strong>Goal:</strong> Calculate the total harvest weight over 3 days
                </div>
                <pre><code>def ft_harvest_total():
    day_1 = int(input("Day 1 harvest: "))
    day_2 = int(input("Day 2 harvest: "))
    day_3 = int(input("Day 3 harvest: "))
    print(f"Total harvest: {day_1 + day_2 + day_3}")</code></pre>
            </div>

            <div class="exercise-card">
                <h3>🌾 Exercise 3: Plant Age Check</h3>
                <div class="info-box">
                    <strong>Function:</strong> <span class="inline-code">ft_plant_age</span><br>
                    <strong>Goal:</strong> Check if a plant is ready to harvest based on age
                </div>
                <pre><code>def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")</code></pre>
            </div>

            <div class="exercise-card">
                <h3>💧 Exercise 4: Water Reminder</h3>
                <div class="info-box">
                    <strong>Function:</strong> <span class="inline-code">ft_water_reminder</span><br>
                    <strong>Goal:</strong> Remind when to water plants
                </div>
                <pre><code>def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")</code></pre>
            </div>

            <div class="exercise-card">
                <h3>⏳ Exercise 5: Count to Harvest</h3>
                <div class="info-box">
                    <strong>Functions:</strong> <span class="inline-code">ft_count_harvest_iterative</span> & <span class="inline-code">ft_count_harvest_recursive</span><br>
                    <strong>Goal:</strong> Count days until harvest using iteration or recursion
                </div>
                <h4>Iterative Version</h4>
                <pre><code>def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")</code></pre>
                <h4>Recursive Version</h4>
                <pre><code>def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    
    def count_day(i):
        if i <= days:
            print(f"Day {i}")
            count_day(i + 1)
    
    count_day(1)
    print("Harvest time!")</code></pre>
            </div>

            <div class="exercise-card">
                <h3>📊 Exercise 6: Garden Summary</h3>
                <div class="info-box">
                    <strong>Function:</strong> <span class="inline-code">ft_garden_summary</span><br>
                    <strong>Goal:</strong> Display a garden summary with name and plant count
                </div>
                <pre><code>def ft_garden_summary():
    garden_name = input("Enter garden name: ")
    plant_count = int(input("Enter number of plants: "))
    print(f"Garden: {garden_name}")
    print(f"Plants: {plant_count}")
    print("Status: Growing well!")</code></pre>
            </div>

            <div class="exercise-card">
                <h3>🌰 Exercise 7: Seed Inventory</h3>
                <div class="info-box">
                    <strong>Function:</strong> <span class="inline-code">ft_seed_inventory</span><br>
                    <strong>Goal:</strong> Manage seed inventory with type annotations
                </div>
                <pre><code>def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")</code></pre>
            </div>
        </div>

        <div class="divider"></div>

        <div class="section">
            <h2>🔧 Getting Started</h2>
            <ul>
                <li><strong>Installation:</strong> No special installation needed - just Python 3.x!</li>
                <li><strong>Running:</strong> Each file is standalone. Execute with:
                    <pre><code>python ex0/ft_hello_garden.py</code></pre>
                </li>
                <li><strong>Contributing:</strong> Feel free to submit improvements via pull requests!</li>
            </ul>
        </div>

        <div class="section">
            <h2>🎯 Learning Goals</h2>
            <p>Master these Python fundamentals:</p>
            <ul>
                <li>User input/output operations</li>
                <li>Basic calculations and operations</li>
                <li>Conditional statements</li>
                <li>Loops (iterative & recursive)</li>
                <li>Functions and type annotations</li>
                <li>String manipulation</li>
            </ul>
        </div>

        <div class="quote">
            "The best time to plant a tree was 20 years ago. The second best time is now."
        </div>

        <div class="badges">
            <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
            <img src="https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge" alt="Level">
            <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">
        </div>
    </div>
</body>
</html>
